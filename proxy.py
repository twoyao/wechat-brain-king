import json
import sqlite3
from urllib.parse import parse_qs

import requests
from mitmproxy import ctx

db = sqlite3.connect('data.sqlite')

question_cache = {}


def search_guess(question, options):
    content = requests.get("http://www.baidu.com/s", params={'wd': question}).text

    counts = list(map(lambda x: (x[0], content.count(x[1])), enumerate(options)))

    max_idx, max_count = max(counts, key=lambda x: x[1])
    options[max_idx] += "[%d]" % max_count

    min_idx, min_count = min(counts, key=lambda x: x[1])
    options[min_idx] += "[%d]" % min_count


# content: roomID=3035629668&quizNum=2&uid=78233430&t=1516643742431&sign=1d5f9061ea1e70c57240de2e4bd04d38
def question_key(content):
    qs = parse_qs(content.decode('utf-8'))
    key = "{}:{}".format(qs["roomID"][0], qs["quizNum"][0])
    return key


def query_string(question, opts):
    return question.strip() + "|" + "|".join(sorted(opts))


def intercept_quiz(req, rsp):
    r = json.loads(rsp.content)
    question = r['data']['quiz']
    options = r['data']['options']

    q = question.strip() + "|" + "|".join(sorted(options))
    row = db.execute("SELECT answer FROM quiz WHERE q == ?", [q]).fetchone()
    if row:
        ans_idx = options.index(row[0])
        ctx.log("正确答案为 %d" % (ans_idx + 1))
        options[ans_idx] += "[正确答案]"
    else:
        # 暂存问题
        key = question_key(req.content)
        question_cache[key] = (q, list(options))

        # 使用百度搜索计数法猜测答案
        search_guess(question, options)

    rsp.text = json.dumps(r)


def update_answer(req, rsp):
    key = question_key(req.content)
    cached = question_cache.pop(key, None)
    if cached:
        answer_idx = json.loads(rsp.content)["data"]["answer"] - 1
        q, options = cached

        with db:
            row = (q, options[answer_idx])
            ctx.log.info("save record: {}".format(row))
            db.execute("INSERT INTO quiz(q, answer) VALUES (?, ?)", row)


def response(flow):
    req = flow.request
    rsp = flow.response

    if req.host != 'question.hortor.net':
        return

    path = req.path
    if path == '/question/bat/findQuiz':
        intercept_quiz(req, rsp)

    if path == '/question/bat/choose':
        update_answer(req, rsp)

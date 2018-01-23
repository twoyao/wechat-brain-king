## /question/bat/findQuiz

```http
POST https://question.hortor.net/question/bat/findQuiz HTTP/1.1
Content-type: application/x-www-form-urlencoded

roomID=3035629668&quizNum=2&uid=78233430&t=1516643742431&sign=1d5f9061ea1e70c57240de2e4bd04d38
```

```http
HTTP/1.1 200 OK
Content-Type:	application/json; charset=utf-8

{
	"data": {
		"quiz": "中国四大美人中「杨贵妃」是哪位皇帝的宠妃？",
		"options": ["唐太宗", "唐高宗", "唐代宗", "唐玄宗"],
		"num": 1,
		"school": "文科",
		"type": "历史",
		"typeID": 3,
		"contributor": "麦小贝",
		"partner": 0,
		"endTime": 1516642338,
		"curTime": 1516642324,
		"myBuff": {
			"3": 0
		}
	},
	"errcode": 0
}
```

## /question/bat/choose 

```http
POST https://question.hortor.net/question/bat/choose 
Content-type: application/x-www-form-urlencoded

roomID=3035629668&quizNum=2&option=1&uid=78233430&t=1516643760537&sign=4f666a626d40ed3cf20194418d1449d0
```

```http
HTTP/1.1 200 OK
Content-Type:	application/json; charset=utf-8

{
	"data": {
		"uid": 0,
		"num": 1,
		"answer": 4, 
		"option": 4,
		"yes": true,
		"score": 120,
		"baseScore": 120,
		"extraScore": {},
		"totalScore": 120,
		"rowNum": 0,
		"rowMult": 0,
		"costTime": 4,
		"roomId": 3034265328,
		"enemyScore": 180,
		"enemyAnswer": 4
	},
	"errcode": 0
}
```

### 返回体

字段 | 含义
---- | ----
data.answer | 正确答案
data.option | 用户选择
data.yes | 是否正确


### /question/bat/fightResult

```http
POST https://question.hortor.net/question/bat/fightResult HTTP/1.1
Content-type:	application/x-www-form-urlencoded

roomID=3035629668&type=0&uid=78233430&t=1516643803430&sign=2f5df04cebd1283a914c78e9e119b246
```

```http
HTTP/1.1 200 OK
Content-Type:	application/json; charset=utf-8

{
	"data": {
		"score": 200,
		"rowNum": 1,
		"addGold": 710,
		"baseGold": 1900,
		"extraGold": {},
		"gold": 32108,
		"addExp": 220,
		"baseExp": 220,
		"extraExp": {},
		"exp": 1205,
		"maxExp": 1979,
		"level": 25,
		"isOut": false,
		"isWin": 1,
		"rowWinNum": 1,
		"rivalScore": 160,
		"rivalRowNum": 1,
		"rivalIsOut": false,
		"itemInfo": {
			"itemId": 0,
			"itemNum": 0
		},
		"groupScore": 0,
		"matchID": 300014,
		"selfMatch": 300014,
		"star": 6,
		"beforeMatch": 300014,
		"beforeStar": 5,
		"winBack": false,
		"myBuff": {
			"3": 0
		}
	},
	"errcode": 0
}
```

# 介绍

头脑王者辅助工具。通过HTTPS代理的方式在答题选项中插入正确答案。
如果题库(当前16709条)中有该问题，则在问题后会插入 **\[正确答案选项\]**。
如果题库中没有该问题，通过百度查找问题，并在选项中插入其在搜索结果页面中出现的次数(最多和最少)。

# 使用方法

## 在电脑上启动代理服务器

```bash
pip3 install -r requirements.txt
mitmproxy -p 8888 -s proxy.py
```

## 在手机上设置代理地址

保证手机与电脑使用同一局域网下，设置代理地址。


<div style="display: flex;flex-flow: row; align-items:flex-start;">

<img src="https://raw.githubusercontent.com/twoyao/wechat-brain-king/master/images/proxy_1.jpg" width="300" height="500"> 
<img src="https://raw.githubusercontent.com/twoyao/wechat-brain-king/master/images/proxy_2.jpg" width="300" height="500"> 

</div>

在手机浏览器上打开 http://mitm.it 下载并安装mitmproxy根证书

![](images/cert.png)

## 开始答题

配置完成后就可以开始答题了，代理会影响其他APP的访问速度，答题完后记得将手机代理重置。

<img src="https://raw.githubusercontent.com/twoyao/wechat-brain-king/master/images/bat.jpg" width="300" height="500">

## 感谢

使用mitmproxy的点子来自[hortor_cheater](https://github.com/chxj1992/hortor_cheater)

原始题库来自[tounao](https://github.com/wansir/tounao)
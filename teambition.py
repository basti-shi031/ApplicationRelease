import requests
import json


def initCookies(c):
    cookies = {}  # 初始化cookies字典变量
    for line in c.split(';'):  # 按照字符：进行划分读取
        # 其设置为1就会把字符串拆分成2份
        name, value = line.strip().split('=', 1)
        cookies[name] = value  # 为字典cookies添加内容
    return cookies


class Teambition(object):
    def __init__(self, c, getUrl, postId):
        self.c = c;
        self.cookies = initCookies(c)
        self.getUrl = getUrl
        self.postId = postId

    def update(self, data):
        headers = {'content-type': 'application/json'}
        payload = {'content': data}
        response = requests.put(url='https://www.teambition.com/api/posts/' + self.postId,
                                data=json.dumps(payload), headers=headers, cookies=self.cookies)
        print("teambition更新成功")

    def get(self):
        updateUrl = 'https://www.teambition.com/api/posts/%s/activities?_postId=%s&_=1486136195044'
        headers = {
            'upgrade - insecure - requests': '1',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'accept-encoding': 'gzip, deflate, sdch, br',
            'accept-language': 'zh-CN,zh;q=0.8',
            'cache-control': 'no-cache',
            'pragma': 'no-cache',
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36'}
        response = requests.get(
            updateUrl % (self.postId, self.postId),
            headers=headers,
            cookies=self.cookies)
        latestResponse = response.json()[0]
        content = latestResponse.get('content').get('content')
        return content

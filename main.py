from requests import Session
from requests.structures import CaseInsensitiveDict
import json


class OSHWHubSession(Session):
    def __init__(self):
        super().__init__()
        self._is_login = False
        self._login_cookies = None
        self._getCookies()

    def login(self):
        self.headers = CaseInsensitiveDict({
            'authority': 'oshwhub.com',
            'pragma': 'no-cache',
            'cache-control': 'no-cache',
            'dnt': '1',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'sec-fetch-site': 'none',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-user': '?1',
            'sec-fetch-dest': 'document',
            'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8',
            'cookie': self._login_cookies,
        })

        resp = self.get(url='https://oshwhub.com/sign_in')

        self._is_login = True
        # TODO: 添加判断登录成功的检测

    def signIn(self):
        if self._is_login:
            resp = self.post(url='https://oshwhub.com/api/user/sign_in')
            print(resp.json())
        else:
            print('未登录')

    def _getCookies(self):
        try:
            with open('config.json', 'r') as f:
                self._login_cookies = json.load(f)['cookies']
            print('成功从配置文件加载cookies')

        except FileNotFoundError:
            print('配置文件不存在')
            self._login_cookies = input('请输入cookies')
            with open('config.json', 'w') as f:
                json.dump({"cookies": self._login_cookies}, f)
            print('cookies已保存')
    # TODO: 添加获取已签到天数/签到礼物


if __name__ == '__main__':
    sess = OSHWHubSession()
    sess.login()
    sess.signIn()

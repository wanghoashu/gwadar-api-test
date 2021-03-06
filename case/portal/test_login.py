from common import Common
import requests


class TestLogin(object):
    common = None

    @classmethod
    def setup_class(cls):
        cls.common = Common()

    def test_normal_login(self):
        """
        正确的账号和密码登录
        """

        headers = {'Api-Version': 'v1',
                   'Device-Platform': 'android',
                   'App-Channel': 'alpha',
                   'App-Type': 'customer',
                   'App-Version': '1.0.0',
                   'Device-Id': 'ABCDEFG',
                   'Device-Model': 'RedMi Note 4X',
                   'Device-Version': '7.1'}
        # TODO 是否有必要封装到Common中
        response_login = requests.post(TestLogin.common.url_root + '/api/portal/login', headers=headers,
                                       data={'email': 'zhaowende',
                                             'password': '8d969eef6ecad3c29a3a629280e686cf0c3f5d5a86aff3ca12020c923adc6c92'})
        print(response_login.status_code)
        print(response_login.text)
        assert 200 == response_login.status_code

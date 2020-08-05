from common import Common


class TestLogin(object):

    def test_normal_login(self):
        """
        正确的账号和密码登录
        """
        comm = Common()
        response_login = comm.post('/api/oms/login', '', {'usernameOrEmail': 'zhaowende',
                                                          'password': '8d969eef6ecad3c29a3a629280e686cf0c3f5d5a86aff3ca12020c923adc6c92'})
        assert 200 == response_login.status_code

    def test_wrong_username_or_password(self):
        """
        错误的账号和密码登录
        """
        comm = Common()
        response_login = comm.post('/api/oms/login', '', {'usernameOrEmail': 'wrong', 'password': 'wrong'})
        assert 400 == response_login.status_code

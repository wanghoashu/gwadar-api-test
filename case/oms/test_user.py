from common import Common
from case.oms.base import get_access_token


class TestUser(object):
    access_token = None

    @classmethod
    def setup_class(cls):
        cls.access_token = get_access_token()

    def test_get_user(self):
        """
        获取个人信息是否成功
        """
        comm = Common(token=TestUser.access_token)
        print("access_token")
        response_user = comm.get('/api/oms/users/me')
        print(response_user.text)
        assert 200 == response_user.status_code

from common import Common
from case.oms.base import get_access_token


class TestUser(object):
    common = None

    @classmethod
    def setup_class(cls):
        cls.common = Common(token=get_access_token())

    def test_get_user(self):
        """
        获取个人信息是否成功
        """
        response_user = TestUser.common.get('/api/oms/users/me')
        print(response_user.text)
        assert 200 == response_user.status_code

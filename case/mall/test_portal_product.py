import json
import os

from base import get_portal_access_token
from common import Common


class TestPortalProduct(object):
    product_id = None
    common = None

    @classmethod
    def setup_class(cls):
        cls.common = Common(token=get_portal_access_token())

    def test_add_product(self):
        """
        发布商品
        """
        url = '/api/portal/products'
        root_path = os.path.abspath(os.path.dirname(__file__)).split('case')[0]
        files = {
            "mediaFile1": (
                'test.png', open(root_path + 'resources/test.png', 'rb').read())
        }
        params = {
            "title": "商品标题",
            "description": "商品详情",
            "isShare": "false",
            "price": "10.00",
            "stock": "1"
        }
        response = TestPortalProduct.common.post(url, params=params, files=files)
        assert 201 == response.status_code
        TestPortalProduct.product_id = json.loads(response.text)['id']
        print(TestPortalProduct.product_id)

    def test_update_product(self):
        """
        修改商品
        """
        print()

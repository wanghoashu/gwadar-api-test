import json
import os

from base import get_portal_access_token, get_oms_access_token
from common import Common


class TestOmsProduct(object):
    oms_common = None
    portal_common = None
    product_id = None

    @classmethod
    def setup_class(cls):
        cls.oms_common = Common(token=get_oms_access_token())
        cls.portal_common = Common(token=get_portal_access_token())

        # 构造数据
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
        response = cls.portal_common.post('/api/portal/products', params=params, files=files)
        assert 201 == response.status_code
        cls.product_id = json.loads(response.text)['id']

    @classmethod
    def teardown_class(cls):
        # 删除商品
        response = cls.portal_common.delete('/api/portal/products/' + cls.product_id)
        assert 204 == response.status_code

    def test_get_product(self):
        """
        查询商品
        """
        url = '/api/oms/products/' + TestOmsProduct.product_id
        print(TestOmsProduct.product_id)
        response = TestOmsProduct.oms_common.get(url)
        print(response.text)
        assert 200 == response.status_code

    def test_get_product_with_wrong_id(self):
        """
        查询商品，无效的ID
        """
        url = '/api/oms/products/111111111'
        response = TestOmsProduct.oms_common.get(url)
        print(response.text)
        assert 400 == response.status_code

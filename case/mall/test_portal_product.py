import json
import os

from base import get_portal_access_token
from common import Common


class TestPortalProduct(object):
    product_id = None
    portalCommon = None

    @classmethod
    def setup_class(cls):
        cls.portalCommon = Common(token=get_portal_access_token())

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
        response = TestPortalProduct.portalCommon.post(url, params=params, files=files)
        assert 201 == response.status_code
        TestPortalProduct.product_id = json.loads(response.text)['id']
        print(TestPortalProduct.product_id)

    def test_update_product(self):
        """
        修改商品
        """
        print()

    def test_delete_product(self):
        """
        删除商品
        """
        url = '/api/portal/products/' + TestPortalProduct.product_id
        response = TestPortalProduct.portalCommon.delete(url)
        print(response.text)
        assert 204 == response.status_code

    def test_delete_product_with_wrong_id(self):
        """
        删除商品
        """
        url = '/api/portal/products/11111111'
        response = TestPortalProduct.portalCommon.delete(url)
        print(response.text)
        assert 400 == response.status_code

    def test_complete_process(self):
        """
        增删改查完整流程
        """
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
        response = TestPortalProduct.portalCommon.post('/api/portal/products', params=params, files=files)
        assert 201 == response.status_code

        product_id = json.loads(response.text)['id']

        response = TestPortalProduct.portalCommon.get('/api/portal/products/' + product_id)
        assert 200 == response.status_code

        response = TestPortalProduct.portalCommon.delete('/api/portal/products/' + product_id)
        assert 204 == response.status_code

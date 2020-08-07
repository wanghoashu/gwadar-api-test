import json

from base import get_oms_access_token
from common import Common


class TestOmsProductCategory(object):
    oms_common = None
    product_category_id = None
    second_product_category_id = None

    @classmethod
    def setup_class(cls):
        cls.oms_common = Common(token=get_oms_access_token())

    def test_add_product_category(self):
        """
        添加一级商品分类
        """
        url = '/api/oms/product-categories'
        response = TestOmsProductCategory.oms_common.post_with_json(url, {
            "name": "一级分类"
        })
        if 201 == response.status_code:
            assert 201 == response.status_code
            TestOmsProductCategory.product_category_id = json.loads(response.text)['id']
            print(TestOmsProductCategory.product_category_id)
        elif '4001057' == response.headers['error-code']:
            assert 400 == response.status_code
            assert 'The upper limit is 30' == response.headers['error-message']
        elif '4001058' == response.headers['error-code']:
            assert 400 == response.status_code
            assert 'Product category name already exists' == response.headers['error-message']

    def test_add_second_product_category(self):
        """
        添加二级商品分类
        """
        url = '/api/oms/product-categories'
        response = TestOmsProductCategory.oms_common.post_with_json(url, {
            "parentId": TestOmsProductCategory.product_category_id,
            "name": "二级分类",
            "iconKey": "mall.xxx.jpg"
        })
        if 201 == response.status_code:
            assert 201 == response.status_code
            TestOmsProductCategory.second_product_category_id = json.loads(response.text)['id']
            print(TestOmsProductCategory.second_product_category_id)
        elif '4001030' == response.headers['error-code']:
            assert 400 == response.status_code
            assert 'Content does not exist' == response.headers['error-message']
        elif '4001057' == response.headers['error-code']:
            assert 400 == response.status_code
            assert 'The upper limit is 30' == response.headers['error-message']
        elif '4001058' == response.headers['error-code']:
            assert 400 == response.status_code
            assert 'Product category name already exists' == response.headers['error-message']

    def test_delete_second_product_category(self):
        """
        删除二级商品分类
        """
        url = '/api/oms/product-categories/' + TestOmsProductCategory.second_product_category_id
        response = TestOmsProductCategory.oms_common.delete(url)
        assert 204 == response.status_code
        
    def test_delete_product_category(self):
        """
        删除一级商品分类
        """
        url = '/api/oms/product-categories/' + TestOmsProductCategory.product_category_id
        response = TestOmsProductCategory.oms_common.delete(url)
        assert 204 == response.status_code

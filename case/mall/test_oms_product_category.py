import json

from base import get_oms_access_token
from common import Common


class TestOmsProductCategory(object):
    oms_common = None
    product_id = None

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
        if '4001057' == response.headers['error-code']:
            assert 400 == response.status_code
            assert 'The upper limit is 30' == response.headers['error-message']
        elif '4001058' == response.headers['error-code']:
            assert 400 == response.status_code
            assert 'Product category name already exists' == response.headers['error-message']
        else:
            assert 201 == response.status_code
            TestOmsProductCategory.product_category_id = json.loads(response.text)['id']
            print(TestOmsProductCategory.product_category_id)

    def test_add_second_product_category(self):
        """
        添加二级商品分类
        """
        url = '/api/oms/product-categories'
        response = TestOmsProductCategory.oms_common.post_with_json(url, {
            "parentId": "1",
            "name": "二级分类",
            "iconKey": "mall.xxx.jpg"
        })
        if '4001030' == response.headers['error-code']:
            assert 400 == response.status_code
            assert 'Content does not exist' == response.headers['error-message']
        elif '4001057' == response.headers['error-code']:
            assert 400 == response.status_code
            assert 'The upper limit is 30' == response.headers['error-message']
        elif '4001058' == response.headers['error-code']:
            assert 400 == response.status_code
            assert 'Product category name already exists' == response.headers['error-message']
        else:
            assert 201 == response.status_code
            TestOmsProductCategory.product_category_id = json.loads(response.text)['id']
            print(TestOmsProductCategory.product_category_id)

    def test_get_product_category(self):
        """
        查询商品分类
        """
        url = '/api/oms/products/' + TestOmsProductCategory.product_id
        print(TestOmsProductCategory.product_id)
        response = TestOmsProductCategory.oms_common.get(url)
        print(response.text)
        assert 200 == response.status_code

    def test_get_product_with_wrong_id(self):
        """
        查询商品，无效的ID
        """
        url = '/api/oms/products/111111111'
        response = TestOmsProductCategory.oms_common.get(url)
        print(response.text)
        assert 400 == response.status_code

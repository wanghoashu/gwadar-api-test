# 广告位新闻相关接口测试
import json
from common import Common
from case.oms.base import get_access_token

class TestAdverts(object):

    adverts_id = None
    common = None

    @classmethod
    def setUp_class(cls):
        cls.common = Common(token=get_access_token)

    def test_add_news_adverts(self):
        """
        添加广告位新闻
        """
        url = '/api/oms/news-adverts'
        print('token:', TestAdverts.common.token)
        advertsData = {
            "contentUrl": "https://www.baidu.com",
            "name": "test_adverts",
            "pictureKey": "news/006b1f6f47529d9bcf167302e5054c3d.png",
            "weight": 70
        }
        response = TestAdverts.common.post_with_json(url, data=advertsData)
        assert 201 == response.status_code
        TestAdverts.adverts_id = json.loads(response.text)['id']



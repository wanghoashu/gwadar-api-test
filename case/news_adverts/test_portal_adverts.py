# portal 广告位新闻相关接口测试

import json
from common import Common
from base import get_portal_access_token
from base import get_oms_access_token


class Test_portal_adverts(object):
    # 初始化参数
    portal_adverts = None
    portal_common = None
    oms_common = None

    @classmethod
    def setup_class(cls):
        cls.oms_common = Common(token=get_oms_access_token())
        cls.portal_common = Common(token=get_portal_access_token())

    # 构造数据：修改广告位新闻配置中广告显示几率配置为100
        response = cls.oms_common.put_with_json('/api/oms/news-adverts/configs/1', {
             "displayProbability": 100,
             "id": 1
        })
        assert 204 == response.status_code

    def test_get_portal_news_adverts(self):
        """
        portal端获取需要展示的广告接口测试
        """
        url = '/api/portal/news-adverts/random'
        response = self.portal_common.get(url)

        assert 200 == response.status_code

    def test_config_portal_news_adverts(self):
        """
        portal端根据是否显示配置获取广告
        """
        url = '/api/portal/news-adverts/random-nullable'
        response = self.portal_common.get(url)

        except_result = json.loads(response.text)

        assert except_result is not None
        assert 200 == response.status_code










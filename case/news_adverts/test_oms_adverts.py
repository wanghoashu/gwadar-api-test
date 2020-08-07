# oms广告位新闻相关接口测试
import json
from common import Common
from base import get_oms_access_token


class TestAdverts(object):
    # 初始化参数：设置两个参数存储广告新闻id及access_token
    adverts_id = None
    common = None

    @classmethod
    def setup_class(cls):
        cls.common = Common(token=get_oms_access_token())

    def test_add_news_adverts(self):
        """
        添加广告位新闻
        """
        url = '/api/oms/news-adverts'
        advertsData = {
            "contentUrl": "https://www.baidu.com",
            "name": "test_adverts",
            "pictureKey": "news/006b1f6f47529d9bcf167302e5054c3d.png",
            "weight": 70
        }
        response = TestAdverts.common.post_with_json(url, advertsData)
        TestAdverts.adverts_id = json.loads(response.text)['id']
        # 判断添加广告位新闻接口code是否为201
        assert 201 == response.status_code

    def test_update_news_adverts(self):
        """
         更新广告位新闻
        """
        url = '/api/oms/news-adverts/' + TestAdverts.adverts_id
        # 数据中更新了weight字段值由70改为80
        advertsUpdte = {
            "contentUrl": "https://www.baidu.com",
            "name": "test_adverts",
            "pictureKey": "news/006b1f6f47529d9bcf167302e5054c3d.png",
            "weight": 80,
            "id": TestAdverts.adverts_id
        }
        response = TestAdverts.common.put_with_json(url, advertsUpdte)
        # 判断更新广告位新闻接口code是否为204
        assert 204 == response.status_code

    def test_update_news_adverts_check(self):
        """
        调用查询接口检查更新广告是否成功
        """
        url = '/api/oms/news-adverts/' + TestAdverts.adverts_id
        response = TestAdverts.common.get(url)
        exceptWeight = json.loads(response.text)['weight']
        # 判断查询广告位新闻接口code是否为200
        assert 200 == response.status_code
        # 判断weight是否修改成功
        assert 80 == exceptWeight

    def test_unpublished_news_adverts(self):
        """
        下线广告位新闻接口验证
        """
        url = '/api/oms/news-adverts/' + TestAdverts.adverts_id + '/status/unpublished'
        response = TestAdverts.common.put(url)
        # 判断下线广告新闻接口code是否为204
        assert 204 == response.status_code

    def test_unpublished_news_adverts_check(self):
        """
        调用查询接口检查下线广告位新闻是否成功
        """
        url = '/api/oms/news-adverts/' + TestAdverts.adverts_id
        response = TestAdverts.common.get(url)
        exceptState = json.loads(response.text)['status']
        # 判断广告新闻状态是否为UNPUBLISHED
        assert "UNPUBLISHED" == exceptState

    def test_published_news_adverts(self):
        """
        上线广告位新闻接口验证
        """
        url = '/api/oms/news-adverts/' + TestAdverts.adverts_id + '/status/published'
        response = TestAdverts.common.put(url)
        # 判断上线广告新闻接口code是否为204
        assert 204 == response.status_code

    def test_published_news_adverts_check(self):
        """
        调用查询接口检查上线广告位新闻是否成功
        """
        url = '/api/oms/news-adverts/' + TestAdverts.adverts_id
        response = TestAdverts.common.get(url)
        exceptState = json.loads(response.text)['status']
        # 判断广告新闻状态是否为PUBLISHED
        assert "PUBLISHED" == exceptState

    def test_get_news_adverts(self):
        """
        查询广告位新闻列表
        """
        url = '/api/oms/news-adverts/'
        advertData = {
            "page": "1",
            "pageSize": "10"
        }
        response = TestAdverts.common.get(url, params=advertData)
        exceptAdvertsId = json.loads(response.text)[0]['id']
        # 判断广告位新闻列表中首个数据的广告id是否为本次新增的广告新闻id
        assert exceptAdvertsId == TestAdverts.adverts_id

    def test_update_news_adverts_config(self):
        """
        修改广告位新闻配置   广告显示几率 displayProbability:0
        """
        url = '/api/oms/news-adverts/configs/1'
        configData = {
            "displayProbability": 0,
            "id": "1"
        }
        response = TestAdverts.common.put_with_json(url, params=configData)
        # 判断修改广告位新闻code是否为204
        assert 204 == response.status_code

    def test_news_adverts_config_check(self):
        """
        调用查询接口检查广告位配置修改是否成功
        """
        url = '/api/oms/news-adverts/config'
        response = TestAdverts.common.get(url)
        exceptConfig = json.loads(response.text)['displayProbability']
        # 广告位配置修改字段displayProbability是否为0
        assert 0 == exceptConfig

    def test_delete_news_adverts(self):
        """
        删除创建的广告位新闻
        """
        url = '/api/oms/news-adverts/' + TestAdverts.adverts_id
        response = TestAdverts.common.delete(url)
        # 删除广告位新闻code是否为204
        assert 204 == response.status_code

    def test_delete_news_adverts_check(self):
        """
        调用查询接口检查删除广告位新闻是否成功
        """
        url = '/api/oms/news-adverts/' + TestAdverts.adverts_id
        response = TestAdverts.common.get(url)
        # 删除的广告位新闻后code是否为400
        assert 400 == response.status_code

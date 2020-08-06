import json
from common import Common
from base import get_oms_access_token


class TestOmsFlight(object):
    flight_id = None
    common = None

    @classmethod
    def setup_class(cls):
        cls.common = Common(token=get_oms_access_token())

    def test_add_flight(self):
        """
        添加航班
        """
        url = '/api/oms/flights'
        print('token:', TestOmsFlight.common.token)
        response = TestOmsFlight.common.post_with_json(url, {
            "flightNumber": "001",
            "startCity": "tj",
            "endCity": "bj",
            "startTime": "2020-01-01 00:00:00",
            "endTime": "2020-01-02 00:00:00"
        })
        assert 201 == response.status_code
        TestOmsFlight.flight_id = json.loads(response.text)['id']

    def test_add_flight_with_wrong_flight_number(self):
        """
        添加航班, 航班号超长
        """
        print('token:', TestOmsFlight.common.token)
        url = '/api/oms/flights'
        response = TestOmsFlight.common.post_with_json(url, {
            "flightNumber": "12345678901",
            "startCity": "tj",
            "endCity": "bj",
            "startTime": "2020-01-01 00:00:00",
            "endTime": "2020-01-02 00:00:00"
        })
        assert 400 == response.status_code

    def test_update_flight(self):
        """
        修改航班
        """
        url = '/api/oms/flights/' + TestOmsFlight.flight_id
        response = TestOmsFlight.common.put_with_json(url, {
            "id": TestOmsFlight.flight_id,
            "flightNumber": "001",
            "startCity": "tj1",
            "endCity": "bj1",
            "startTime": "2020-01-02 00:00:00",
            "endTime": "2020-01-03 00:00:00"
        })
        print(response.text)
        assert 204 == response.status_code

    def test_update_flight_with_wrong_flight_number(self):
        """
        修改航班，航班号超长
        """
        url = '/api/oms/flights/' + TestOmsFlight.flight_id
        response = TestOmsFlight.common.put_with_json(url, {
            "id": TestOmsFlight.flight_id,
            "flightNumber": "12345678901",
            "startCity": "tj1",
            "endCity": "bj1",
            "startTime": "2020-01-02 00:00:00",
            "endTime": "2020-01-03 00:00:00"
        })
        print(response.text)
        assert 400 == response.status_code

    def test_get_flight(self):
        """
        查询航班
        """
        url = '/api/oms/flights/' + TestOmsFlight.flight_id
        response = TestOmsFlight.common.get(url)
        print(response.text)
        assert 200 == response.status_code

    def test_get_filght_list(self):
        url = '/api/oms/flights'
        response = TestOmsFlight.common.get(url, params={'page': 1, 'pageSize': 10})
        print(response.text)
        assert 200 == response.status_code

    def test_get_flight_with_wrong_id(self):
        """
        查询航班，无效的ID
        """
        url = '/api/oms/flights/111111111'
        response = TestOmsFlight.common.get(url)
        print(response.text)
        assert 400 == response.status_code

    def test_delete_flight(self):
        """
        删除航班
        """
        url = '/api/oms/flights/' + TestOmsFlight.flight_id
        response = TestOmsFlight.common.delete(url)
        print(response.text)
        assert 204 == response.status_code

    def test_delete_flight_with_wrong_id(self):
        """
        删除航班
        """
        url = '/api/oms/flights/111111110'
        response = TestOmsFlight.common.delete(url)
        print(response.text)
        assert 400 == response.status_code

    def test_complete_process(self):
        """
        增删改查完整流程
        """
        response = TestOmsFlight.common.post_with_json('/api/oms/flights', {
            "flightNumber": "001",
            "startCity": "tj",
            "endCity": "bj",
            "startTime": "2020-01-01 00:00:00",
            "endTime": "2020-01-02 00:00:00"
        })
        assert 201 == response.status_code

        flight_id = json.loads(response.text)['id']
        response = TestOmsFlight.common.put_with_json('/api/oms/flights/' + flight_id, {
            "id": str(flight_id),
            "flightNumber": "001",
            "startCity": "tj1",
            "endCity": "bj1",
            "startTime": "2020-01-02 00:00:00",
            "endTime": "2020-01-03 00:00:00"
        })
        assert 204 == response.status_code

        response = TestOmsFlight.common.get('/api/oms/flights/' + flight_id)
        assert 200 == response.status_code

        response = TestOmsFlight.common.delete('/api/oms/flights/' + flight_id)
        assert 204 == response.status_code

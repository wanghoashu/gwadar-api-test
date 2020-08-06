import json
from common import Common
from base import get_oms_access_token
from base import get_portal_access_token


class TestPortalFlight(object):
    omsCommon = None
    portalCommon = None
    flight_id_list = []

    @classmethod
    def setup_class(cls):
        cls.omsCommon = Common(token=get_oms_access_token())
        cls.portalCommon = Common(token=get_portal_access_token())

        # 构造数据
        response = cls.omsCommon.post_with_json('/api/oms/flights', {
            "flightNumber": "001",
            "startCity": "tj",
            "endCity": "bj",
            "startTime": "2020-01-01 00:00:00",
            "endTime": "2020-01-02 00:00:00"
        })
        assert 201 == response.status_code
        flight_id = json.loads(response.text)['id']
        cls.flight_id_list.append(flight_id)

        # 上线航班
        cls.omsCommon.put('/api/oms/flights/' + flight_id + '/status/published')

        response = cls.omsCommon.post_with_json('/api/oms/flights', {
            "flightNumber": "002",
            "startCity": "tj",
            "endCity": "bj",
            "startTime": "2020-01-03 00:00:00",
            "endTime": "2020-01-04 00:00:00"
        })
        assert 201 == response.status_code
        flight_id = json.loads(response.text)['id']
        cls.flight_id_list.append(flight_id)

        # 上线航班
        cls.omsCommon.put('/api/oms/flights/' + flight_id + '/status/published')

    @classmethod
    def teardown_class(cls):
        for flight_id in cls.flight_id_list:
            # 下线航班
            response = cls.omsCommon.put('/api/oms/flights/' + flight_id + '/status/offline')
            assert 204 == response.status_code

            # 删除航班
            response = cls.omsCommon.delete('/api/oms/flights/' + flight_id)
            assert 204 == response.status_code

    def test_get_flight_list(self):
        response = self.portalCommon.get('/api/portal/flights',
                                         params={'startCity': 'tj', 'endCity': 'bj', 'date': '2020-01-01'})
        assert 200 == response.status_code
        result_list = json.loads(response.text)
        print(result_list)
        assert 1 == len(result_list)

    def test_get_exists_flight_day(self):
        response = self.portalCommon.get('/api/portal/flights/exists-flight-day',
                                         params={'startCity': 'tj', 'endCity': 'bj', 'month': '2020-01'})

        assert 200 == response.status_code
        result_list = json.loads(response.text)
        print(result_list)
        assert 2 == len(result_list)

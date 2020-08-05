import json
from common import Common
from case.oms.base import get_access_token


class TestFlight(object):
    flight_id = None
    access_token = None

    @classmethod
    def setup_class(cls):
        cls.access_token = get_access_token()

    def test_add_flight(self):
        """
        添加航班
        """
        print('添加航班')
        url = '/api/oms/flights'
        comm = Common()
        response = comm.post_with_json(url, TestFlight.access_token, {
            "flightNumber": "001",
            "startCity": "tj",
            "endCity": "bj",
            "startTime": "2020-01-01 00:00:00",
            "endTime": "2020-01-02 00:00:00"
        })
        assert 201 == response.status_code
        TestFlight.flight_id = json.loads(response.text)['id']

    def test_update_flight(self):
        """
        修改航班
        """
        print('flight_id', TestFlight.flight_id)
        print('修改航班')
        url = '/api/oms/flights/' + TestFlight.flight_id
        comm = Common()
        response = comm.put_with_json(url, TestFlight.access_token, {
            "id": TestFlight.flight_id,
            "flightNumber": "001",
            "startCity": "tj1",
            "endCity": "bj1",
            "startTime": "2020-01-02 00:00:00",
            "endTime": "2020-01-03 00:00:00"
        })
        print(response.text)
        assert 204 == response.status_code

    def test_get_flight(self):
        """
        查询航班
        """
        print('查询航班')
        url = '/api/oms/flights/' + TestFlight.flight_id
        comm = Common()
        response = comm.get(url, token=TestFlight.access_token)
        print(response.text)
        assert 200 == response.status_code

    def test_delete_flight(self):
        """
        删除航班
        """
        print('删除航班')
        url = '/api/oms/flights/' + TestFlight.flight_id
        comm = Common()
        response = comm.delete(url, token=TestFlight.access_token)
        print(response.text)
        assert 204 == response.status_code

    def test_complete_process(self):
        """
        增删改查完整流程
        """
        print('增删改查完整流程')
        comm = Common()
        response = comm.post_with_json('/api/oms/flights', TestFlight.access_token, {
            "flightNumber": "001",
            "startCity": "tj",
            "endCity": "bj",
            "startTime": "2020-01-01 00:00:00",
            "endTime": "2020-01-02 00:00:00"
        })
        assert 201 == response.status_code

        flight_id = json.loads(response.text)['id']
        response = comm.put_with_json('/api/oms/flights/' + flight_id, TestFlight.access_token, {
            "id": str(flight_id),
            "flightNumber": "001",
            "startCity": "tj1",
            "endCity": "bj1",
            "startTime": "2020-01-02 00:00:00",
            "endTime": "2020-01-03 00:00:00"
        })
        assert 204 == response.status_code

        response = comm.get('/api/oms/flights/' + flight_id, token=TestFlight.access_token)
        assert 200 == response.status_code

        response = comm.delete('/api/oms/flights/' + flight_id, token=TestFlight.access_token)
        assert 204 == response.status_code

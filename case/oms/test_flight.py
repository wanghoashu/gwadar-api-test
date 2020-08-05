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
        url = '/api/oms/flights'
        comm = Common(token=TestFlight.access_token)
        response = comm.post_with_json(url, {
            "flightNumber": "001",
            "startCity": "tj",
            "endCity": "bj",
            "startTime": "2020-01-01 00:00:00",
            "endTime": "2020-01-02 00:00:00"
        })
        assert 201 == response.status_code
        TestFlight.flight_id = json.loads(response.text)['id']

    def test_add_flight_with_wrong_flight_number(self):
        """
        添加航班, 航班号超长
        """
        url = '/api/oms/flights'
        comm = Common(token=TestFlight.access_token)
        response = comm.post_with_json(url, {
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
        url = '/api/oms/flights/' + TestFlight.flight_id
        comm = Common(token=TestFlight.access_token)
        response = comm.put_with_json(url, {
            "id": TestFlight.flight_id,
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
        url = '/api/oms/flights/' + TestFlight.flight_id
        comm = Common(token=TestFlight.access_token)
        response = comm.put_with_json(url, {
            "id": TestFlight.flight_id,
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
        url = '/api/oms/flights/' + TestFlight.flight_id
        comm = Common(token=TestFlight.access_token)
        response = comm.get(url)
        print(response.text)
        assert 200 == response.status_code

    def test_get_flight_with_wrong_id(self):
        """
        查询航班，无效的ID
        """
        url = '/api/oms/flights/111111111'
        comm = Common(token=TestFlight.access_token)
        response = comm.get(url)
        print(response.text)
        assert 400 == response.status_code

    def test_delete_flight(self):
        """
        删除航班
        """
        url = '/api/oms/flights/' + TestFlight.flight_id
        comm = Common(token=TestFlight.access_token)
        response = comm.delete(url)
        print(response.text)
        assert 204 == response.status_code

    def test_delete_flight_with_wrong_id(self):
        """
        删除航班
        """
        url = '/api/oms/flights/111111110'
        comm = Common(token=TestFlight.access_token)
        response = comm.delete(url)
        print(response.text)
        assert 400 == response.status_code

    def test_complete_process(self):
        """
        增删改查完整流程
        """
        comm = Common(token=TestFlight.access_token)
        response = comm.post_with_json('/api/oms/flights', {
            "flightNumber": "001",
            "startCity": "tj",
            "endCity": "bj",
            "startTime": "2020-01-01 00:00:00",
            "endTime": "2020-01-02 00:00:00"
        })
        assert 201 == response.status_code

        flight_id = json.loads(response.text)['id']
        response = comm.put_with_json('/api/oms/flights/' + flight_id, {
            "id": str(flight_id),
            "flightNumber": "001",
            "startCity": "tj1",
            "endCity": "bj1",
            "startTime": "2020-01-02 00:00:00",
            "endTime": "2020-01-03 00:00:00"
        })
        assert 204 == response.status_code

        response = comm.get('/api/oms/flights/' + flight_id)
        assert 200 == response.status_code

        response = comm.delete('/api/oms/flights/' + flight_id)
        assert 204 == response.status_code

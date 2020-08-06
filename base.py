import json
import requests

from common import Common


def get_oms_access_token():
    comm = Common()
    username = 'zhaowende'
    response_login = comm.post('/api/oms/login', {'usernameOrEmail': username,
                                                  'password': '8d969eef6ecad3c29a3a629280e686cf0c3f5d5a86aff3ca12020c923adc6c92'})
    return json.loads(response_login.text)['access_token']


def get_portal_access_token():
    comm = Common()
    headers = {'Api-Version': 'v1',
               'Device-Platform': 'android',
               'App-Channel': 'alpha',
               'App-Type': 'customer',
               'App-Version': '1.0.0',
               'Device-Id': 'ABCDEFG',
               'Device-Model': 'RedMi Note 4X',
               'Device-Version': '7.1'}
    # TODO 是否有必要封装到Common中
    response_login = requests.post(comm.url_root + '/api/portal/login', headers=headers, data={'email': 'zhaowende',
                                                                                               'password': '8d969eef6ecad3c29a3a629280e686cf0c3f5d5a86aff3ca12020c923adc6c92'})
    return json.loads(response_login.text)['access_token']

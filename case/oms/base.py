import json

from common import Common


def get_access_token():
    comm = Common()
    username = 'zhaowende'
    response_login = comm.post('/api/oms/login', '', {'usernameOrEmail': username,
                                                      'password': '8d969eef6ecad3c29a3a629280e686cf0c3f5d5a86aff3ca12020c923adc6c92'})
    return json.loads(response_login.text)['access_token']

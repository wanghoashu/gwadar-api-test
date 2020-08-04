import requests
import yaml
import os

cur_path = os.path.dirname(os.path.realpath(__file__))
yaml_path = os.path.join(cur_path, "config.yaml")

f = open(yaml_path, 'r', encoding='utf-8')
cfg = f.read()
config_dict = yaml.load(cfg, Loader=yaml.FullLoader)


class Common(object):
    def __init__(self):
        self.url_root = config_dict.get('url')

    def get(self, uri, token='', params=''):
        url = self.url_root + uri + params
        headers = {'Api-Version': 'v1'}
        if len(token) > 0:
            headers['Authorization'] = 'Bearer ' + token

        res = requests.get(url, params=params, headers=headers)
        return res

    def post(self, uri, token='', params=None):
        url = self.url_root + uri
        headers = {'Api-Version': 'v1'}
        if len(token) > 0:
            headers['Authorization'] = 'Bearer ' + token
        if params is not None:
            res = requests.post(url, headers=headers, data=params)
        else:
            res = requests.post(url, headers=headers)
        return res

    def post_with_json(self, uri, token='', params=None):
        url = self.url_root + uri
        headers = {'Api-Version': 'v1'}
        if len(token) > 0:
            headers['Authorization'] = 'Bearer ' + token
        if params is not None:
            res = requests.post(url, headers=headers, json=params)
        else:
            res = requests.post(url, headers=headers)
        return res

    def put(self, uri, token='', params=None):
        url = self.url_root + uri
        headers = {'Api-Version': 'v1'}
        if len(token) > 0:
            headers['Authorization'] = 'Bearer ' + token
        if params is not None:
            res = requests.put(url, headers=headers, data=params)
        else:
            res = requests.put(url, headers=headers)
        return res

    def put_with_json(self, uri, token='', params=None):
        url = self.url_root + uri
        headers = {'Api-Version': 'v1'}
        if len(token) > 0:
            headers['Authorization'] = 'Bearer ' + token
        if params is not None:
            res = requests.put(url, headers=headers, json=params)
        else:
            res = requests.put(url, headers=headers)
        return res

    def delete(self, uri, token='', params=None):
        url = self.url_root + uri
        headers = {'Api-Version': 'v1'}
        if len(token) > 0:
            headers['Authorization'] = 'Bearer ' + token
        if params is not None:
            res = requests.delete(url, headers=headers, data=params)
        else:
            res = requests.delete(url, headers=headers)
        return res


if __name__ == '__main__':
    comm = Common()
    print('url:', comm.url_root)

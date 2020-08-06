import os

import requests
import yaml

cur_path = os.path.dirname(os.path.realpath(__file__))
yaml_path = os.path.join(cur_path, "config.yaml")

f = open(yaml_path, 'r', encoding='utf-8')
cfg = f.read()
config_dict = yaml.load(cfg, Loader=yaml.FullLoader)


class Common(object):
    def __init__(self, token=''):
        self.url_root = config_dict.get('url')
        self.token = token

    def get(self, uri, params=''):
        url = self.url_root + uri
        headers = {'Api-Version': 'v1'}
        if len(self.token) > 0:
            headers['Authorization'] = 'Bearer ' + self.token

        res = requests.get(url, params=params, headers=headers)
        return res

    def post(self, uri, params=None, files=None):
        url = self.url_root + uri
        headers = {'Api-Version': 'v1'}
        if len(self.token) > 0:
            headers['Authorization'] = 'Bearer ' + self.token
        if params is not None and files is not None:
            res = requests.post(url, headers=headers, data=params, files=files)
        elif params is not None and files is None:
            res = requests.post(url, headers=headers, data=params)
        elif params is None and files is not None:
            res = requests.post(url, headers=headers, files=files)
        else:
            res = requests.post(url, headers=headers)
        return res

    def post_with_json(self, uri, params=None):
        url = self.url_root + uri
        headers = {'Api-Version': 'v1'}
        if len(self.token) > 0:
            headers['Authorization'] = 'Bearer ' + self.token
        if params is not None:
            res = requests.post(url, headers=headers, json=params)
        else:
            res = requests.post(url, headers=headers)
        return res

    def put(self, uri, params=None, files=None):
        url = self.url_root + uri
        headers = {'Api-Version': 'v1'}
        if len(self.token) > 0:
            headers['Authorization'] = 'Bearer ' + self.token
        if params is not None and files is not None:
            res = requests.post(url, headers=headers, data=params, files=files)
        elif params is not None and files is None:
            res = requests.post(url, headers=headers, data=params)
        elif params is None and files is not None:
            res = requests.post(url, headers=headers, files=files)
        else:
            res = requests.post(url, headers=headers)
        return res

    def put_with_json(self, uri, params=None):
        url = self.url_root + uri
        headers = {'Api-Version': 'v1'}
        if len(self.token) > 0:
            headers['Authorization'] = 'Bearer ' + self.token
        if params is not None:
            res = requests.put(url, headers=headers, json=params)
        else:
            res = requests.put(url, headers=headers)
        return res

    def delete(self, uri, params=None):
        url = self.url_root + uri
        headers = {'Api-Version': 'v1'}
        if len(self.token) > 0:
            headers['Authorization'] = 'Bearer ' + self.token
        if params is not None:
            res = requests.delete(url, headers=headers, data=params)
        else:
            res = requests.delete(url, headers=headers)
        return res


if __name__ == '__main__':
    comm = Common()
    print('url:', comm.url_root)

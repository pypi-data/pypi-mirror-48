import json
import requests

from py_nsbcli.config import HTTP_HEADERS, ENC
from py_nsbcli.modules.admin import get_admin


class Client(object):
    def __init__(self, bind_admin):
        if isinstance(bind_admin, Client):
            self._admin = get_admin(bind_admin.admin)
            self.http_header = bind_admin.http_header
            return
        self._admin = get_admin(bind_admin)
        self.http_header = HTTP_HEADERS

    @property
    def admin(self):
        return self._admin

    @property
    def host(self):
        return self._admin.rpc_host

    def set_http_header(self, new_header):
        self.http_header = new_header

    def get(self, url, params=None):
        response = requests.get(
            url,
            headers=self.http_header,
            params=params
        )
        if response.status_code != 200:
            raise Exception(response)
        # for k, v in response.__dict__.items():
        #     print(k, v)
        return response.content

    def get_json(self, url, params=None):
        return json.loads(self.get(url, params), encoding=ENC)

    def abci_info(self):
        response = self.get_json(self._admin.abci_info_url)
        response['result']['response']['data'] = json.loads(response['result']['response']['data'])
        print(json.dumps(response, sort_keys=True, indent=4))

    def abci_query(self, path: str, data: str, height=0, prove=False):
        return self.get_json(self.admin.abci_query_url, params={
            'path': path,
            'data': data,
            'height': height,
            'prove': prove
        })

    def append_module(self, name: str, sub_module):
        setattr(self, name, sub_module)


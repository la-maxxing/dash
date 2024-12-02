from typing import Any, Optional
import requests
from urllib.parse import urljoin


class ApiHandler:
    def __init__(self, base_url: str, headers: dict={}):
        self.base_url = base_url
        self.headers = headers
        
    def _get(self, endpoint: str, params:Optional[dict]=None)->Any:
        response = requests.get(url=urljoin(self.base_url,endpoint), headers=self.headers,params=params)
        self._handle_response(response)
        return response.json()

    def _post(self, endpoint: str, data: Optional[dict] = None, params:Optional[dict]=None)->Any:
        response = requests.post(url=urljoin(self.base_url,endpoint), headers=self.headers, json=data, params=params)
        self._handle_response(response)
        return response.json()
    

    def _handle_response(self, response:requests.Response)->None:
        if not response.ok:
            raise Exception(f"API request failed with status {response.status_code}: {response.text}")

    def _test_connect(self)->str:
        return self._get(endpoint="")
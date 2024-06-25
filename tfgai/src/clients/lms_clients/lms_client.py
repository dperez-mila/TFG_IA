
import requests
from abc import ABC


class LMSClient(ABC):

    def __init__(self, base_url: str, token: str):
        self._base_url = base_url
        self._token = token
        self._headers = {
            'Authorization': 'Bearer ' + self._token,
            'Content-Type': 'application/json'
        }
    
    def _get(self, endpoint: str, params: dict = None) -> dict:
        url = f"{self._base_url}{endpoint}"
        response = requests.get(url, headers=self._headers, params=params)
        response.raise_for_status()
        return response.json()
    
    def _put(self, endpoint: str, data: dict = None):
        url = f"{self._base_url}{endpoint}"
        response = requests.put(url, headers=self._headers, json=data)
        response.raise_for_status()


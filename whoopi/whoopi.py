import requests
from typing import Optional

from whoopi.constants import APIENDPOINTS

class WhoopiLog:
  """whoopi API client"""
  def __init__(self, token: str) -> None:
    self._token = token #project key/token

  def logit(self, 
            ukey: str, 
            method: str, 
            endpoint: str, 
            status: str, 
            payload: Optional[str] = None, 
            resp_body: Optional[str] = None
            )-> None:
    data = {

    }
    reponse = requests.post(APIENDPOINTS.LOG, data=data)
    return
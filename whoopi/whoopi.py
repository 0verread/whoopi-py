import requests
from typing import Optional

from whoopi.constants import APIENDPOINTS

class Whoopi:
  """whoopi API client"""
  def __init__(self, ptoken: str) -> None:
    self._ptoken = ptoken #project key/token

  def logit(self, 
            ukey: str, 
            method: str, 
            endpoint: str, 
            status: str, 
            payload: Optional[str] = None, 
            resp_body: Optional[str] = None
            )-> None:
    
    data = {
      "ptoken": self._ptoken,
      "log_data": {
        "ukey": ukey,
        "method": method,
        "endpoint": endpoint,
        "status": status,
        "payload": payload,
        "resp_body": resp_body,
      }
    }

    response = requests.post(APIENDPOINTS.LOG, json=data)
    # TODO: @Jeet better error handling
    if response.status_code != 200:
      raise Exception
    return


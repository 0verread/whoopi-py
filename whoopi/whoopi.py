import requests
import datetime
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
    
    logged_at = datetime.datetime.now()
    data = {
      "ptoken": self._ptoken,
      "log_data": {
        "ukey": ukey,
        "method": method,
        "endpoint": endpoint,
        "status": status,
        "payload": payload,
        "resp_body": resp_body,
        "logged_at": logged_at
      }
    }

    response = requests.post(APIENDPOINTS.LOG, data=data)

    if response.status_code != 200:
      raise Exception
    return
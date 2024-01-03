import requests
import datetime
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
    
    log_time = datetime.datetime.now()
    data = {
      "ukey": ukey,
      "method": method,
      "endpoint": endpoint,
      "status": status,
      "payload": payload,
      "resp_body": resp_body,
      "date": log_time 
    }
    response = requests.post(APIENDPOINTS.LOG, data=data)

    if response.status_code != 200:
      raise Exception
    return
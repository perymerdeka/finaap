import json

from httpx import Client
from typing import Any, Optional

class FloatratesSpider(object):
   def __init__(self, url: str) -> None:
        self.url: str =  url
        self.client: Client = Client()

   def parse(self, key: Optional[str]=None):
        response = self.client.get(self.url)
        
        # proses data
        json_data = response.json()
        if key != None:
            datas: dict[str, Any] = json_data[key]
            return datas
        else:
            results = [{keys: val} for keys, val in json_data.items()]
            with open('results.json', 'w') as outfile:
                json.dump(results, outfile)
            return json_data
        
    
        


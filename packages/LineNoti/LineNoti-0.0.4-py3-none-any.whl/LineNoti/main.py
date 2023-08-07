import requests
from requests.packages.urllib3.util.retry import Retry
from requests.adapters import HTTPAdapter

"""
LINE Notify API

Copyright © LINE Corporation
"""

API_URL = 'https://notify-api.line.me/api/notify'

class Notifier:
    def __init__(self, token):
        self.token = token
        self.tokens = {self.token:0} # token list which used
        # self.api_url = 'https://notify-api.line.me/api/notify'
        self.retries = Retry(total=3,
                             backoff_factor=1,
                             status_forcelist=[500, 502, 503, 504])

    def notify(self, msg, img_path=None, limit=False):
        if limit and self.tokens[self.token] > 100:
            print('Limit count: change the token by change_token()')
            return False, self.tokens[self.token]

        session = requests.Session()
        session.mount('https://', HTTPAdapter(max_retries=self.retries))
        headers={'Authorization': 'Bearer ' + self.token}
		
        if img_path == None:
            response = session.post(url=API_URL,
                                    data={'message': msg}, #1000 characters max
                                    headers=headers,
                                    timeout=3)
        else:
            try:
                with open(img_path, 'rb') as fd:
                    response = session.post(url=API_URL, 
                                            data={'message': msg},
                                            headers=headers,
                                            files={'imageFile': fd},
                                            timeout=3)
            except:
                print("Error: Sending Image File is Failed")
				
                response = session.post(url=API_URL,
                                        data={'message': 'Image Failed, '+msg},
                                        headers=headers,
                                        timeout=3)
        
        """
            Response Headers status
            
            200: Success
            400: Bad request
            401: Invalid access token
            500: Failure due to server error
        """
        if response.status_code!=200:
            print('LINE Notify Request Failed')
            return response
        
        self.tokens[self.token] += 1
        
        return self.tokens[self.token]
        
    
    def change_token(self, token):
        if self.tokens.get(token)==None:
            self.token = token
            self.tokens[self.token] = 0
        else:
            print('Warning: '+token+' is already used '+str(self.tokens[token]))
            self.token = token

        return True
import logging
import json
import requests

class APIService:
    def _call_request_post(self, url, jsonBody, user_token):
        headers = {
            "Cookie": f"user-token={user_token}",
            "Content-Type": "application/json"
        }
        r = requests.post(url, headers=headers, json=jsonBody)
        if r.status_code == 200:
            logging.info(f"Succeeded calling {url}")
        else:
            logging.error(f"FAILED calling {url}")
        logging.info(f"POST response: {r.content}. Body: {jsonBody}")
    
    def _call_request_put(self, url, jsonBody, user_token):
        headers = {
            "cookie": f"user-token={user_token}",
            "accept": "application/json"
        }
        r = requests.put(url, headers=headers, json=jsonBody)
        if r.status_code == 200:
            logging.info(f"Succeeded calling {url}")
        else:
            logging.error(f"FAILED calling {url}")
        logging.info(f"PUT response: {r.content}. Body: {jsonBody}")
    
    def _call_request_delete(self, url, params, user_token):
        headers = {
            "cookie": f"user-token={user_token}",
            "accept": "application/json"
        }
        r = requests.delete(url, headers=headers, params=params)
        # print('response', r)
        if r.status_code == 200:
            logging.info(f"Succeeded calling {url}")
        else:
            logging.error(f"FAILED calling {url}")
        logging.info(f"DELETE response: {r.content}. Params: {params}")

    def _call_request_get(self, url, params, user_token):
        headers = {
            "cookie": f"user-token={user_token}",
            "accept": "application/json"
        }
        r = requests.get(url, headers=headers, params=params)
        # print(r)
        if r.status_code == 200:
            logging.info(f"Succeeded calling {url}")
        else:
            logging.error(f"FAILED calling {url}")
        logging.info(f"GET response: {r.content}. Params: {params}")
        return json.loads(r.content.decode())
import logging
import json
import requests

class APIService:

    def _call_api_delete_s3_bucket(self):
        pass

    def _call_api_delete_ec2_instance(self):
        pass

    def _call_request_delete(self, url, params, user_token):
        headers = {
            "cookie": f"user-token={user_token}",
            "accept": "application/json"
        }
        r = requests.delete(url, headers=headers, params=params)
        if r.status_code == 200:
            logging.info(f"Succeeded calling {url}")
        else:
            logging.error(f"FAILED calling {url}")
        logging.info(f"Delete response: {r.content}. Params: {params}")

    def _call_request_get(self, url, params, user_token):
        headers = {
            "cookie": f"user-token={user_token}",
            "accept": "application/json"
        }
        r = requests.get(url, headers=headers, params=params)
        if r.status_code == 200:
            logging.info(f"Succeeded calling {url}")
        else:
            logging.error(f"FAILED calling {url}")
        logging.info(f"GET response: {r.content}. Params: {params}")
        return json.loads(r.content.decode())
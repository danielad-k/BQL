import json
import pandas as pd
import requests
from requests.auth import HTTPBasicAuth


class BqlAPI:
    def __init__(self, payload, account_id, username, password):
        self.payload = payload
        self.account_id = account_id
        self.username = username
        self.password = password

    def authentication(username, password):
        return HTTPBasicAuth(username, password)

    def bql_api(payload, account_id, username, password):
        headers = {
            'Content-Type': "text/plain",
            'cache-control': "no-cache",
        }

        req = requests.request("POST", url='https://api.brightedge.com/3.0/query/%s' % account_id,
                               data=payload, headers=headers, auth=BqlAPI.authentication(username, password))

        try :

            assert req.status_code == 200
            return req

        except:
            # print(req.text)
            wrong_output = json.loads(req.text)
            # print(req.status_code)
            # print(wrong_output['error']['errormsg'])
            print("Error {}: {}.".format(req.status_code, wrong_output['error']['errormsg']))

    def bql_output(payload, account_id, username, password):
        output = BqlAPI.bql_api(payload, account_id, username, password)

        try:

            json_output = json.loads(output.text)
            return pd.DataFrame(json_output['values'])

        except:
            return output

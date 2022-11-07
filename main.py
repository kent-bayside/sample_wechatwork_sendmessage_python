"""Example code with Wechat Work API
This is an example python code to send a message to a 'Wechat Work' (企业微信).
"""

import os
import sys
import json
import requests
from dotenv import load_dotenv

load_dotenv()


def GetAccessToken():
    """
    Connect to the We Chat Work API and get an access token.
    """
    CORP_ID = os.environ['CORP_ID']
    CORP_SECRET = os.environ['CORP_SECRET']

    url = f'https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={CORP_ID}&corpsecret={CORP_SECRET}'
    res = requests.post(url)
    res_json = json.loads(res.text)
    token = res_json.get('access_token')

    return token


token = GetAccessToken()
if token is None:
    print('ERROR! Unable to get token, please check your corp ID or corp secret.')
    sys.exit()

agentid, touser, msgtype = '999999', 'test_user', 'text'
json_data = {
    "agentid": agentid,
    "touser": touser,
    "msgtype": msgtype,
    "text": {
       "content": "Test!\n<a href=\"http://example.com\">example.com</a>",
            },
}

url = f'https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token={token}'
res = requests.post(url, data=json.dumps(json_data))
if res.status_code != 200:
    print(f'ERROR! Status code: {res.status_code}')
    sys.exit()

print(res.text)

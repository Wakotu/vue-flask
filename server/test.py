'''
Author: Axiuxiu
Date: 2022-02-27 17:06:03
LastEditTime: 2022-02-27 19:35:43
Description: 
'''
from datetime import datetime, timedelta
import jwt
from config import SECRET_KEY

now=datetime.utcnow()

jwt_token=jwt.encode(
    {
        'name':'Jack',
        'age':18,
        'exp':now-timedelta(seconds=1),
    },
    SECRET_KEY,
    algorithm='HS256',
)

print(jwt_token)

payload=jwt.decode(
    jwt=jwt_token,
    key=SECRET_KEY,
    algorithms=['HS256']
)

print(payload)
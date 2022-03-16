'''
Author: Axiuxiu
Date: 2022-02-27 16:26:41
LastEditTime: 2022-03-16 12:36:16
Description: 装饰器
'''


from functools import wraps
from flask import request
import jwt
from config import SECRET_KEY, HASH_ALGORITHM
from exts import db
from models import User


def login_required(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        userToken=request.headers.get('Authorization')
        if not userToken:
            return '您尚未登陆',401
        
        try:
            # 解密token
            payload=jwt.decode(jwt=userToken, key=SECRET_KEY, algorithms=[HASH_ALGORITHM,])
            # print(payload)
        except Exception as e:
            print(e)
            return 'token已过期',401
        else:
            user_id=payload.get('id')
            user=db.session.query(User).filter(User.id==user_id).first()
            if not user:
                return '无效的token', 401
            return func(user, *args, **kwargs)
    return wrapper

'''
Author: Axiuxiu
Date: 2022-02-26 17:30:19
LastEditTime: 2022-03-16 11:15:49
Description: 定义数据库模型
'''

from datetime import datetime
import enum
from sqlalchemy import Column, DateTime, String, Enum
from werkzeug.security import generate_password_hash, check_password_hash
from uuid import uuid4
from exts import db

def gen_id():
    return uuid4().hex

class Gender(enum.Enum):
    male=1
    female=0

class Identity(enum.Enum):
    admin=1
    user=0


class User(db.Model):
    '''用户表'''
    __tablename__='users'

    id=Column(String(32), default=gen_id, primary_key=True)
    # 邮箱
    email=Column(String(20), unique=True)
    # 手机号码
    phone=Column(String(20), unique=True)
    # 所属单位
    unit=Column(String(50))
    # 居住地址
    address=Column(String(50))
    # 个人介绍
    intro=Column(String(500))
    # 用户名
    username=Column(String(20), nullable=False)
    # 密码（加密）
    hash_pwd=Column(String(256), nullable=False)
    # 创建时间
    create_time=Column(DateTime, default=datetime.now)
    # 上次登录时间
    last_login=Column(DateTime)
    # 头像url
    avatar_url=Column(String(256),default='/static/user.png')
    # 性别
    gender=Column(Enum(Gender), default=Gender.male, nullable=False)
    # 身份
    identity=Column(Enum(Identity), default=Identity.user, nullable=False)

    def __repr__(self) -> str:
        return 'User '+self.username

    @property
    def pwd(self):
        raise AttributeError('禁止读取密码')
    
    @pwd.setter
    def pwd(self,plain_pwd):
        self.hash_pwd=generate_password_hash(plain_pwd)
    
    # 检查密码
    def check_pwd_hash(self,pwd):
        return check_password_hash(self.hash_pwd, pwd)
'''
Author: Axiuxiu
Date: 2022-02-27 11:33:22
LastEditTime: 2022-02-28 14:36:49
Description: 用户视图
'''

from datetime import datetime, timedelta
from flask import Blueprint, jsonify, request
from decorators import login_required
from models import User
from exts import db
import jwt
from config import SECRET_KEY, HASH_ALGORITHM, JWT_EXPIRY


bp = Blueprint('users', __name__, url_prefix='/api/users')


@bp.route('/test', methods=['GET', 'POST'])
@login_required
def test(user):
    if request.method == 'POST':
        param = request.get_json()
        return jsonify({
            'code': 200,
            'info': '成功接收参数',
            'param': param,
        })
    else:
        return jsonify({
            'code': 200,
            'info': '请求成功',
        })


@bp.route('/register', methods=['POST'])
def register():
    form = request.get_json()
    email = form.get('email')
    # 判断是否重复
    user = db.session.query(User).filter(User.email == email).first()
    if user:
        return jsonify({
            'code': 404,
            'info': '用户已存在',
        })
    # 直接注册不验证
    db.session.add(User(**form))
    db.session.commit()
    return jsonify({
        'code': 200,
        'info': '注册成功',
    })


@bp.route('/login', methods=['POST'])
def login():
    form = request.get_json()
    email = form.get('email')
    pwd = form.get('pwd')

    if not email or not pwd:
        return jsonify({
            'code': 404,
            'info': '缺少必填字段',
        })

    user = db.session.query(User).filter(User.email == email).first()
    if user:
        if user.check_pwd_hash(pwd):
            # 生成jwt-token
            now=datetime.utcnow()
            userToken=jwt.encode(
                {
                    'id':user.id,
                    'username':user.username,
                    'email':user.email,
                    'iat':now,
                    'exp':now+timedelta(minutes=JWT_EXPIRY),
                },
                key=SECRET_KEY,
                algorithm=HASH_ALGORITHM,
            )
            # print(userToken)

            return jsonify({
                'code': 200,
                'userToken': userToken,
            })
        else:
            return jsonify({
                'code': 404,
                'info': '密码不正确',
            })
    else:
        return jsonify({
            'code': 404,
            'info': '用户不存在',
        })

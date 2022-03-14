'''
Author: Axiuxiu
Date: 2022-02-27 11:33:22
LastEditTime: 2022-03-14 18:13:36
Description: 用户视图
Todo: 添加用户更信息接口
'''

from datetime import datetime, timedelta
import os
from flask import Blueprint, jsonify, request
from decorators import login_required
from models import User
from exts import db
import jwt
from werkzeug.utils import secure_filename
from config import SECRET_KEY, HASH_ALGORITHM, JWT_EXPIRY, AVATAR_FOLDER


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

# 注册
@bp.route('/register', methods=['POST'])
def register():
    form = request.get_json()
    email = form.get('email')
    phone=form.get('phone')
    # 判断是否重复
    user = db.session.query(User).filter(User.email == email).first()
    if user:
        return '邮箱已存在',404
    user=db.session.query(User).filter(User.phone==phone).first()
    if user:
        return '手机号已存在',404
    # 直接注册不验证
    db.session.add(User(**form))
    db.session.commit()
    return jsonify({
        'code': 200,
        'info': '注册成功',
    })

# 登录
@bp.route('/login', methods=['POST'])
def login():
    form = request.get_json()
    email = form.get('email')
    pwd = form.get('pwd')

    if not email or not pwd:
        return '缺少必填字段',404

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
                    'isAdmin':user.identity.value,
                    'avatar_url':user.avatar_url,
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
            return '密码不正确',404
    else:
        return '用户不存在',404

"""
    更新基础数据
    接收到的参数：
        username
        unit
        address
        intro
"""
@bp.route('/updateBasic',methods=['POST'])
@login_required
def update_basic(user):
    # 获取信息
    form=request.get_json()
    try:
        db.session.query(User).filter(User.id==user.id).update(form)
        db.session.commit()
    except Exception:
        return '数据库更新错误',404
        
    return jsonify({
        'code':200,
        'info':'更新成功',
    })

# 更新邮箱
@bp.route('/updateEmail',methods=['POST'])
@login_required
def update_email(user):
    form=request.get_json()
    email=form.get('email')
    if not email:
        return '缺少必填字段', 404
    # 验证是否重复
    res=db.session.query(User).filter(User.email==email).first()
    if res:
        return '邮箱已存在',404
    
    # 进行修改
    try:
        db.session.query(User).filter(User.id==user.id).update({
            'email':email,
        })
        db.session.commit()
    except Exception:
        return '邮箱更新失败',404
    
    return jsonify({
        'code':200,
        'info':'更新成功'
    })

# 更新手机号码
@bp.route('/updatePhone',methods=['POST'])
@login_required
def update_phone(user):
    form=request.get_json()
    phone=form.get('phone')
    if not phone:
        return '缺少必填字段',404
    # 验证是否重复
    res=db.session.query(User).filter(User.phone==phone).first()
    if res:
        return '手机号已存在',404
    
    # 进行修改
    try:
        db.session.query(User).filter(User.id==user.id).update({
            'phone':phone,
        })
        db.session.commit()
    except Exception:
        return '手机号更新失败',404
    
    return jsonify({
        'code':200,
        'info':'更新成功'
    })

# 更新密码
@bp.route('/updatePwd',methods=['POST'])
@login_required
def update_pwd(user):
    pwd=request.get_json().get('pwd')
    if not pwd:
        return '缺少必填字段',404
    
    # 更新
    try:
        db.session.query(User).filter(User.id==user.id).update({
            'pwd':pwd,
        })
        db.session.commit()
    except Exception:
        return '密码更新失败',404
    
    return jsonify({
        'code':200,
        'info':'更新成功',
    })

# 头像上传
@bp.route('/uploadAvatar',methods=['POST'])
@login_required
def upload_avatar(user):
    print(request.files)
    f=request.files.get('file')
    if not f:
        return '缺少必填字段', 404
    
    # 文件保存
    file_path=os.path.join(AVATAR_FOLDER, secure_filename(f.filename))
    avatar_url='/'+file_path
    # print(file_path)
    try:
        f.save(file_path)
    except Exception:
        return '文件保存失败',500
    
    # 更新数据库
    try:
        db.session.query(User).filter(User.id==user.id).update({
            'avatar_url':avatar_url,
        })
        db.session.commit()
    except Exception:
        return '数据库更新失败', 500
    return jsonify({
        'code':200,
        'info':'上传成功',
        'image_url':avatar_url,
    })

    
'''
Author: Axiuxiu
Date: 2022-02-27 11:33:22
LastEditTime: 2022-03-20 15:54:01
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
from werkzeug.security import generate_password_hash


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
        return '邮箱已存在', 404
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
        return '缺少必填字段', 404

    user = db.session.query(User).filter(User.email == email).first()
    if user:
        if user.check_pwd_hash(pwd):
            # 生成jwt-token
            now = datetime.utcnow()

            userToken = jwt.encode(
                {
                    'id': user.id,
                    'iat': now,
                    'exp': now+timedelta(minutes=JWT_EXPIRY),
                },
                key=SECRET_KEY,
                algorithm=HASH_ALGORITHM,
            )
            # print(userToken)

            # 更新登录时间
            db.session.query(User).filter(User.id == user.id).update({
                'last_login': datetime.now()
            })
            db.session.commit()

            return jsonify({
                'code': 200,
                'userToken': userToken,
                'avatar_url': user.avatar_url,
                'username': user.username,
                'isAdmin': user.identity.value,
            })
        else:
            return '密码不正确', 404
    else:
        return '用户不存在', 404


"""
    更新基础数据
    接收到的参数：
        username
        unit
        address
        intro
"""


@bp.route('/updateBasic', methods=['POST'])
@login_required
def update_basic(user):
    # 获取信息
    form = request.get_json()
    try:
        db.session.query(User).filter(User.id == user.id).update(form)
        db.session.commit()
    except Exception:
        return '数据库更新错误', 404

    return jsonify({
        'code': 200,
        'info': '更新成功',
    })


@bp.route('/updateEmail', methods=['POST'])
@login_required
def update_email(user):
    form = request.get_json()
    email = form.get('email')
    if not email:
        return '缺少必填字段', 404
    # 验证是否重复
    res = db.session.query(User).filter(User.email == email).first()
    if res:
        return '邮箱已存在', 404

    # 进行修改
    try:
        db.session.query(User).filter(User.id == user.id).update({
            'email': email,
        })
        db.session.commit()
    except Exception:
        return '邮箱更新失败', 404

    return jsonify({
        'code': 200,
        'info': '更新成功'
    })


@bp.route('/updatePhone', methods=['POST'])
@login_required
def update_phone(user):
    form = request.get_json()
    phone = form.get('phone')
    if not phone:
        return '缺少必填字段', 404
    # 验证是否重复
    res = db.session.query(User).filter(User.phone == phone).first()
    if res:
        return '手机号已存在', 404

    # 进行修改
    try:
        db.session.query(User).filter(User.id == user.id).update({
            'phone': phone,
        })
        db.session.commit()
    except Exception:
        return '手机号更新失败', 404

    return jsonify({
        'code': 200,
        'info': '更新成功'
    })


@bp.route('/updatePwd', methods=['POST'])
@login_required
def update_pwd(user):
    form = request.get_json()
    pwd = form.get('pwd')
    pwd_token = form.get('pwdToken')
    if not pwd:
        return '缺少必填字段', 404

    if not pwd_token:
        return '未验证原密码', 404

    # 判断pwdToken合法性
    try:
        jwt.decode(jwt=pwd_token, algorithms=[
                   HASH_ALGORITHM, ], key=SECRET_KEY)
    except Exception as e:
        print(e)
        return 'token已失效', 401

    # 更新
    try:
        db.session.query(User).filter(User.id == user.id).update({
            'hash_pwd': generate_password_hash(pwd),
        })
        db.session.commit()
    except Exception as e:
        print(e)
        return '密码更新失败', 404

    return jsonify({
        'code': 200,
        'info': '更新成功',
    })


@bp.route('/uploadAvatar', methods=['POST'])
@login_required
def upload_avatar(user):
    print(request.files)
    f = request.files.get('file')
    if not f:
        return '缺少必填字段', 404

    # 文件保存
    file_path = os.path.join(AVATAR_FOLDER, secure_filename(f.filename))
    avatar_url = '/'+file_path
    # print(file_path)
    try:
        f.save(file_path)
    except Exception:
        return '文件保存失败', 500

    # 更新数据库
    try:
        db.session.query(User).filter(User.id == user.id).update({
            'avatar_url': avatar_url,
        })
        db.session.commit()
    except Exception:
        return '数据库更新失败', 500
    return jsonify({
        'code': 200,
        'info': '上传成功',
        'image_url': avatar_url,
    })


# 获取用户个人信息
@bp.route('/getUserInfo', methods=['POST'])
@login_required
def get_userinfo(user):
    # 查询
    # print(type(user.create_time))
    return jsonify({
        'code': 200,
        'userInfo': {
            'create_time': user.create_time.strftime(r'%Y-%m-%d'),
            'isMale': user.gender.value,
            'unit': user.unit,
            'address': user.address,
            'intro': user.intro,
            'email': user.email,
            'phone': user.phone,
            'last_login': user.last_login.strftime('%Y-%m-%d %H:%M:%S'),
        }
    })


@bp.route('/validatePwd', methods=['POST'])
@login_required
def validate_pwd(user):
    form = request.get_json()
    pwd = form.get('pwd')
    if not pwd:
        return '缺少必填字段', 404

    if user.check_pwd_hash(pwd):
        # 返回token
        now = datetime.utcnow()
        pwd_token = jwt.encode(
            {
                # 'pwd': pwd,
                'iat': now,
                'exp': now+timedelta(minutes=3),
            },
            key=SECRET_KEY,
            algorithm=HASH_ALGORITHM
        )

        return jsonify({
            'code': 200,
            'pwd_token': pwd_token,
        })
    else:
        return '密码错误', 404


@bp.route('/getAllUsers', methods=['POST'])
@login_required
def get_all_users(user):
    # 判断用户身份
    if not user.identity.value:
        return '您的权限不足', 402

    users = db.session.query(User.id, User.email, User.username, User.phone, User.gender, User.identity, User.unit, User.address).all()
    user_list=[]
    for user in users:
        user_item={
            'id':user.id,
            'email':user.email,
            'username':user.username,
            'phone':user.phone,
            'gender':'男' if user.gender.value else '女',
            'identity':'管理员' if user.identity.value else '普通用户',
            'unit':user.unit,
            'address':user.address,
        }
        user_list.append(user_item)
    return jsonify({
        'code':200,
        'users':user_list,
    })

@bp.route('/addUser',methods=['POST'])
@login_required
def add_user(user):
    form=request.get_json().get('form')
    # 判断邮箱和手机重复性
    email=form.get('email')
    phone=form.get('phone')

    res=db.session.query(User).filter(User.email==email).first()
    if res:
        return '邮箱已存在', 404
    
    res=db.session.query(User).filter(User.phone==phone).first()
    if res:
        return '手机号已存在', 404
    
    try:
        new_user=User(**form)
        db.session.add(new_user)
        db.session.commit()
    except Exception as e:
        print(e)
        return '数据库更新失败', 404

    return jsonify({
        'code':200,
        'info':'添加成功',
    })

@bp.route('/editUser',methods=['POST'])
@login_required
def edit_user(user):
    if not user.identity.value:
        return '您的权限不足', 402
    params=request.get_json()
    form=params.get('form')
    user_id=params.get('user_id')
    
    pwd=form.get('pwd')
    if pwd:
        if pwd!='':
            form['hash_pwd']=generate_password_hash(pwd)
        del form['pwd']

    try:
        db.session.query(User).filter(User.id==user_id).update(form)
        db.session.commit()
    except Exception as e:
        print(e)
        return '用户不存在', 404
    
    return jsonify({
        'code':200,
        'info':'更新成功',
    })

@bp.route('/removeUser',methods=['POST'])
@login_required
def remove_user(user):
    form=request.get_json()
    user_id=form.get('user_id')
    
    if not user_id:
        return '缺少必填字段', 404
    
    try:
        db.session.query(User).filter(User.id==user_id).delete()
        db.session.commit()
    except Exception as e:
        print(e)
        return '用户不存在', 404

    return jsonify({
        'code':200,
        'info':'删除成功',
    })
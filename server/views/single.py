'''
Author: Axiuxiu
Date: 2022-03-23 14:31:30
LastEditTime: 2022-03-23 19:34:24
Description: 单体检测视图
Todo: 
'''

from flask import Blueprint, jsonify, request
from exts import db
from models import SingleTask
from decorators import login_required

bp=Blueprint('single',__name__, url_prefix='/api/single')

# 添加单体检测任务
@bp.route('/addSingleTask',methods=['POST'])
@login_required
def add_single_task(user):
    form=request.get_json()
    
    try:
        new_task=SingleTask(**form)
        db.session.add(new_task)
        db.session.commit()
    except Exception as e:
        print(e)
        return '数据库更新失败', 404

    return jsonify({
        'code':200,
        'info':'任务创建成功，请前往检测结果页面进行查看',
    })

@bp.route('/getAllTask',methods=['POST'])
@login_required
def get_all_task(user):
    try:
        res=db.session.query(SingleTask).all()
    except Exception as e:
        print(e)
        return '数据库查询失败', 404
    task_list=[]
    for task in res:
        task_item={
            'id':task.id,
            'name':task.name,
            'status':task.status.value,
        }
        task_list.append(task_item)
    
    return jsonify({
        'code':200,
        'task_list':task_list,
    })
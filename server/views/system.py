'''
Author: Axiuxiu
Date: 2022-03-21 10:35:47
LastEditTime: 2022-03-21 14:01:28
Description: 系统管理路由
Todo: 
'''

from flask import Blueprint, jsonify, request
from decorators import login_required
from exts import db
from models import Task, TaskStatus, Section, Status

bp = Blueprint('system', __name__, url_prefix='/api/system')


@bp.route('/getAllTask', methods=['POST'])
@login_required
def get_all_task(user):
    try:
        tasks = db.session.query(Task).all()
    except Exception as e:
        print(e)
        return '数据库查询失败', 404
    task_list = []
    for task in tasks:
        task_item = {
            'id': task.id,
            'create_time': task.create_time.strftime(r'%Y-%m-%d %H:%M:%S'),
            'name': task.name,
            'keyword': task.keyword,
            'end_time':task.end_time.strftime(r'%Y-%m-%d %H:%M:%S'),
        }
        task_list.append(task_item)

    return jsonify({
        'code': 200,
        'tasks': task_list,
    })


@bp.route('/addTask', methods=['POST'])
@login_required
def add_task(user):
    form = request.get_json()

    # 判断是否重复
    name = form.get('name')
    res = db.session.query(Task).filter(Task.name == name).first()
    if res:
        return '任务名称已存在', 404

    try:
        task = Task(**form)
        task.statuses=[ 
            TaskStatus(section=Section.spider, status=Status.run),
            TaskStatus(section=Section.analysis, status=Status.run),
        ]
        db.session.add(task)
        db.session.commit()
    except Exception as e:
        print(e)
        return '数据库更新失败', 404
    
    return jsonify({
        'code':200,
        'info':'添加成功',
    })

@bp.route('/removeTask',methods=['POST'])
@login_required
def remove_task(user):
    form=request.get_json()
    id=form.get('id')
    if not id:
        return '缺少必填字段',404
    
    try:
        task=db.session.query(Task).filter(Task.id==id).first()
        # 先删除状态
        for status in task.statuses:
            db.session.query(TaskStatus).filter(TaskStatus.id==status.id).delete()
            db.session.commit()
        db.session.query(Task).filter(Task.id==id).delete()
        db.session.commit()
    except Exception as e:
        print(e)
        return '数据库更新失败', 404
    
    return jsonify({
        'code':200,
        'info':'删除成功',
    })
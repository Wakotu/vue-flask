'''
Author: Axiuxiu
Date: 2022-03-21 10:35:47
LastEditTime: 2022-03-22 10:34:54
Description: 系统管理路由
Todo: 
'''

from flask import Blueprint, jsonify, request
from decorators import login_required
from exts import db
from models import Task, TaskStatus, Section, Status

bp = Blueprint('system', __name__, url_prefix='/api/system')


# 任务管理部分
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

# 爬虫监测部分
@bp.route('/getAllStatus',methods=['POST'])
@login_required
def get_spider_status(user):
    status_list=[]
    section=request.get_json().get('section')
    
    if section=='spider':
        try:
            spider_statuses=db.session.query(TaskStatus).filter(TaskStatus.section==Section.spider).all()
        except Exception as e:
            print(e)
            return '数据库查询失败',404
        for status in spider_statuses:
            status_item={
                'id':status.id,
                'keyword':status.task.keyword,
                'name':status.task.name,
                'interval':status.task.interval,
                'end_time':status.task.end_time.strftime(r'%Y-%m-%d %H:%M:%S'),
                'status': status.status.value,
            }
            status_list.append(status_item)
    elif section=='analysis':
        try:
            analysis_statuses=db.session.query(TaskStatus).filter(TaskStatus.section==Section.analysis).all()
        except Exception as e:
            print(e)
            return '数据库查询失败'
        for status in analysis_statuses:
            status_item={
                'id':status.id,
                'name':status.task.name,
                'create_time':status.task.create_time.strftime(r'%Y-%m-%d %H:%M:%S'),
                'status':status.status.value,
            }
            status_list.append(status_item)
    
    return jsonify({
        'code':200,
        'status_list':status_list,
    })


@bp.route('/editStatus',methods=['POST'])
@login_required
def edit_status(user):
    form=request.get_json()
    section=form.pop('section')
    if not section:
        return '缺少必填字段',404
    id=form.pop('id')
    if not id:
        return '缺少必填字段', 404

    if section=='spider':
        status=form.pop('status')
        if not status:
            return '缺少必填字段', 404
        try:
            # 更新状态
            task_status = db.session.query(TaskStatus).filter(TaskStatus.id==id)
            task_status.update({
                'status':status,
            })
            # 找到对应任务，更新其他
            task_id=task_status.first().task.id
            db.session.query(Task).filter(Task.id==task_id).update(form)
            db.session.commit()
        except Exception as e:
            print(e)
            return '数据库更新失败',404
    elif section=='analysis':
        # 直接更新状态
        try:
            db.session.query(TaskStatus).filter(TaskStatus.id==id).update(form)
            db.session.commit()
        except Exception as e:
            print(e)
            return '数据库更新失败',404

    return jsonify({
        'code':200,
        'info':'更新成功',
    })

@bp.route('/removeStatus',methods=['POST'])
@login_required
def remove_spider_status(user):
    form=request.get_json()
    id=form.get('id')
    
    try:
        db.session.query(TaskStatus).filter(TaskStatus.id==id).delete()
        db.session.commit()
    except Exception as e:
        print(e)
        return '数据库更新失败', 404
    
    return jsonify({
        'code':200,
        'info':'删除成功'
    })
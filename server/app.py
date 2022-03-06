'''
Author: Axiuxiu
Date: 2022-02-26 17:06:37
LastEditTime: 2022-02-27 13:43:06
Description: 主文件
'''

from flask import Flask
from flask_migrate import Migrate
from exts import db
from views.users import bp as users_bp
import config

app = Flask(__name__)

app.config.from_object(config)

# 配置数据库
db.init_app(app)
migrate=Migrate(app,db)


app.register_blueprint(users_bp)


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000, debug=True)

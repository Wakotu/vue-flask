'''
Author: Axiuxiu
Date: 2022-02-26 17:14:20
LastEditTime: 2022-03-14 15:28:38
Description: 配置文件
'''
# 主项目配置
JSON_AS_ASCII=False

# JWT设置
SECRET_KEY='ciscn-1701'
HASH_ALGORITHM='HS256'
JWT_EXPIRY=60

# 数据库配置
DB_SERVER='localhost'
DB_PORT=3306
DB_USERNAME='root'
DB_PASSWORD='admin'
DB_NAME='ciscn_db'
SQLALCHEMY_DATABASE_URI='mysql+pymysql://{0}:{1}@{2}:{3}/{4}?charset=utf8'.format(
    DB_USERNAME,DB_PASSWORD,DB_SERVER, DB_PORT,DB_NAME)
SQLALCHEMY_TRACK_MODIFICATIONS=False

# 上传文件设置, 注意前面不能加'/'
AVATAR_FOLDER='static/avatars/'
# saltedfish（咸鱼）
  这是一个基于[Flask](http://flask.pocoo.org)框架及其插件[Flask-RESTful](http://flask-restful.readthedocs.io/en/latest/)实现的资源整合服务，以研究学习为主。

## RESTful的接口设计风格
  为了便于资源的有效管理，采用RESTful的设计风格。

## 环境安装
  - [Python2.y](https://www.python.org/)环境安装
  <p><code></code></p>
  - [Flask](http://flask.pocoo.org)安装，用于Web应用搭建
  <p><code>pip install flask</code></p>
  - [Flask-RESTful](http://flask-restful.readthedocs.io/en/latest/)安装，用于RESTful架构
  <p><code>pip install flask-restful</code></p>
  - [Flask-Script](http://flask-script.readthedocs.io/en/latest/)安装，用于服务管理
  <p><code>pip install flask-script</code></p>
  - [peewee](http://docs.peewee-orm.com/en/stable/)安装，数据库ORM
  <p<code>pip install peewee</code></p>

## 数据安装
  <p><code></code></p>

## 服务管理
### 服务启动
  <p><code>python manager.py server</code></p>
### 服务停止
  <p><code>CTRL+C</code></p>

## 资源列表
### 用户资源(users)
  - 获取所有用户列表(get)
  <p><code>http://127.0.0.1:5000/api/v1/users</code></p>
  - 查询用户(get)
  <p><code>http://127.0.0.1:5000/api/v1/users/<string:username></code></p>
  - 更新用户(put)
  <p><code>http://127.0.0.1:5000/api/v1/users/<string:username></code></p>
  - 新增用户(post)
  <p><code>http://127.0.0.1:5000/api/v1/users/<string:username></code></p>
  - 删除用户(delete)
  <p><code>http://127.0.0.1:5000/api/v1/users/<string:username></code></p>
### 文件(files)
###  

#-*- coding=utf-8 -*-

import sys
import datetime
from flask import jsonify
sys.path.append('..')
from flask_restful import Resource, reqparse, fields, marshal_with, marshal
from models.sfmodels import User
from playhouse.shortcuts import model_to_dict
from utils import TransException
from utils import make_result, custom_abort
from codes import Code
from peewee import IntegrityError

#解析
parser = reqparse.RequestParser()
parser.add_argument( 'username', type=str )
parser.add_argument( 'password', type=str )
parser.add_argument( 'realname', type=str )
parser.add_argument( 'role', type=str )
parser.add_argument( 'logdate', type=str )

#对返回结果进行过滤
resource_fields = {
    'username':fields.String,
    'realname':fields.String,
    'role':fields.String,
    'regdate':fields.DateTime,
    'logdate':fields.DateTime,
}

#用户注册
class UserResource( Resource ):
    def post( self ):
        #用户新增
        args = parser.parse_args()
        username = args['username']
        realname = args['realname']
        password = args['password']
        role = args['role']
        logdate = datetime.datetime.now()
        user = User( username=username, realname=realname, role=role, password=password )
        try:
            user.save()
        except IntegrityError as e:
            return make_result( code = Code.PUB_DATA_ERROR, emsg=e.message )
        except Exception as e:
            return make_result( code = Code.PUB_DATA_ERROR, emsg=e.message )
        return make_result( model_to_dict( user ) )

    def put( self ):
        #用户更新
        args = parser.parse_args()
        username = args['username']
        password = args['password']
        realname = args['realname']
        role = args['role']
        user = User( username=username, realname=realname, password=password, role=role )
        try:
            user.update()
        except Exception as e:
            return make_result( code=Code.USER_UPDATE_FAILED )
        return make_result( data=model_to_dict( user ) )

    def get( self ):
        #查询用户
        args = parser.parse_args()
        username=args.get('username')
        users = User.select()
        if username is not None:
            users = users.filter( username = username ).first()
        if users is None:
            return make_result( code=Code.USER_NOT_FOUND )
        else:
            return make_result( [ model_to_dict(user) for user in users ] )

class UserListResource( Resource ):
    def get( self ):
        #查询用户列表
        users = User.select()
        return make_result([ model_to_dict(user) for user in users ])

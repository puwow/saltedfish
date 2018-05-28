#-*- coding:utf-8 -*-
from flask import Flask
import flask_restful
from flask_restful import Resource, Api, abort, reqparse
from resources import UserResource
from config.config import DevConfig
from utils import custom_abort
from flask import jsonify

app = Flask( __name__ )
app.config.from_object( DevConfig )
api = Api( app )

#users资源
#列出所有用户
api.add_resource( UserResource.UserListResource, '/api/v1/users' )
api.add_resource( UserResource.UserResource, '/api/v1/users/<string:username>' )
flask_restful.abort = custom_abort

@app.errorhandler(404)
def not_found_error( error ):
    return jsonify({'code':404, 'msg':'not found error'})

if __name__ == '__main__':
    app.run( debug=True )

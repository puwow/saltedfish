#-*- coding:utf-8 -*-
from flask import jsonify
from codes import Code
from flask_restful import abort

class TransException( Exception ):
    status_code = Code.NOT_FOUND
    def __init__( self, return_code=None, status_code=None, data=None):
        Exception.__init__( self )
        self.return_code = return_code
        if status_code is not None:
            self.status_code = status_code
        self.data = data
    def to_dict( self ):
        return make_result( self.data, self.return_code )

def make_result( data=None, code=Code.SUCCESS, emsg=None ):
    return jsonify( {"code":code, "data":data, "msg":Code.msg[code], "emsg":emsg } )

def custom_abort( http_status_code, *args, **kwargs ):
    if http_status_code == Code.FAILED:
        abort( make_result( code = Code.FAILED ) )
    return abort( http_status_code )

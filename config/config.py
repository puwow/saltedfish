#-*- coding:utf-8 -*-

class Config( object ):
    #配置文件基类
    DATABASE = "SALTEDFISH.db"

class ProdConfig( Config ):
    pass

class DevConfig( Config ):
    DEBUG = True

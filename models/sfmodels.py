#-*- encoding:utf-8 -*-
#desc   用户模型
#author puwow
#create 2018.5.14

from peewee import *
import datetime
import sys
sys.path.append("..")
from config.config import *

database = SqliteDatabase(DevConfig.DATABASE)
class BaseModel( Model ):
    class Meta:
        database = database

#用户模型
class User( BaseModel ):
    userid = AutoField()
    username = CharField( unique=True, help_text='用户名' )
    password = CharField( help_text='用户密码' )
    realname = CharField( help_text='真实姓名' )
    role = CharField( default='1', help_text='用户角色 0-管理员 1-开发人员 2-测试人员' )
    regdate = DateTimeField( default=datetime.datetime.now(), help_text='注册日期' )
    logdate = DateTimeField( default=datetime.datetime.now(), help_text='登录日期' )

    class Meta:
        table_name='User'
        order_by=('regdate',)

#包模型 
class Package( BaseModel ):
    packuuid = CharField( unique=True, help_text='包唯一标识' )
    packname = CharField( help_text='包名' )
    version = CharField( help_text='版本号' )
    cdate = DateTimeField( default=datetime.datetime.now(), help_text='创建日期' )
    mdate = DateTimeField( default=datetime.datetime.now(), help_text='修改日期' )
    filecount = IntegerField( default=0, help_text='文件数量' )
    class Meta:
        table_name='Package'
        order_by=('cdate',)
        indexes=(
                (('version'),True),
                )

#用户故事模型 (用户故事+人是唯一的)
class Story( BaseModel ):
    storyid = CharField( unique=True, help_text='用户故事ID' )
    storyname = CharField(null=True, help_text='用户故事名称' )
    user = ForeignKeyField( User, column_name='userid', help_text='开发人员' )
    ctdate = DateTimeField( default=datetime.datetime.now(), help_text='创建时间' )
    package = ForeignKeyField( Package, column_name='packuuid', help_text='属包' )

    class Meta:
        table_name='Story'
        order_by=('user',)
        #唯一索引
        indexes=( (('storyid','user'),True),)

#文件模型 (文件+用户故事+人是唯一的)
class File( BaseModel ):
    fileid = AutoField()
    filename = CharField( help_text='文件名' )
    filesize = IntegerField(null=True, help_text='文件大小' )
    story = ForeignKeyField( Story, column_name='storyid', help_text='所属用户故事' )
    package = ForeignKeyField( Package, column_name='packuuid', help_text='所属包' )
    cdate = DateTimeField( default=datetime.datetime.now(), help_text='创建时间' )
    cuser = ForeignKeyField( User, help_text='属主' )
    mdate = DateTimeField( default=datetime.datetime.now(), help_text='修改时间' )
    muser = ForeignKeyField( User, help_text='修改人员' )

    class Meta:
        table_name='File'
        order_by=('story',)
        indexes=(
                (('filename','cuser','story'),True),
                )

def create_table():
    #创建表
    try:
        database.connect()
        database.create_tables([Package,User,Story,File])
    finally:
        database.close()

def drop_table():
    try:
        database.connect()
        database.drop_tables([Package,User,Story,File])
    finally:
        database.close()


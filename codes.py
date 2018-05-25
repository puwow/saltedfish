#-*- coding:utf-8 -*-

class Code:
    SUCCESS=200
    FAILED=400
    NOT_FOUND=404 
    PUB_DATA_ERROR = 999

    USER_EXISTS_ERROR=1000
    USER_NOT_FOUND=1004
    USER_UPDATE_FAILED=1005
    USER_ADD_FAILED = 1006

    msg={
        SUCCESS:u"交易成功!",
        FAILED:u"交易失败!",
        NOT_FOUND:u"未找到您请求的资源!",
        PUB_DATA_ERROR:u"数据异常!",
        USER_EXISTS_ERROR:u"用户已存在!",
        USER_NOT_FOUND:u"未找到该用户信息!",
        USER_UPDATE_FAILED:u"更新用户信息失败!",
        USER_ADD_FAILED:"用户注册失败!",
    }

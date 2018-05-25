#-*- coding:utf-8 -*-
from flask import Flask, url_for

app = Flask( __name__ )

@app.route('/user/')
def getUserName():
    return 'qiaogs'

@app.route('/phone/<string:phone>/', methods=['GET','POST'])
def getUserPhone(phone):
    return phone

with app.test_request_context():
    print url_for( 'getUserPhone', phone='18819943121')

if __name__ == '__main__':
    app.run( debug=True )

#-*- coding:utf-8 -*-
from flask_script import Manager, Server
import Main

manager = Manager( Main.app )
manager.add_command( "server", Server() )

@manager.shell
def make_shell_context():
    return dict( app = Main.app )

if __name__ == '__main__':
    manager.run()

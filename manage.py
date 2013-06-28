#coding: utf-8

from flask.ext.script import Manager

from meta.app import build


app = build('../conf/local.py')
manager = Manager(app)


@manager.command
def run():
    app.run(host='0.0.0.0')


if __name__ == '__main__':
    manager.run()

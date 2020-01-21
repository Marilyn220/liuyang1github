# -*- coding: utf-8 -*-
# python 2.7
# @Time    : 2019/3/22 18:00
# @Author  : Chengzy
# @File    : manager.py
# @Software: PyCharm
from ZCD import app
import click
from flask import render_template
from flask.views import MethodView
from ZCD import db
from ZCD.models import User
from ZCD.bigdata import bigdata as bd_app
from ZCD.sayhello import sayhello as say_app

app.register_blueprint(bd_app)
app.register_blueprint(say_app)
#
# @app.cli.command()
# def initdb():
#     db.create_all()
#     click.echo('数据库创建成功')

@app.cli.command()
@click.option('--drop', is_flag=True, help='Create after drop.')
def initdb(drop):
    """Initialize the database."""
    if drop:
        click.confirm('This operation will delete the database, do you want to continue?', abort=True)
        db.drop_all()
        click.echo('Drop tables.')
    db.create_all()
    click.echo('Initialized database.')

# @app.cli.command()
# @click.option('--c',default=10,help='gagaga')
# def forge(c):
#     from faker import Faker


class Index(MethodView):
    def get(self):
        users = User.query.all()
        return render_template('index.html',users=users)



if __name__=="__main__":
    #initdb()
    app.run(host='0.0.0.0',port='7777',debug=True)
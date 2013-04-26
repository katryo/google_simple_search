#coding: utf-8
from bottle import Bottle, route, get, post, run, static_file
from mako.template import Template


template = Template(filename='views/index.tmpl')
app = Bottle()

@route('/static/:path#.+#', name='static')
def static(path):
    return static_file(path, root='static')

@route('/assets/<filepath:path>')
def assets(filepath):
    return static_file(filepath, root='/assets/')

@route('/help')
def help():
    return static_file('help.html', root='/assets/')

@route('/')
@route('/denki')
@route('/hello/<name>')
def greet(name='who'):
    name = name + 'あいあ'
    return template.render(name=name)
run(host='localhost', port=1234, debug=True)

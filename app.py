#coding: utf-8
from bottle import Bottle, route, run, static_file, request
from mako.template import Template
import googlesearch
import pdb


template = Template(filename='static/templates/index.tmpl')
app = Bottle()


@route('/static/:path#.+#', name='static')
def static(path):
    return static_file(path, root='static')


@route('/results')
def results_get():
    return template.render(items='')


@route('/results', method='POST')
def results():
    query = request.forms.decode().get('query')
    items = googlesearch.simple_search(query)
    return template.render(items=items)


@route('/')
def greet():
    return template.render(items='')
run(host='localhost', port=1234, debug=True)

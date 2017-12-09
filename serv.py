from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from pyramid.response import Response
from webob import Request, Response
from jinja2 import Environment, FileSystemLoader

mass = [
  'app.js',
  'react.js',
  'leaflet.js',
  'D3.js',
  'moment.js',
  'math.js',
  'main.css',
  'bootstrap.css',
  'normalize.css',
]

style = []
skript = []

#Распределяем элементы массива по расширению
for elem in mass:
    elemspl = elem.split('.')
        if len(elemspl[1]) == 2:
            skript.append(elem)
        elif len(elemspl[1]) == 3:
            style.append(elem)

def index(request):
    env = Environment(loader=FileSystemLoader('.'))  
    result = env.get_template('/index.html').render({'css1': css, 'js1': js}) 
    return Response(result)

def aboutme(request):
    env = Environment(loader=FileSystemLoader('.'))
    result = env.get_template('aboutme/aboutme.html').render({'css1': css, 'js1': js})
    return Response(result)

if __name__ == '__main__':
    configurator = Configurator()
    configurator.add_route('aboutme', '/aboutme/aboutme.html')
    configurator.add_view(aboutme, route_name='aboutme')
    configurator.add_route('index', '/index.html')
    configurator.add_view(index, route_name='index')
    app = configurator.make_wsgi_app()
    server = make_server('0.0.0.0', 8000, app)
    server.serve_forever()
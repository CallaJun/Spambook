#!/usr/bin/env python
import jinja2
import logging
import os
import webapp2
import json
import fb                     #To install this package run: sudo pip install fb
from facepy import GraphAPI

jinja_environment = jinja2.Environment(loader=
    jinja2.FileSystemLoader(os.path.dirname(__file__)))

class HomeHandler(webapp2.RequestHandler):
    def get(self):
        template_values = {
        }
        template = jinja_environment.get_template('views/home.html')
        self.response.out.write(template.render(template_values))

class MeasureHandler(webapp2.RequestHandler):
    def get(self):  
        template_values = {
        }
        final = self.request.get('input')

        template_values['input'] = final
        template = jinja_environment.get_template('views/measure.html')
        self.response.out.write(template.render(template_values))

routes = [('/', HomeHandler),('/measure', MeasureHandler)]
app = webapp2.WSGIApplication(routes, debug=True) 
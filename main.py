#!/usr/bin/env python
import jinja2
import logging
import os
import webapp2
import json
import fb
from facepy import GraphAPI

FACEBOOK_APP_ID = "851997781477293"
FACEBOOK_APP_SECRET = "bf274f5df71bd6eb29fbadfb255310bb"
#http://graph.facebook.com/endpoint?key=value&access_token=851997781477293|bf274f5df71bd6eb29fbadfb255310bb

jinja_environment = jinja2.Environment(loader=
    jinja2.FileSystemLoader(os.path.dirname(__file__)))

class HomeHandler(webapp2.RequestHandler):
    def get(self):
        template_values = {
        }
        template = jinja_environment.get_template('views/home.html')
        self.response.out.write(template.render(template_values))

class LikeHandler(webapp2.RequestHandler):
    def get(self):  
        template_values = {
        }
        #Some Facebook stuff
        token="CAACEdEose0cBAASb831zZADCqCgpVd9tyLyy9inrE1YX5xJJNZCvTJI7Ng55SpIGCt5KbvFuvIg6ZCtMIewUKuoTjoxWAEu4pGhP8ppHRmNNBQYOliWNJi3D9vo2DiUHhvK7Ha40yb7baixyMOPnACCYK7BdLpAHzGEotc3EPI6isZC8YoKIt7ZA5LcKPm6x9wNX5v8pMqcF3fCh9YmbX1c8LkXZBNxIUZD"
        facebook=fb.graph.api(token)
        graph1 = GraphAPI(token)
        #Getting the username and getting the posts on the profile
        username = self.request.get('username')
        query=str(username)+"/feed?fields=id&limit=5000000000"
        r=graph1.get(query)
        idlist=[x['id'] for x in r['data']]
        idlist.reverse()

        template_values['numposts'] = str(len(idlist))
        template_values['username'] = username
        template = jinja_environment.get_template('views/like.html')
        self.response.out.write(template.render(template_values))

routes = [('/', HomeHandler),('/like', LikeHandler)]
app = webapp2.WSGIApplication(routes, debug=True) 
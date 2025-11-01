# -*- coding: utf-8 -*-
"""
Created on Sat Nov  1 09:23:02 2025

@author: Tuomo.Karasjarvi
"""

from wsgiref.simple_server import make_server

def app(environ, respond):
	respond('200 OK', [('Content-type', 'text/plain; charset=utf-8')])
	yield "Sigma grindset!".encode('utf-8')

if __name__ == '__main__':
	with make_server("localhost", 8001, app) as server: 
         server.serve_forever()

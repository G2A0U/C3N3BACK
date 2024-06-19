# -*- coding: utf-8 -*-
"""
Created on Mon Jul 17 13:19:34 2023

@author: eFabiani
"""

import http.server

import socketserver

import os
os.chdir("/Users/gau20/Desktop/stage programmation/N-back HDG/n2-back")



PORT = 8000




Handler = http.server.SimpleHTTPRequestHandler




with socketserver.TCPServer(("", PORT), Handler) as httpd:

    print("serving at port", PORT)

    httpd.serve_forever()
    
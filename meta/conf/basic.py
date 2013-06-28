#coding: utf-8

import os


base = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

STATIC_PATH = os.path.join(base, 'static')
UPLOAD_PATH = os.path.join(STATIC_PATH, 'upload')

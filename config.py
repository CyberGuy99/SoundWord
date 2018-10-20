import os

class Config(object):
    BASEDIR = os.path.abspath(os.path.dirname(__file__))
    TOP_LEVEL_DIR = os.path.abspath(os.curdir)
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    UPLOADS_DEFAULT_DEST = TOP_LEVEL_DIR + '/tmp/static'
    UPLOADS_DEFAULT_URL = 'http://localhost:5000/static/img/'


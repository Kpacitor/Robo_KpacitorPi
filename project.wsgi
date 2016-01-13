
import sys
import logging

logging.basicConfig(stream=sys.stderr)
sys.path.insert(0,"/var/www/raspberry/")

activate_this = '/var/www/raspberry/venv/bin/activate_this.py'
execfile(activate_this, dict(__file__=activate_this))

from project import app as application
application.secret_key = 'Add your secret key'
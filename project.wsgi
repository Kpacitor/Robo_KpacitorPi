
import sys
import logging

logging.basicConfig(stream=sys.stderr)
sys.path.insert(0,"/var/www/Robo_KpacitorPi/")

activate_this = '/var/www/Robo_KpacitorPi/venv/bin/activate_this.py'
execfile(activate_this, dict(__file__=activate_this))

from kpacitorpi import app as application
application.secret_key = 'Add your secret key'

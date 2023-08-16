import re
from os import environ
id_pattern = re.compile(r'^.\d+$')

CHANNEL_ONE =int(environ.get("CHANNEL_ONE", "-1001983799712"))
CHANNEL_TWO =int(environ.get("CHANNEL_TWO", "-1001586726744"))

DATABASE_URI = environ.get('DATABASE_URI', "mongodb+srv://LINKBYPASSER:LINKBYPASSER@cluster0.1z2z5gw.mongodb.net/?retryWrites=true&w=majority")
DATABASE_NAME = environ.get('DATABASE_NAME', "Cluster0")
ADMINS = [
    int(admin) if id_pattern.search(admin) else admin
    for admin in environ.get('ADMINS', '5274370570,5164928761').split(',')
]

class temp(object):
    LINK_ONE = None
    LINK_TWO = None

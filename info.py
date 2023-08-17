import re
from os import environ
from database import db
id_pattern = re.compile(r'^.\d+$')

CHANNEL_ONE =int(-1001983799712)
CHANNEL_TWO =int(-1001586726744)

ADMINS = [
    int(admin) if id_pattern.search(admin) else admin
    for admin in environ.get('ADMINS', '5274370570,5164928761').split(',')
]

class temp(object):
    LINK_ONE = None
    LINK_TWO = None

def is_requested_one(self , message):
    user = db.get_req_one(int(message.from_user.id))
    if user:
        return True
    if message.from_user.id in ADMINS:
        return True
    return False
    
def is_requested_two(self, message):
    user = db.get_req_two(int(message.from_user.id))
    if user:
        return True
    if message.from_user.id in ADMINS:
        return True
    return False

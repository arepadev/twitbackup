import sys

from libturpial.api.core import Core

message = sys.argv[1]
if not message or message == '':
    sys.exit(-1)

ACCOUNT = 'turpialve-twitter'
BROADCAST = ['satanas82', 'guerrerocarlos']

c = Core()
c.login(ACCOUNT)
c.auth(ACCOUNT)

for acc in BROADCAST:
    c.send_direct(ACCOUNT, acc, message)

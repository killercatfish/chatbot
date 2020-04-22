'''
This will send commands to a screen named test.
# https://unix.stackexchange.com/questions/110055/send-command-to-detached-screen-and-get-the-output
'''

import pexpect, time

# spawn new bash session
session = pexpect.spawn('/bin/bash')

# send screen command
session.sendline('screen -S test -p 0 -X stuff "echo Hello World"')
session.sendline('screen -S test -p 0 -X eval "stuff \\015"')

# give the command a chance to execute
time.sleep(0.1)


session.close()
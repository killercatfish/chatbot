'''
This will send commands to a screen named test.
# https://unix.stackexchange.com/questions/110055/send-command-to-detached-screen-and-get-the-output
'''

import pexpect, time, subprocess, sys

# spawn new bash session
session = pexpect.spawn('/bin/bash')

# send screen command
session.sendline('screen -S test -p 0 -X stuff "echo Hello World"')
session.sendline('screen -S test -p 0 -X eval "stuff \\015"')

# give the command a chance to execute
time.sleep(0.1)

'''
Below i attempted to read the output stream of the other screen, but didnt seem to work.  Might be something there though.
'''

# cmd = "screen -r test"

# p = subprocess.Popen("screen -r test", stdout=subprocess.PIPE, bufsize=1, shell=True)
# # p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
    
# while True:
#     out = p.stdout.read(0)
#     if out == '' and p.poll() != None:
#         break
#     if out != '':
#         sys.stdout.write(str(out))
#         sys.stdout.flush()


session.close()
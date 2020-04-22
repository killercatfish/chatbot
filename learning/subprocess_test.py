#!/usr/bin/python
import subprocess, sys
## command to run - tcp only ##
cmd = "screen -S lux -p 0 -X stuff \"cd //Applications\""
 
## run it ##
p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
 
## But do not wait till netstat finish, start displaying output immediately ##
while True:
    out = str(p.stdout_thread)
    if out == '' and p.poll() != None:
        break
    if out != '':
        sys.stdout.write(out)
        sys.stdout.flush()
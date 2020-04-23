'''
Version 0.1
i think this my slag my macbook pro.
'''
import pexpect, time

log_length = 0
previous_length = 0
with open('/Applications/tmp/mylog.txt', 'r') as file:
    lines = file.readlines()
    log_length = len(lines)
    previous_length = log_length
    # print("length: " + str(log_length))
    # print("last line: " + lines[len(lines)-1])

# spawn new bash session
session = pexpect.spawn('/bin/bash')



# give the command a chance to execute
time.sleep(0.1)

while True:
    with open('/Applications/tmp/mylog.txt', 'r') as file:
        lines = file.readlines()
        log_length = len(lines)
        if log_length > previous_length:
            lines_to_check = log_length - previous_length
            previous_length = log_length
            print("**** " + str(lines_to_check) + " lines added: ")
            for i in range(lines_to_check):
                line = lines[len(lines)-i-1]
                check = 'has joined with'
                if check in line:
                    print('++++YES: ' + line)
                    # # send screen command
                    session.sendline('screen -S lux -p 0 -X stuff "Hello World"')
                    session.sendline('screen -S lux -p 0 -X eval "stuff \\015"')
                else:
                    print('***** NO: ' + line)

session.close()
 
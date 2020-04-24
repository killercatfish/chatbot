'''
Version 0.1
i think this may slag my macbook pro.

Next version: 
Welcome player by name
Guest in and out
change settings 
'''
import pexpect, time, threading

# Find the end of the log file
def initialize():
    # A couple of globals
    log_length = 0
    previous_length = 0
    with open('/Applications/tmp/mylog.txt', 'r') as file:
        lines = file.readlines()
        log_length = len(lines)
    previous_length = log_length

    return (previous_length, log_length)
        # print("length: " + str(log_length))
        # print("last line: " + lines[len(lines)-1])

def run(previous_length, log_length):

    # Continuously check log file for new entry
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
                    check = 'has joined from IP'
                    print("line " + str(i + 1) + ": " + line)
                    
                    if check in line:
                        # welcome(line)
                        t = threading.Timer(3, welcome, [line])
                        t.start()
                        
        
        time.sleep(0.1)
    # Need to move this to an exit function when ctrl+c is pressed

def welcome(line):
    # spawn new bash session
    session = pexpect.spawn('/bin/bash')
    words = line.split(' ')
    name = ' '.join(words[:words.index('has')]) # Find the name, could be more than one word.

    print("***** Line: " + line)
    print("***** name: " + name, end="\n\n")

    # cmd = 'screen -S lux -p 0 -X stuff \"Welcome, ' + name + '\"'
    cmd = 'screen -S lux -p 0 -X stuff \"Welcome, %s :-)\"' % name
    
    # # send screen command
    session.sendline(cmd)
    session.sendline('screen -S lux -p 0 -X eval "stuff \\015"')
    
    time.sleep(0.1)

    session.close()
    
    # give the command a chance to execute

def main():
    (previous_length, log_length) = initialize()
    run(previous_length, log_length)
    print("hello world!")

if __name__ == "__main__":
    main()
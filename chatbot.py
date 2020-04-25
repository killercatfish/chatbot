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
    with open('/usr/games/LuxDelux/logs/mylog.txt', 'r') as file:
        lines = file.readlines()
        log_length = len(lines)
    previous_length = log_length

    return (previous_length, log_length)
        # print("length: " + str(log_length))
        # print("last line: " + lines[len(lines)-1])

def run(previous_length, log_length):

    # Continuously check log file for new entry
    while True:
        with open('/usr/games/LuxDelux/logs/mylog.txt', 'r') as file:
            lines = file.readlines()
            log_length = len(lines)
            if log_length > previous_length:
                lines_to_check = log_length - previous_length
                previous_length = log_length
                print("**** " + str(lines_to_check) + " lines added: ")
                for i in range(lines_to_check):
                    line = lines[len(lines)-i-1]
                    print("LINE: " + line)
                    check_line(line)
                        
        
        time.sleep(0.1)
    # Need to move this to an exit function when ctrl+c is pressed

def check_line(line):
    # print("line " + str(i + 1) + ": " + line)
    # print("***" + str(split_line[1][0]))
    # Welcome!
    player_joined = 'has joined from IP'
    game_over = 'GameIsOver -> '
    if player_joined in line:
        # welcome(line)
        # https://www.geeksforgeeks.org/timer-objects-python/
        # https://stackoverflow.com/questions/4415672/python-theading-timer-how-to-pass-argument-to-the-callback
        t = threading.Timer(3, welcome, [line])
        t.start()
    
    if game_over in line:
        print("+++GAME OVER+++")
    
    # Checking for # and command entered.
    if ':' in line:
        start = line.index(":") # Check location of colon
        # print("Start: " + str(start))
        if len(line) > start + 2:
            line_no_name = line[start+2:] # remove name of user who wrote
            check_hash_mark = True if line[start+2:][0] == '#' else False # is first char #
            line_no_name = line_no_name.split(' ') # split line by space
            line_no_name_len = len(line_no_name) # get number of items in list

            # High probability that a command was entered.  So we will go and check if its a valid
            if check_hash_mark and line_no_name_len == 1:
                command = line_no_name[0].rstrip() # remove an \n 
                print("Command entered: " + command)
                check_command(command)

    # if line[1][0] == '#' and line[len(line)-1][len(line[len(line)-1])-1]

def check_command(command):
    with open('commands/command_list.txt') as f:
        commands = f.readlines()
        commands = [x.strip() for x in commands]
    print(str(commands))

    if command == '#CommandList':

        cmd = 'screen -S lux -p 0 -X stuff \"'
        for i in range(len(commands)):
            if i == len(commands) - 1:
                cmd = cmd + commands[i]
            else:
                cmd = cmd + commands[i] + ' - '
        cmd = cmd + '\"'
        # print("CMD: " + cmd)
        # spawn new bash session
        session = pexpect.spawn('/bin/bash')
        session.sendline(cmd)
        session.sendline('screen -S lux -p 0 -X eval "stuff \\015"')
        time.sleep(0.1)
        session.close()
    
    elif command == '#Help':
        cmd = 'screen -S lux -p 0 -X stuff \"BioButler is in the beta stages of becoming a chat bot to improve your bio experience.\"'
        session = pexpect.spawn('/bin/bash')
        session.sendline(cmd)
        session.sendline('screen -S lux -p 0 -X eval "stuff \\015"')
        time.sleep(0.1)
        session.close()

def welcome(line):
    # spawn new bash session
    session = pexpect.spawn('/bin/bash')
    words = line.split(' ')
    name = ' '.join(words[:words.index('has')]) # Find the name, could be more than one word.

    print("***** Line: " + line)
    print("***** name: " + name)

    # cmd = 'screen -S lux -p 0 -X stuff \"Welcome, ' + name + '\"'

    if name == 'RogueMonk':
        cmd = 'screen -S lux -p 0 -X stuff \"Welcome, master :-)\"'
    elif name == 'Landlord':
        cmd = 'screen -S lux -p 0 -X stuff \"Shalom, %s :-)\"' % name
    elif name == 'MrMartini':
        cmd = 'screen -S lux -p 0 -X stuff \"Welcome, sir :-)\"'
    else:
        cmd = 'screen -S lux -p 0 -X stuff \"Welcome, %s :-)\"' % name

    print("***** cmd: " + cmd)
    
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
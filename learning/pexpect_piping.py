'''
Open a lux host within this script
-can i pipe all the output if its spawned here?

1. Must have a screen -S lux running.

screen commands:
what screen am I attached to? echo $STY

OK cant get the java to go there with the extra quotes....
'''

import pexpect, time

# spaw new screen
# lux_screen = pexpect.spawn('screen -S lux') # If i create this here, the 2nd sendline on line 18 doesnt execute properly?

# spawn new bash session
session = pexpect.spawn('/bin/bash')

session.sendline('screen -S lux -p 0 -X stuff "cd //Applications"')
# the following wont work if I spawn the lux screen in here.
session.sendline('screen -S lux -p 0 -X eval "stuff \\015"')
time.sleep(0.1)
# time.sleep(0.2)
# with open('cmd.txt', 'r') as file:
#     java = str(file.readlines()[0])
#     print(java)
    
java = 'screen -S lux -p 0 -X stuff java -Djava.awt.headless=true -cp \"./Lux Delux.app/Contents/Java/LuxCore.jar:./Lux Delux.app/Contents/Java/MRJAdapter.jar\" com.sillysoft.lux.Lux -headless -network=true -public=true -map=BioDeux-extreme -cards=5e25 -conts=25 -time=35 -name=Killercatfish -desc=EXPERIMENTAL -nofirstturncontbonus -abortbotgames -novariablestart -port=6622\"'
# can i send the java command via sendline when it has those quotes?
# print(java)

test = "\"hello\""

cmd = 'screen -S lux -p 0 -X stuff %s' % java

print(cmd)

session.sendline(cmd)
session.sendline('screen -S lux -p 0 -X eval "stuff \\015"')
# quit session
# session = pexpect.spawn('screen -XS 26258 quit')

# # send screen command
# session.sendline('screen -S test -p 0 -X stuff "echo Hello World"')
# session.sendline('screen -S test -p 0 -X eval "stuff \\015"')

# # give the command a chance to execute
time.sleep(0.1)

# lux_screen.close()
session.close()
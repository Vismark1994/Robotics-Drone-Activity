
import socket
import sys, tty, termios


''' DO NOT MODIFY'''
#####################################
#           getChar()               #
#                                   #
#   Method processes user input     #
#   as it's received from user.     #
#   The input is expected to be     #
#   a char value. This value is     #
#   returned and program proceeds   #
#   accordingly.                    #
#                                   #
#####################################

'''
This function just waits for you to type a 
keyboard key. When you do, this function will read it
into the program.
'''
def getChar():
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch



''' DO NOT MODIFY'''
#####################################
#           setBits( lst )          #
#                                   #
#   Manipulates the bit values of   #
#   the specified drone command.    #
#   Specific bits need to be        #
#   set to 0 or 1 in order for the  #
#   drone to perform desired        #  
#   actions. This function sets     #
#   these bits accordingly.         #
#                                   #
#####################################
def setBits( lst ):
    """
    set the bits in lst to 1.
    also set bits 18, 20, 22, 24, and 28 to one (since they should always be set to 1 (because they are never used))
    all other bits will be 0
    """
    res = 0
    for b in lst + [18,20,22,24,28]:
        res |= (1 << b)
    return res
    


''' DO NOT MODIFY'''
#####################################
#         sendCommand( cmd ):       #
#                                   #
#   Sends the AT* command to the    #
#   ARDrone. This is the last       #
#   processing step taken by the    #
#   program--given that the drone   # 
#   is left to process the info this#  
#   function sends it. This method  #
#   also increments seqno count in  #
#   preparation of any future       #
#   commands.                       #
#                                   #
#####################################
def sendCommand( cmd ):
    global address
    global seqno
    global s
    print ("DEBUG: Sending:  '%s' " % cmd.strip())
    s.sendto(cmd,address)
    seqno += 1



''' DO NOT MODIFY'''
#####################################
#             reset()               #
#                                   #
#  Resets the seqno variable and    #
#  prepares drone for takeoff by    #
#  re-calibrating.                  #
#                                   #
#####################################
def reset():
    global seqno
    seqno = 1
    sendCommand("AT*FTRIM=%d\r" % seqno )



''' DO NOT MODIFY'''
#Sends the drone a command (""AT*FTRIM=%d\r" % seqno") for the drone to take off.
def takeoff():
    global seqno
    sendCommand("AT*FTRIM=%d\r" % seqno ) #calibrating before takeoff
    takeoff_cmd = setBits([9]) #bit 9 is used for takeoff
    for i in xrange(1,25):
        sendCommand("AT*REF=%d,%d\r" % (seqno,takeoff_cmd))


''' DO NOT MODIFY'''
def land():
    global seqno
    land_cmd = setBits([])
    for i in xrange(1,25):
        sendCommand("AT*REF=%d,%d\r" % (seqno,land_cmd))

''' DO NOT MODIFY'''
def toggleEmergencyMode():
    global seqno
    shutdown_cmd = setBits([8]) #bit 8 to toggle emergency mode
    sendCommand("AT*REF=%d,%d\r" % (seqno,shutdown_cmd))

# ----------------------------------------------------------------


'''
NOTES: 

Sending a command to the drone is very simple.  A valid command contains 4 pieces of information.  Each
piece of information determines the direction the drone will move in.  This is specified in a 10 digit number 
(positive for forward, negative for backward). There are 4 variables you'll need to set:

- "ROLL": the amount to turn left/right
- "PITCH": the amount to move forward/backward
- "GAZ": the amount to move up/down
- "YAW": The amount to move left/right

"ROLL": Turns the drone to the LEFT or RIGHT.
        A NEGATIVE number moves the drone to the left, a POSITIVE
        number moves it to the right.

"PITCH": Moves the drone FORWARD or BACKWARD.
         A NEGATIVE number moves the drone backwards, a POSITIVE
         number moves it forwards.

"GAZ": Moves the drone UP or DOWN. 
       A NEGATIVE number moves the drone down.  A POSITIVE number
       moves the drone up.

"YAW": Makes the drone fly to the left or right. A NEGATIVE number
       makes the drone fly to the left. A POSITIVE number makes the
       drone fly to the right.


The command will need to be sent to the "sendCommand()" method within a "for" loop as shown below:

    for i in xrange(1, 250):
        sendCommand("AT*PCMD=%d,%d,%d,%d,%d,%d\r" % (seqno,1,ROLL,PITCH,GAZ,YAW))


But, you'll need to create a variable for "ROLL", "PITCH", "GAZ", "YAW" and give them values to specify how you
want the drone to move. 

For example, if you want the drone to move FORWARD, you need to set the variable that controls forward/backward
movement to a number that is 10 integers long (for example, 1324543256, or 43564836294, or -2432543456).

Depending on whether the number is a positive number or negative number, the drone will move forward or backward
(it will move forward if the number is positive.  it will move backward if the number is negative).


The following method makes the drone move to the left:

def move_left():
    global seqno
    ROLL = -1082130432
    PITCH = 0
    GAZ = 0
    YAW = 0
    
    for i in xrange(1, 250):
        sendCommand("AT*PCMD=%d,%d,%d,%d,%d,%d\r" % (seqno,1,ROLL,PITCH,GAZ,YAW))


'''


#TODO: Write a function that will cause the drone to turn left.




#TODO: Write a function that will cause the drone to turn right.



#TODO: Write a function that will cause the drone to move forward.



#TODO: Write a function that will cause the drone to move backward.



#TODO: Write a function that will cause the drone to move up.



#TODO: Write a function that will cause the drone to move down.



#TODO: Write a function that will cause the drone to fly to the left.



#TODO: Write a function that will cause the dron to fly to the right.





'''   #ANSWERS ARE BELOW
def move_left():
    global seqno
    ROLL = -1082130432
    PITCH = 0
    GAZ = 0
    YAW = 0
    
    for i in xrange(1, 250):
        sendCommand("AT*PCMD=%d,%d,%d,%d,%d,%d\r" % (seqno,1,ROLL,PITCH,GAZ,YAW))




def move_right():
    global seqno
    ROLL = 1065352316
    PITCH = 0
    GAZ = 0
    YAW = 0

    for i in xrange(1,250):
        sendCommand("AT*PCMD=%d,%d,%d,%d,%d,%d\r" % (seqno,1,ROLL,PITCH,GAZ,YAW))
    


def move_forwards():
    global seqno
    ROLL = 0
    PITCH = 1065353216
    GAZ = 0
    YAW = 0

    for i in xrange(1,250):
        sendCommand("AT*PCMD=%d,%d,%d,%d,%d,%d\r" % (seqno,1,ROLL,PITCH,GAZ,YAW))




def move_backwards():
    global seqno
    ROLL = 0
    PITCH = -1082130432
    GAZ = 0
    YAW = 0

    
    for i in xrange(1,250):
        sendCommand("AT*PCMD=%d,%d,%d,%d,%d,%d\r" % (seqno,1,ROLL,PITCH,GAZ,YAW))



def ascend():
    global seqno
    ROLL = 0
    PITCH = 0
    GAZ = 1065353216
    YAW = 0

    for i in xrange(1,250):
        sendCommand("AT*PCMD=%d,%d,%d,%d,%d,%d\r" % (seqno,1,ROLL,PITCH,GAZ,YAW))
    

def descend():
    global seqno
    ROLL = 0
    PITCH = 0
    GAZ = -1082130432
    YAW = 0

    for i in xrange(1,250):
        sendCommand("AT*PCMD=%d,%d,%d,%d,%d,%d\r" % (seqno,1,ROLL,PITCH,GAZ,YAW))


def yaw_left(): #move left
    global seqno
    ROLL = 0
    PITCH = 0
    GAZ = 0
    YAW = -1082130432

    for i in xrange(1,250):
        sendCommand("AT*PCMD=%d,%d,%d,%d,%d,%d\r" % (seqno,1,ROLL,PITCH,GAZ,YAW))



def yaw_right(): #move right
    global seqno
    ROLL = 0
    PITCH = 0
    GAZ = 0
    YAW = 1065353216

    for i in xrange(1,250):
        sendCommand("AT*PCMD=%d,%d,%d,%d,%d,%d\r" % (seqno,1,ROLL,PITCH,GAZ,YAW))

'''




def printPossibleCommandsToScreen():
    print("\n\n")
    print("Keyboard commands:")
    print("\tq       - quit")
    print("\tt       - takeoff")
    print("\tl       - land")
    print("\tu       - ascend")
    print("\tj       - descend")
    print("\th       - left")
    print("\tk       - right")
    print("\ty       - forwards")
    print("\tn       - backwards")
    print("\tz       - yaw_left")
    print("\tm       - yaw_right")
    print("\t(space) - emergency shutoff")


print("""
NOTE:  This program assumes you are already connected to the
       drone's WiFi network.
""")
    
address = ('192.168.1.1',5556)
seqno = 1
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(("", 5554))

while True:
    printPossibleCommandsToScreen()
    ch = getChar()
    if ch == 'q':
        exit(0)
    elif ch == 't':
        takeoff()
    elif ch == 'l':
        land()
    elif ch == 'u':
         pass #ascend()
    elif ch == 'j': 
        pass #descend()
    elif ch == 'h':
        pass #move_left()
    elif ch == 'k':
        pass #move_right()
    elif ch == 'y':
        pass #move_forwards()
    elif ch == 'n':
        pass #move_backwards()
    elif ch == 'z':
        pass #yaw_left()
    elif ch == 'm':
        pass #yaw_right()   
    elif ch == ' ':
        reset()
        toggleEmergencyMode()   
    else:
        print("Invalid command!")
        
    

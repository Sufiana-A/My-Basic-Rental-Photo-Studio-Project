from time import time
import vlc
import time
""""
def delay(howlong):
    print("Sound and message will imediately appear")
    #song.set_time(howlong*60) #in milliseconds
    time.sleep(howlong*60) #in seconds
    song = vlc.MediaPlayer("Time limit.mp3")
    song.play()
    print("Your Rental time is over.\nPlease empty this room before our staff inspect this room!")
delay(2)
"""
def timer(s):
    time.sleep(s)
    print('Audio Playing...')
timer(5)
inp = input("Play audio(yes/no): ")
while inp == 'yes' or inp == 'Yes':
    song = vlc.MediaPlayer('Time limit.mp3')
    song.play()
    break
else:
    print("Audio is not played")


#def delay(fn, ms, *args):
    #sleep(ms / 1000)
    #return fn(*args)
#print("Square root after specific mileseconds: ")
#delay(lambda x: math.sqrt(x), 100, 16) #sometimes you need to call function with print 
#delay(lambda x: math.sqrt(x), 1000, 100)
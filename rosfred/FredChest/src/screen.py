#!/usr/bin/env python
import roslib; roslib.load_manifest('FredChest')
import rospy
import pygame.display
import pygame.image
from Planner.msg import Mood
from std_msgs.msg import String
import os


def callbackscreen(message):
	if message.data == "full":
		screenplane = pygame.display.set_mode((0,0),pygame.FULLSCREEN,0)
		screenplane.blit(picture, (0, 0))
		pygame.display.update()
		rospy.loginfo(rospy.get_name()+"Switching to fullscreen mode")
	elif message.data == "close":
		screenplane = pygame.display.set_mode((0,0),0,0)
		screenplane.blit(picture, (0, 0))
		pygame.display.update()
		rospy.loginfo(rospy.get_name()+"Closing fullscreen mode")	

def callback(message):
	#-100 to 100 input moved to 0 to 200 and normalized over 255.
    level = int(((message.data+100)%201)*1.275)
    rospy.loginfo(rospy.get_name()+"Mood input: %i,rg(not b) level: %i",message.data,level)
    #colors are set at 255,255,0 when happy (yellow), downto to 0,0,255 when sad (blue)
	#at neutral it is grey coloured
    screenplane.fill((level,level,255-level,0))
    screenplane.blit(picture, (0, 0))
    pygame.display.update()

def screen():
    rospy.init_node('screen')
    rospy.Subscriber("mood", Mood, callback)
    rospy.Subscriber("screen",String, callbackscreen)
    rospy.spin()

if __name__ == '__main__':
	pygame.display.init()
	print os.getcwd()
	picture = pygame.image.load("sign.png")
	#screen resolution: (0,0) is current, flags: pygame.FULLSCREEN for fullscreen, depth.
	screenplane = pygame.display.set_mode((0,0),pygame.FULLSCREEN,0)
	screenplane.blit(picture, (0, 0))
	pygame.display.update()
	screen()
	

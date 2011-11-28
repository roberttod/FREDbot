#!/usr/bin/env python
import roslib; roslib.load_manifest('FredChest')
import rospy
import pygame.display
from Planner.msg import Mood


def callback(msg):
    rgbvalue = int(((msg.data)%100)*2.55)
    rospy.loginfo(rospy.get_name()+"Setting rgb value to %s",rgbvalue)
    #screen resolution: (0,0) is current, flags: pygame.FULLSCREEN for fullscreen, depth.
    screenplane.fill((rgbvalue,rgbvalue,rgbvalue,0))
    pygame.display.update()

def screen():
    rospy.init_node('screen', anonymous=True)
    rospy.Subscriber("mood", Mood, callback)
    rospy.spin()

if __name__ == '__main__':
    pygame.display.init()
    screenplane = pygame.display.set_mode((0,0),0,0)
    screen()
	

//This is a test program showing how to interface with the 
//emotive speech synthersiser 

#include "ros/ros.h"
#include "emote_text.h" //custom message type
#include <sstream>
#include <iostream>
#include <fstream>
using namespace std;




	
 


int main(int argc, char **argv)
{
  ros::init(argc, argv, "talker");
  ros::NodeHandle n;
  ros::Publisher chatter_pub = n.advertise<speech_synth::emote_text>("chatter", 1000);

  ros::Rate loop_rate(0.02); //one message every 50s

  int count = 0;
  int no_lines = 0;

 //Read the text file into an array
 static const char filename[] = "phrases.txt";
	FILE *file = fopen ( filename, "r" );
	int i, j;
	char arra[128][128];
	char line[128]; /* or other suitable maximum line size */

	for(i=0; i<128; i++)
	for(j=0; j<128; j++)
	arra[i][j] = '\0';

	for(i=0; i<128; i++)
	line[i] = '\0';

if ( file != NULL )
{
	i=0;
	while ( fgets ( line, sizeof line, file ) != NULL ) /* read a line */
	{

		strcpy(arra[i], line);
		printf("array ----> %s ", &arra[i]);
		i++;
	}
	no_lines = i-1;
	fclose ( file );
}
else
{
	perror ( filename );
}

  while (ros::ok())
  {

   speech_synth::emote_text msg; //create a new message object

    std::stringstream ss;
    //ss << "hello world " << count;
    if (i > no_lines) {i = 0;}
    ss << arra[i];
    i++;
    msg.text = ss.str();
    msg.emotion = (rand()%11)-5; //-5 to 5

    ROS_INFO("%s | I feel: %f", msg.text.c_str(), msg.emotion);

    chatter_pub.publish(msg);

    ros::spinOnce();

    loop_rate.sleep();
    ++count;
  }


  return 0;
}

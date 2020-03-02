import cv2
import numpy as np  

maps = cv2.imread('Maps.png',0)
robot = cv2.imread('robot.png',0)
robot_sensor = cv2.imread('robot_sensor.png',0)

rows,cols = robot.shape
x,y = 200,350

map_snippet = maps[x-(rows/2):x+(rows/2) , y-(cols/2):y+(cols/2)]

maps_copy = maps.copy()

maps_copy[x-(rows/2):x+(rows/2) , y-(cols/2):y+(cols/2)] = robot


cv2.imshow("Map Segments",np.bitwise_or(map_snippet,robot_sensor))

edged = cv2.Canny(np.bitwise_or(map_snippet,robot_sensor), 30, 200) 
contours, hierarchy = cv2.findContours(edged,  
    cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE) 

for cnt in contours:

	rect = cv2.boundingRect(cnt)
	area = rect[2] * rect[3]
	if(area > 40):
		M = cv2.moments(cnt)
		c_x = int(M["m10"] / M["m00"])
		c_y = int(M["m01"] / M["m00"])
		if(c_y < 14):
			print("sensor 1 is active")
		

		if(c_y > 14 and c_y < 28):
			print("sensor 2 is active")


		if(c_y > 28):
			print("sensor 3 is active")



cv2.imshow("Line Following Simulator",maps_copy)

cv2.waitKey(0)



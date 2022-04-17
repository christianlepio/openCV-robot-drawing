import cv2 as cv
import numpy as np
#              height, width
robot = np.zeros((700, 600, 3), dtype='uint8')

#BackGround_color
robot[:] = 255,255,255
#Rectangle ulo
#x1=left, y1=top, x2=right, y2=bottom
#                    x1,y1     x2,y2
cv.rectangle(robot, (200,150),(400,250),(0,0,0), thickness=cv.FILLED)
#Rectangle buhok 
cv.rectangle(robot, (235, 130), (365, 145), (0,0,0), thickness=cv.FILLED)
cv.rectangle(robot, (245, 123), (355, 145), (0,0,0), thickness=cv.FILLED)
cv.rectangle(robot, (260, 114), (340, 145), (0,0,0), thickness=cv.FILLED)
cv.rectangle(robot, (275, 107), (325, 145), (0,0,0), thickness=cv.FILLED)
cv.rectangle(robot, (290, 100), (310, 145), (0,0,0), thickness=cv.FILLED)

#circle mata
cv.circle(robot, (250,200), 37, (255,255,255), thickness=3)

#circle mata
cv.circle(robot, (348,200), 37, (255,255,255), thickness=3)

#circle mata
cv.circle(robot, (260,185), 5, (255,255,255), thickness=cv.FILLED)

#circle mata
cv.circle(robot, (358,185), 5, (255,255,255), thickness=cv.FILLED)

#Rectangle Left Ear
#x1=left, y1=top, x2=right, y2=bottom
#                    x1,y1     x2,y2
cv.rectangle(robot, (191,170),(197, 230),(0,0,0),thickness=cv.FILLED)
cv.rectangle(robot, (184,181),(194, 219),(0,0,0),thickness=cv.FILLED)

#Rectangle Right Ear
#x1=left, y1=top, x2=right, y2=bottom
#                    x1,y1     x2,y2
cv.rectangle(robot, (403,170),(409, 230),(0,0,0),thickness=cv.FILLED)
cv.rectangle(robot, (410,181),(416, 219),(0,0,0),thickness=cv.FILLED)

#Rectangle neck
#x1=left, y1=top, x2=right, y2=bottom
#                    x1,y1     x2,y2
cv.rectangle(robot, (252,255),(348,275),(0,0,0),thickness=cv.FILLED)

#Rectangle body
#x1=left, y1=top, x2=right, y2=bottom
#                    x1,y1     x2,y2
cv.rectangle(robot, (150,280), (450,480), (0,0,0), thickness=cv.FILLED)
cv.rectangle(robot, (170, 320),(430,400),(255,255,255),thickness=cv.FILLED)

#Rectangle Arm
#x1=left, y1=top, x2=right, y2=bottom
#                    x1,y1     x2,y2
cv.rectangle(robot, (75,285), (145,340), (0,0,0), thickness=cv.FILLED)
cv.rectangle(robot, (455,285), (525,340), (0,0,0), thickness=cv.FILLED)

#line Braso
#
cv.line(robot, (110,340), (110,450), (0,0,0), thickness=25)
cv.line(robot, (490,340), (490,450), (0,0,0), thickness=25)

cv.circle(robot, (110, 485), 40, (0,0,0), thickness=cv.FILLED)
cv.circle(robot, (110, 499), 30, (255,255,255), thickness=cv.FILLED)

cv.circle(robot, (491, 485), 40, (0,0,0), thickness=cv.FILLED)
cv.circle(robot, (491, 499), 30, (255,255,255), thickness=cv.FILLED)

#line lower body
cv.line(robot, (220,490), (380,490), (0,0,0), thickness=10)
cv.line(robot, (230,500), (370,500), (0,0,0), thickness=10)
cv.line(robot, (240,510), (360,510), (0,0,0), thickness=10)
cv.line(robot, (250,520), (350,520), (0,0,0), thickness=10)
cv.line(robot, (260,530), (340,530), (0,0,0), thickness=15)
cv.line(robot, (268,540), (332,540), (0,0,0), thickness=15)
cv.line(robot, (278,550), (322,550), (0,0,0), thickness=15)
cv.line(robot, (288,560), (312,560), (0,0,0), thickness=15)
cv.line(robot, (298,570), (302,570), (0,0,0), thickness=20)
cv.line(robot, (308,580), (292,580), (0,0,0), thickness=10)
cv.line(robot, (220,490), (300,590), (0,0,0), thickness=10)
cv.line(robot, (380,490), (300,590), (0,0,0), thickness=10)

#circle gulong
cv.circle(robot, (300, 623), 60, (255,255,255), thickness=cv.FILLED)
cv.line(robot, (300,550), (300,631), (0,0,0), thickness=13)
cv.circle(robot, (300, 630), 60, (0,0,0), thickness=cv.FILLED)
cv.circle(robot, (300, 630), 50, (255,255,255), thickness=3)
cv.circle(robot, (300, 630), 9, (255,255,255), thickness=3)

#line gulong
cv.line(robot, (300,589), (300, 615), (255,255,255), thickness=3)
cv.line(robot, (300,647), (300, 672), (255,255,255), thickness=3)
cv.line(robot, (300,647), (300, 672), (255,255,255), thickness=3)
cv.line(robot, (255,630), (284, 630), (255,255,255), thickness=3)
cv.line(robot, (315,630), (344, 630), (255,255,255), thickness=3)
cv.line(robot, (270,598), (289, 620), (255,255,255), thickness=3)
cv.line(robot, (330,598), (310, 620), (255,255,255), thickness=3)
cv.line(robot, (270,660), (289, 640), (255,255,255), thickness=3)
cv.line(robot, (330,660), (313, 640), (255,255,255), thickness=3)

#putText()
cv.putText(robot, "CS Professional Elective 3", (110, 20), cv.FONT_HERSHEY_SIMPLEX, 0.9, (0,0,0), thickness=2)
cv.putText(robot, "CARREON, LEPIO, TADENA", (140, 80), cv.FONT_HERSHEY_SIMPLEX, 0.8, (0,0,0), thickness=2)
cv.putText(robot, "b3hB3hkuh24 <3", (204, 370), cv.FONT_HERSHEY_SIMPLEX, 0.7, (0,0,0), thickness=2)
cv.putText(robot, "MapagMAhal", (380, 570), cv.FONT_HERSHEY_SIMPLEX, 0.9, (0,0,0), thickness=2)
cv.putText(robot, "na", (420, 600), cv.FONT_HERSHEY_SIMPLEX, 0.9, (0,0,0), thickness=2)
cv.putText(robot, "ROBOT", (395, 630), cv.FONT_HERSHEY_SIMPLEX, 0.9, (0,0,0), thickness=2)

cv.imshow("Robot", robot)
cv.waitKey(5000)
Theme : Broadcast football amateur games with tracking football ball

-Purpose

In amateur games, there are not only broadcasts but also referees themselves, 
and if you want to leave a video like this, the goal is to detect the ball and automatically follow the camera around the ball.

: 아마추어 경기에서는 중계 뿐만 아니라 심판 자체도 없는 경우가 있는데 이와같이 영상을 남기고 싶은 경우 카메라를 설치해두면 공을 탐지하여 자동으로 공 중심으로 카메라가 따라가는 것을 목표로 한다.


-Operation

opencv & keras & dlib : face detection, eye roi

train : AlexeyAB darknet YOLOv4 

detection : raspberry pi 4 4gb + raspberry pi IR-CUT camera

operation : Started state, regardless of Excel, the speed of the car is not 0km. Warning sound when closed for 2.5 to 3 seconds.

-datasets

taken by myself

total 1000 images. 

-requirements

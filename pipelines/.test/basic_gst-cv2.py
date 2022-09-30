#################################################################################################
#                                                                                               #
#   Command to test the integration of gstreamer backend with opencv                            #
#   If this command fails opencv has to be installed/built from souce with gstreamer enabled    #
#   refer to cmake tutorial on this.                                                            #
#                                                                                               #
#################################################################################################
import cv2
import numpy as np
# command used to check gstreamer:
#gst-launch-1.0 videotestsrc ! videoconvert ! appsink
gst_command = 'videotestsrc ! videoconvert ! appsink'

#integration with opencv
cap = cv2.VideoCapture(gst_command, cv2.CAP_GSTREAMER)


while True:
    ret, frame = cap.read()
    #
    if ret == False:
         print(frame)
    else:
        cv2.imshow("FrameREAD",frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
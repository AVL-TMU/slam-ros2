

import cv2
import numpy as np
# command used to check gstreamer:
#gst-launch-1.0 videotestsrc ! videoconvert ! appsink
gst_command = 'videotestsrc ! videoconvert ! appsink'

#integration with opencv

frame_width = 240
frame_height = 320

cap = cv2.VideoCapture(gst_command, cv2.CAP_GSTREAMER)
gst_str_rtp = "appsrc ! video/x-raw,format=BGR ! queue ! videoconvert ! video/x-raw,format=BGRx !  h264parse ! rtph264pay ! udpsink host=127.0.0.1 port=8000 auto-multicast=0"

out = cv2.VideoWriter(gst_str_rtp, cv2.CAP_GSTREAMER, 0, float(52), (frame_width, frame_height), True)


while True:
    ret, frame = cap.read()
    #
    if ret == False:
         print(frame)
    else:
        cv2.imshow("FrameREAD",frame)
        #print(np.shape(frame))
        out.write(frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
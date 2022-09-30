

import cv2
import numpy as np
# command used to check gstreamer:
#gst-launch-1.0 videotestsrc ! videoconvert ! appsink
gst_command = 'videotestsrc ! videoconvert ! appsink'

#integration with opencv

frame_width = 320
frame_height = 240
fps = 52.0
cap = cv2.VideoCapture(gst_command, cv2.CAP_GSTREAMER)

#gst_str = "appsrc ! queue ! videoconvert ! autovideosink"

gst_str = "appsrc ! videoconvert ! autovideosink"


#gst_str = "appsrc caps=video/x-raw,format=BGR,width=320,height=240,framerate=52.0/1  ! videoconvert ! autovideosink"


# gst_str = "appsrc " \
#             " caps=video/x-raw,format=BGR,width=320,height=240,framerate={}/1 " \
#             "! videoconvert ! video/x-raw,format=I420 " \
#             "!  jpegenc " \
#             "! rtpjpegpay " \
#             "! autovideosink".format(fps)
#            "! udpsink host=127.0.0.1 port=8080".format(fps)


out = cv2.VideoWriter(gst_str, cv2.CAP_GSTREAMER, 0, float(100), (frame_width, frame_height), True)


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
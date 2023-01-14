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

#gst_str = "appsrc ! videoconvert ! udpsink host=127.0.0.1 port=8080 "



#sender:
#gst_str = "appsrc ! videoconvert ! rtpvrawpay ! 'application/x-rtp, media=(string)video, encoding-name=(string)RAW' ! udpsink host=127.0.0.1 port=5000"

"""
recv:
gst-launch-1.0 -v udpsrc port=5000 ! 'application/x-rtp, media=(string)video, encoding-name=(string)RAW, sampling=(string)YCbCr-4:2:0, depth=(string)8, width=(string)1920, height=(string)1080, framerate=30/1' ! queue ! rtpvrawdepay ! video/x-raw, format=I420 ! xvimagesink
"""



#gst_str = "appsrc caps=video/x-raw,format=BGR,width=320,height=240  ! videoconvert ! autovideosink"




#sender:
gst_str = "appsrc ! videoconvert ! 'video/x-raw, width=340, height=240, framerate=30/1, format=I420' ! rtpvrawpay ! 'application/x-rtp, media=(string)video, encoding-name=(string)RAW' ! udpsink host=127.0.0.1 port=8080"

"""
recv:
gst-launch-1.0 -v udpsrc port=8080 ! 'application/x-rtp, media=(string)video, encoding-name=(string)RAW, sampling=(string)YCbCr-4:2:0, depth=(string)8, width=(string)1920, height=(string)1080, framerate=30/1' ! queue ! rtpvrawdepay ! video/x-raw, format=I420 ! xvimagesink
"""


out = cv2.VideoWriter(gst_str, cv2.CAP_GSTREAMER, 0, float(52), (frame_width, frame_height), True)


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
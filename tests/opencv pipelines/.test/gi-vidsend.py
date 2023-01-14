#!/usr/bin/env python3
import sys
import os
import cv2
import gi
import signal
import threading

gi.require_version('Gst', '1.0')
from gi.repository import Gst, GObject

GObject.threads_init()
Gst.init(None)
class video():
    def __init__(self):
        self.number_frames = 0
        self.fps = 10
        self.duration = 1 / self.fps * Gst.SECOND
        self.pipe = "appsrc name=source is-live=true block=true format=GST_FORMAT_TIME " \
            " caps=video/x-raw,format=BGR,width=640,height=480,framerate={}/1 " \
            "! videoconvert ! video/x-raw,format=I420 " \
            "!  jpegenc " \
            "! rtpjpegpay " \
            "! udpsink host=127.0.0.1 port=1234".format(self.fps)
        self.pipeline = Gst.parse_launch(self.pipe)
        self.loop = None
        appsrc=self.pipeline.get_by_name('source')
        appsrc.connect('need-data', self.on_need_data)
        self.cap = cv2.VideoCapture("videotestsrc " \
            "! video/x-raw,width=640,height=480,framerate={}/1 " \
            "! videoconvert ! timeoverlay ! appsink".format(self.fps))
        

    def run(self):
        self.pipeline.set_state(Gst.State.READY)
        self.pipeline.set_state(Gst.State.PLAYING)
        
        self.loop = GObject.MainLoop()
        self.loop.run()

    def on_need_data(self, src, lenght):
       if self.cap.isOpened():
            ret, frame = self.cap.read()
            if ret:
                data = frame.tostring()
                
                buf = Gst.Buffer.new_allocate(None, len(data), None)
                buf.fill(0, data)
                buf.duration = self.duration
                timestamp = self.number_frames * self.duration
                buf.pts = buf.dts = int(timestamp)
                buf.offset = timestamp
                self.number_frames += 1
                retval = src.emit('push-buffer', buf)
                print('pushed buffer, frame {}, duration {} ns, durations {} s'.format(self.number_frames,
                                                                                       self.duration,
                                                                                   self.duration / Gst.SECOND))
                print(retval)                                                                                   
                if retval != Gst.FlowReturn.OK:
                    print(retval)
                return True

        

if __name__ == "__main__":
    """
    gst-launch-1.0 -v udpsrc port=1234 \
    ! application/x-rtp, encoding-name=JPEG,payload=26 \
    ! rtpjpegdepay \
    ! jpegdec \
    ! autovideosink
    """
    v = video()
    v.run()


#gst-launch-1.0 -v udpsrc port=1234 ! application/x-rtp, encoding-name=JPEG,payload=26 ! rtpjpegdepay ! jpegdec ! autovideosink
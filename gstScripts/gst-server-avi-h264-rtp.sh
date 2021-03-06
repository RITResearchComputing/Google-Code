#!/bin/bash
#
# Script for serving an AVI containing H.264 video via RTP.
# @author Andrew Ford
# Usage: ./gst-server-avi-h264-rtp.sh [file] [destination ip] [destination port] [name]

# Destination multicast address
DEST=$2
PORT=$3
RTCPPORT=$(($3+1))

VELEM="filesrc location=$1 ! avidemux"

VSOURCE="$VELEM ! rtph264pay"

VRTPSINK="udpsink port=$PORT host=$DEST name=vrtpsink"
VRTCPSINK="udpsink port=$RTCPPORT host=$DEST sync=false async=false name=vrtcpsink"
VRTCPSRC="udpsrc port=$RTCPPORT name=vrtpsrc"
SDES="sdes-cname=$4"

gst-launch-0.10 -v gstrtpbin name=rtpbin $SDES    \
    $VSOURCE ! queue ! rtpbin.send_rtp_sink_0     \
        rtpbin.send_rtp_src_0 ! queue ! $VRTPSINK \
        rtpbin.send_rtcp_src_0 ! $VRTCPSINK       \
      $VRTCPSRC ! rtpbin.recv_rtcp_sink_0


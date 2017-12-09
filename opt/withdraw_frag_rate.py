#!/usr/bin/python
fl=open("/var/run/exabgp.in", "w")

fl.write("withdraw flow route source 10.0.0.0/8 destination 1.2.3.4/32 protocol [ udp ] fragment [ is-fragment first-fragment ] rate-limit 125000000" + '\n')

fl.flush()
fl.close

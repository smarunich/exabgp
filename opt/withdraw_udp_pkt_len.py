#!/usr/bin/python
fl=open("/var/run/exabgp.in", "w")

fl.write("withdraw flow route destination 10.10.10.10/32 protocol [ udp ] destination-port [ =19 ]  packet-length [ <128 ] discard" + '\n')

fl.flush()
fl.close

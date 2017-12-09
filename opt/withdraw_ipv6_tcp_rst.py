#!/usr/bin/python
fl=open("/var/run/exabgp.in", "w")

fl.write("withdraw flow route destination 2a02:b80:15::7aca:39ff:feae:a87a/128 next-header [ tcp ] tcp-flags [ =rst ] accept" + '\n')

fl.flush()
fl.close

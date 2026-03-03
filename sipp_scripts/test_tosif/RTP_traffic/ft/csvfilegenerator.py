#!/usr/bin/python

incr = 500
src_ext = '4000'
dst_ext = '5000'
domain = 'ci.com'
protocol = 'sip'
misc = '123'
transport = 'udp'

with open('csvfileload', 'w+') as fh:
	while incr:
		fh.write(str(src_ext)+';'+str(dst_ext)+';'+domain+';'+protocol+';'+misc+';'+transport+';'+'\n')
		src_ext = int(src_ext) + 1
		dst_ext = int(dst_ext) + 1
		incr -= 1

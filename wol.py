#!/usr/bin/env python
# -*- coding: utf-8 -*-

#http://www.emptypage.jp/gadgets/wol.htmlより

import binascii
import socket

PORT_DEFAULT = 9
IPADDR_DEFAULT = '<broadcast>'
_USAGE = """Usage:
  python wol.py [options] <MAC address>...

Options:
  -p, --port <port>
	Default port is 9
  -a, --address <IP address>
	Default IP address is '<broadcast>'
  -h, --help
	Show this help.
"""

def sendmagickpacket(macs, ipaddr=IPADDR_DEFAULT, port=PORT_DEFAULT):
	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
	for mac in macs:
		for sep in ':-':
			if sep in mac:
				mac = ''.join([x.rjust(2, '0') for x in mac.split(sep)])
				break
		mac = mac.rjust(12, '0')
		p = '\xff' * 6 + binascii.unhexlify(mac) * 16
		s.sendto(p, (ipaddr, port))
	s.close()

def main():
	import getopt
	import sys

	try:
		opt, args = getopt.getopt(sys.argv[1:], 'hp:a:', ['help', 'port=', 'address='])
	except getopt.GetoptError:
		print _USAGE
		sys.exit(2)

	if not args:
		print _USAGE
		sys.exit(2)

	port = PORT_DEFAULT
	ipaddr = IPADDR_DEFAULT
	for k, v in opt:
		if k in ('-h', '--help'):
			print _USAGE
			sys.exit()
		if k in ('-p', '--port'):
			port = int(v)
		if k in ('-a', '--address'):
			ipaddr = v

	sendmagickpacket(args, ipaddr, port)

if __name__ == '__main__':
	main()


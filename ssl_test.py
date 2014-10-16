#!/usr/bin/python
from OpenSSL import SSL
from socket import socket
import netaddr
import sys

netaddr.IPSet([])
list = netaddr.IPSet()
list.add(sys.argv[1])

context = SSL.Context(SSL.SSLv3_METHOD)
context.set_options(SSL.OP_NO_SSLv2)

for ip in list:
  try:
    sock = socket()
    ssl_sock = SSL.Connection(context, sock)
    ssl_sock.connect((str(ip), 443))
    ssl_sock.do_handshake()
    if ssl_sock.get_peer_certificate():
      cert = ssl_sock.get_peer_certificate()
      print "Successful SSLv3 Connection to: " + cert.get_subject().commonName.decode() + " Address Tested " + str(ip)
    else:
      print "connect failed"
    ssl_sock.close()
  except Exception:
    pass

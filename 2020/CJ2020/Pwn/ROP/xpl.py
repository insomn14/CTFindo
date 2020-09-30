#!/usr/bin/python

from pwn import *

host, port = 'pwn.cyber.jawara.systems', 13372

r = remote(host, port)


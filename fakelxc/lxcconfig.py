#!/usr/bin/env python
import sys

def main():
  if sys.argv[1] == 'lxc.lxcpath':
    print('/var/lib/lxc')

if __name__ == '__main__':
  main()

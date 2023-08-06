#!/usr/bin/env python

import sys
from chs.utils.core import Colors, Levels
from chs.client.runner import Client


def main():
  try:
    num = int(sys.argv[1].split('=')[1])
    level = Levels.level_of_int(num)
  except:
    level = Levels.ONE
  client = Client(level)
  client.run()

def run():
  main()
  # try:
  # except Exception as exception:
  #   print(Colors.RED + '\nUncaught error "{}", exiting the app.\n'.format(
  #     exception.__class__.__name__
  #   ))

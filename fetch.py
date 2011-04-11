#!/bin/python
import os
from subprocess import *
import config

def ls(dir = ''):
  return Popen(['svn', 'list',  trunk + dir], stdout=PIPE).communicate()[0].splitlines()

dirs = os.listdir(config.localBase)

for dir in config.splitDirs:
  dirs.remove(dir)
  dirs.extend([dir + '/' + x for x in os.listdir(config.localBase + dir)])

currentDir = os.getcwd();

for dir in dirs:
  print 'Fetching ' + dir + ' ...'
  os.chdir(currentDir)
  os.chdir(config.localBase + dir)
  Popen(['git', 'svn', 'fetch']).wait()
  Popen(['git', 'gc']).wait()

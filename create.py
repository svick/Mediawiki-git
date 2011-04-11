#!/bin/python
import sys
import os
from subprocess import *
import config

def ls(dir = ''):
  return Popen(['svn', 'list', config.trunk + dir], stdout=PIPE).communicate()[0].splitlines()

dirs = ls()

for dir in config.splitDirs:
  dirs.remove(dir + '/')
  dirs.extend([dir + '/' + x for x in ls(dir)])

currentDir = os.getcwd();

for dir in dirs:
  print 'Initializing ' + dir + ' ...'
  os.chdir(currentDir)
  os.makedirs(config.localBase + dir)
  os.chdir(config.localBase + dir)
  Popen(['git', 'svn', 'init', config.base, '-Ttrunk/' + dir, '-bbranches/*/' + dir, '-ttags/*/' + dir]).wait()

#!/bin/python
import sys
import os
from subprocess import *

base = 'http://svn.wikimedia.org/svnroot/mediawiki/'

trunk = base + 'trunk/'

splitDirs = [ 'extensions', 'tools' ]

localBase = sys.argv[1] + '/'

def ls(dir = ''):
  return Popen(['svn', 'list',  trunk + dir], stdout=PIPE).communicate()[0].splitlines()

dirs = ls()

for dir in splitDirs:
  dirs.remove(dir + '/')
  dirs.extend([dir + '/' + x for x in ls(dir)])

currentDir = os.getcwd();

for dir in dirs:
  print 'Initializing ' + dir + ' ...'
  os.chdir(currentDir)
  os.makedirs(localBase + dir)
  os.chdir(localBase + dir)
  Popen(['git', 'svn', 'init', base, '-Ttrunk/' + dir, '-bbranches/*/' + dir, '-ttags/*/' + dir]).wait()

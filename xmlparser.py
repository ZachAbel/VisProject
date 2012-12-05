#!/usr/bin/env python

import sys
from HTMLParser import HTMLParser
from htmlentitydefs import name2codepoint
import vtk
from vtk import *
import math
from math import log10

def main():
   
  meow = 'meow'
  class MyHTMLParser(HTMLParser):
     
     def __init__(self):
        HTMLParser.__init__(self)
        self.data = []     

     def handle_data(self, data):
         self.data.append(data)


  parser = MyHTMLParser()
  inputfile = str(sys.argv[1])
  
   #input/reading into a big list
  file = open(inputfile,"r")
  BigList = file.readlines()
  filewidth = len(BigList[3].split(" "))
  filelength = len(BigList)  
  print meow
  #Here we parse the xml file, unfortunately this method produces unwanted items in our list :(
  datastorelist = [] 
  n = 0
  i = 4
  while( i < filelength-2):
    if n == 1:  #skip the useless category tag
      i = i + 1
      n = n + 1
    else:  #scan the Country name, year and value
      if n == 4:
        i = i + 2
        n = 0
      else:
       parser.feed(BigList[i])
       parser.reset()
       i = i + 1
       n = n + 1

  datastorelist=parser.data
  #time to try and clean the crap out of our list, as well as adding neccesary null values
  #first, to add the null values
  n = 0
  while n < len(datastorelist)-2:
     if datastorelist[n] == '\r\n' and datastorelist[n+2] == '\r\n':
        datastorelist.insert(n+2,'0.005')
     n = n + 1
  #Then, remove the crap
  n = 0
  while n < len(datastorelist):
    if datastorelist[n] == '      ':
      del datastorelist[n]
    if datastorelist[n] == '\r\n':
      del datastorelist[n]
    else:
       n = n +1
  file.close()
  inputfile = str(sys.argv[2])

   #input/reading into a big list
  file = open(inputfile,"r")
  BigList = file.readlines()
  filewidth = len(BigList[3].split(" "))
  filelength = len(BigList)

  #Here we parse the xml file, unfortunately this method produces unwanted items in our list :(
  parser.data = []
  datastorelist1 = []
  n = 0
  i = 4
  while( i < filelength-2):
    if n == 1:  #skip the useless category tag
      i = i + 1
      n = n + 1
    else:  #scan the Country name, year and value
      if n == 4:
        i = i + 2
        n = 0
      else:
       parser.feed(BigList[i])
       parser.reset()
       i = i + 1
       n = n + 1
  
  datastorelist1=parser.data

  #time to try and clean the crap out of our list, as well as adding neccesary null values
  #first, to add the null values
  n = 0
  while n < len(datastorelist1)-2:
     if datastorelist1[n] == '\r\n' and datastorelist1[n+2] == '\r\n':
        datastorelist1.insert(n+2,'0.005')
     n = n + 1
  #Then, remove the crap
  n = 0
  while n < len(datastorelist1):
    if datastorelist1[n] == '      ':
      del datastorelist1[n]
    if datastorelist1[n] == '\r\n':
      del datastorelist1[n]
    else:
       n = n +1
  file.close()

  inputfile = str(sys.argv[3])

   #input/reading into a big list
  file = open(inputfile,"r")
  BigList = file.readlines()
  filewidth = len(BigList[3].split(" "))
  filelength = len(BigList)

  #Here we parse the xml file, unfortunately this method produces unwanted items in our list :(
  parser.data = []
  datastorelist2 = []
  n = 0
  i = 4
  while( i < filelength-2):
    if n == 1:  #skip the useless category tag
      i = i + 1
      n = n + 1
    else:  #scan the Country name, year and value
      if n == 4:
        i = i + 2
        n = 0
      else:
       parser.feed(BigList[i])
       parser.reset()
       i = i + 1
       n = n + 1
  datastorelist2=parser.data

  #time to try and clean the crap out of our list, as well as adding neccesary null values
  #first, to add the null values
  n = 0
  while n < len(datastorelist2)-2:
     if datastorelist2[n] == '\r\n' and datastorelist2[n+2] == '\r\n':
        datastorelist2.insert(n+2,'0.005')
     n = n + 1
  #Then, remove the crap
  n = 0
  while n < len(datastorelist2):
    if datastorelist2[n] == '      ':
      del datastorelist2[n]
    if datastorelist2[n] == '\r\n':
      del datastorelist2[n]
    else:
       n = n +1
  file.close()
  counter1 = 1
  print meow
  n = 0
  finaldata = []
 
  while n < len(datastorelist):
    finaldata.append(datastorelist[n])
    if counter1 == 3:
      finaldata.append(datastorelist1[n])
      finaldata.append(datastorelist2[n])
      counter1 = 0
    n = n + 1
    counter1 = counter1 + 1
  mig = [] # making three lists that store migration, investment, and gdpdeflator data exclusively
  inv = []
  gdp = [] 
  countrylist = []  
  n = 0
  counter1 = 0
  while n < len(finaldata):
    if counter1 == 0:
      countrylist.append(finaldata[n])
    if counter1 == 2:
     if float(finaldata[n]) != 0:
      gdp.append(float(finaldata[n]))
     else:
      gdp.append(0.05)
    if counter1 == 3:
     if float(finaldata[n]) != 0:
      mig.append(float(finaldata[n]))
     else:
      mig.append(0.05)
    if counter1 == 4:
     if float(finaldata[n]) != 0:
      inv.append(float(finaldata[n]))
     else:
      inv.append(0.05)
    if counter1 == 5:
      counter1 = 0 
    n = n + 1
    counter1 = counter1 + 1
#  gdp.sort()
#  mig.sort()
#  inv.sort()
#  print "GDP Biggest and littlest"+str(gdp[0])+' '+str(gdp[len(gdp)-1])
#  print "MIG Biggest and littlest"+str(mig[0])+' '+str(mig[len(mig)-1])
#  print "INV Biggest and littlest"+str(inv[0])+' '+str(inv[len(inv)-1])
  q = 0 
  n = 0 
  sumgdp = 0
  averageslist = []
  print len(gdp)
  while q < 246:
   while n < 52:
     sumgdp = sumgdp + gdp[q*52+n]
     n = n + 1
   averageslist.append(sumgdp/52)
   sumgdp = 0
   n = 0
   q = q + 1
  
  new2file = open("dataforprojectkmeans","w")
  for i in range(0,246):
       tempstring = str(averageslist[i])+'\n'
       new2file.writelines(tempstring)
  new2file.close()


  data = vtkImageData()
  data.SetExtent(0,16,0,16,0,0)
  data.SetNumberOfScalarComponents(3)
  data.SetScalarTypeToDouble()  
  data.AllocateScalars()
  x = 0
  y = 0
  z = 0 
  # POTENTIAL PROBLEM LOOP
  while x < 16:
   while y < 16:
     
     data.SetScalarComponentFromDouble(x,y,z,0,gdp[(x*16+y)*52+50]/abs(gdp[(x*16+y)*52+50])*3.2*log10(abs(gdp[(x*16+y)*52+50])))   
     data.SetScalarComponentFromDouble(x,y,z,1,mig[(x*16+y)*52+50]/abs(mig[(x*16+y)*52+50])*2.285*log10(abs(mig[(x*16+y)*52+50])))
     data.SetScalarComponentFromDouble(x,y,z,2,1.33*inv[(x*16+y)*52+50]/abs(inv[(x*16+y)*52+50])*log10(abs(inv[(x*16+y)*52+50])))
     
     if x*16+y == 245:
       y = 17
       x = 17
     y = y + 1
   x = x + 1
  data.SetSpacing(10,10,10)
  writer = vtkImageWriter()  
  writer.SetFileName("vtkVoxelGrid.vti") #for multiple files might call SetFilePrefix
  writer.SetFileDimensionality(2)
  writer.SetInput(data) 
  writer.Write()

main()

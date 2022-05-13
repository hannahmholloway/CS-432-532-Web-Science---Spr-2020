from random import random,randint
import math
import json


def main():
	input= open('rowassign','r')
	userdata = json.load(input)
	for line in userdata:
		for nline in line:
			if nline == 'ewarren':
				vec1= line[nline]
				knnestimate(userdata,vec1)



def getdistances(userdata,vec1):
  distancelist=[]

  for i in userdata:
    for nline in i:
      if nline != 'RepSeanMaloney':
        vec2= i[nline]
    
    distancelist.append((cosineDistance(vec1,vec2),i))

  distancelist.sort()
  
  return distancelist


def cosineDistance(v1,v2):
  sumxx, sumxy, sumyy = 0, 0, 0
  for i in range(0,len(v1)-1):
    x = int(v1[i]); y = int(v2[i])
    sumxx += x*x
    sumyy += y*y
    sumxy += x*y
  return sumxy/math.sqrt(sumxx*sumyy)



def knnestimate(data,vec1,k=5):
  print 'k=5'
  print "5 closest neighbours for ewarren are:"
  dlist=getdistances(data,vec1)
  avg=0.0
  # Take the average of the top k results
  for i in range(k):
    idx=dlist[i]
    value = idx[0]
    for item in idx[1]:
		username= item
    print username +'\t'+ str(value)

		
main()

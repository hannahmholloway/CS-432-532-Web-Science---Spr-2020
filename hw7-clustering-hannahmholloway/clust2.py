#!/usr/local/bin/python

import clusters

account,words,data=clusters.readfile('userdata.txt')

coordinates = clusters.scaledown(data)

clusters.draw2d(coordinates, account, jpeg='accounts.jpg')

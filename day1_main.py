# -*- coding: utf-8 -*-
"""
Created on Wed Feb  7 02:04:53 2018

@author: mhamz
"""

import day1 as a


def menu(x):
        
        a.setBackGroundColor("red")
        a.setForeGroundColor("orange")
        a.setTxt(x)
        a.setStartX(-500)
        a.setStartY(100)
        a.setFontSize(8)
        a.setSpeed(2)
        a.printData()




x=input ("Write Your Name:")
menu(x)
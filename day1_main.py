# -*- coding: utf-8 -*-
"""
Created on Wed Feb  7 02:04:53 2018

@author: mhamz
"""

from day1 import alphabets as a
import turtle

class draw (a):
    def printData(a):
        turtle.color(str(a.bg))
        turtle.setx(a.startx)
        turtle.sety(a.starty)
        turtle.speed(a.speedOfCursor)
        print(a.fg)
        print(a.bg)
        print(a.txt)
        turtle.width(int(a.font))
        turtle.bgcolor(str(a.bg))
        txtnew = str(a.txt).upper()
    
        for i in txtnew:
            if turtle.xcor() > 500:
                a.printNewLine()
            if i == 'A':
                print("inside")
                a.printA(str(a.fg))
            elif i == 'B':
                a.printB(str(a.fg))
            elif i == 'C':
                a.printC(str(a.fg))
            elif i == 'D':
                a.printD(str(a.fg))
            elif i == 'E':
                a.printE(str(a.fg))
            elif i == 'F':
                a.printF(str(a.fg))
            elif i == 'G':
                a.printG(str(a.fg))
            elif i == 'H':
                a.printH(str(a.fg))
            elif i == 'I':
                a.printI(str(a.fg))
            elif i == 'J':
                a.printJ(str(a.fg))
            elif i == 'K':
                a.printK(str(a.fg))
            elif i == 'L':
                a.printL(str(a.fg))
            elif i == 'M':
                a.printM(str(a.fg))
            elif i == 'N':
                a.printN(str(a.fg))
            elif i == 'O':
                a.printO(str(a.fg))
            elif i == 'P':
                a.printP(str(a.fg))
            elif i == 'Q':
                a.printQ(str(a.fg))
            elif i == 'R':
                a.printR(str(a.fg))
            elif i == 'S':
                a.printS(str(a.fg))
            elif i == 'T':
                a.printT(str(a.fg))
            elif i == 'U':
                a.printU(str(a.fg))
            elif i == 'V':
                a.printV(str(a.fg))
            elif i == 'W':
                a.printW(str(a.fg))
            elif i == 'X':
                a.printX(str(a.fg))
            elif i == 'Y':
                a.printY(str(a.fg))
            elif i == 'Z':
                a.printZ(str(a.fg))
            elif i == ' ':
                a.printBlank()
            a.printBlank()
    
    
        turtle.done()

draw (d1)
d1.setBackGroundColor("red")
d1.setForeGroundColor("orange")
d1.setTxt("MUHAMMAD hamza aziz")
d1.setStartX(-500)
d1.setFontSize(8)
d1.setSpeed(2)
d1.printData()

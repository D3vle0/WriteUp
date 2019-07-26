#!/usr/bin/python3

import sys
import random
import os
import time

def send(data, end='\n'):
    sys.stdout.write(data + end)
    sys.stdout.flush()

def read():
    return input()

def checkCoin():
    global dimicoin
    if dimicoin > 1000000:
        send("GoodJob!!!")
        send('-'*50)
        send(os.environ['flag'])
        send('-'*50)
        sys.exit(1)

def checkDebt():
    global debt
    global debtCount
    if debt > 0:
        if debtCount > 5:
            send("Hey! What are you doing?!?!?!")
            sys.exit(-1)
        else:
            debtCount += 1
    else:
        debtCount = 0

def changeRate():
    global rate
    if random.randint(0,1) == 0:
        rate = int(random.random() * -1 * 10) - random.randint(0, 10)
    else:
        rate = int(random.random() * 10) + random.randint(0, 10)

def changeByRate():
    global rate
    global dimicoin
    global debt

    dimicoin = dimicoin + dimicoin * (rate/100.0)
    debt = debt + debt * (rate/100.0)

def banner():
    global dimicoin
    global rate
    global debt

    send('---- Rate ----')
    if rate < 0:
        send(str(rate) + '%')
    else:
        send(str(rate) + '%')
    send('---- Coin ----')
    send(str(dimicoin) + '@')

    send('---- debt ----')
    send(str(debt) + '@')

    send("")

def menu():
    send('1. pay back')
    send('2. debt')

def payBack():
    global dimicoin
    global debt

    if debt == 0:
        send("You no have debt!")
        return

    send("How much you pay back?")
    send(":> ", end='')

    try:
        payback = int(read())
    except ValueError:
        send("Plz input int")
        return

    if payback > debt or payback > dimicoin:
        send("Too much :<")
        return

    debt -= payback
    dimicoin -= payback

def getDebt():
    global dimicoin
    global debt

    send("How much you loan?")
    send(":> ", end='')
    
    try:
        loan = int(read())
    except ValueError:
        send("Plz input int")
        return

    if loan > 10:
        send("Too much :<")
        return 

    debt += loan
    dimicoin += loan

if __name__ == '__main__':
    global dimicoin
    global rate
    global debt
    global debtCount

    send("Welcome DIMI-Bank!")
    send("Here 1@ dimi-coin")

    dimicoin = 1
    rate = 0
    debt = 0
    debtCount = 0

    time.sleep(1)

    for i in range(0,10):
        send(chr(27) + "[2J")

        checkCoin()
        checkDebt()
        changeRate()
        changeByRate()
        banner()
        send('-'*30)
        menu()
        send(':> ', end='')
        try:
            select = int(read())
            if select == 1:
                payBack()
            elif select == 2:
                getDebt()
            else:
                send("No select!")

        except ValueError:
            send("Plz input int")
        
       
    send("You get Flag? XD")

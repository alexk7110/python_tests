#!/usr/bin/python3
import datetime
from termcolor import colored
hsh = colored('*', 'blue')
tday = datetime.date.today()
mycloud = datetime.date(2015,8,22)
yoga500 = datetime.date(2015,12,15)
mate8 = datetime.date(2016,3,26)
mint = datetime.date(2016,8,29)
piserv = datetime.date(2016,11,9)
piusb = datetime.date(2017,1,10)
frmcloud = tday - mycloud
frmyoga = tday - yoga500
frommate = tday - mate8
frmmint = tday - mint
frmpisrv = tday- piserv
frmpiusb = tday - piusb
print(colored('<< ','blue'),'Uptime',colored(' >>','blue') \
        ,hsh,colored('MyCloud','green',attrs=['bold']),int(frmcloud.days/30),colored('m','white'),int(frmcloud.days%30),colored('d','white') \
        ,hsh,colored('Yoga500','green',attrs=['bold']),int(frmyoga.days/30),colored('m','white'),int(frmyoga.days%30),colored('d','white') \
        ,hsh,colored('Mate8','green',attrs=['bold']),int(frommate.days/30),colored('m','white'),int(frommate.days%30),colored('d','white') \
        ,hsh,colored('Mint','green',attrs=['bold']),int(frmmint.days/30),colored('m','white'),int(frmmint.days%30),colored('d','white') \
        ,hsh,colored('Pi3','green',attrs=['bold']),int(frmpisrv.days/30),colored('m','white'),int(frmpisrv.days%30),colored('d','white') \
        ,hsh,colored('PiUSB','green',attrs=['bold']),int(frmpiusb.days/30),colored('m','white'),int(frmpiusb.days%30),colored('d','white'))

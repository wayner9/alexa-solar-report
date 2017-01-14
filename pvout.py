#!/usr/bin/env python
import requests
import json
import datetime
import logging
from flask import Flask, render_template
from flask_ask import Ask, statement, question, session
from requests.packages.urllib3.exceptions import InsecurePlatformWarning, SNIMissingWarning
requests.packages.urllib3.disable_warnings(InsecurePlatformWarning)
requests.packages.urllib3.disable_warnings(SNIMissingWarning)

app = Flask(__name__)
ask = Ask(app, "/")

logger=logging.getLogger("flask_ask")
logger.setLevel(logging.DEBUG)
#fh=logging.FileHandler("/home/wayne/alexa/solarpv/solar_rep.log")
#fh.setLevel(logging.DEBUG)
#logger.addHandler(fh)

url_prefix='http://pvoutput.org/service/r2/'
site_id='12345'  #enter your own site ID here
api_key='1234567890abacdef1232347adfbc'  #enter your own api key here

def solar_info(fieldnum,div,deci):
	command="getstatus.jsp?"
	thisday= datetime.datetime.now()
	year=str(thisday.year)
	month=str(thisday.month).zfill(2)
	day=str(thisday.day).zfill(2)
	datestring=year+month+day
	url=url_prefix+command+"key="+api_key+"&sid="+site_id+"&d="+datestring
	data=requests.get(url)
	datalist=data.text.split(",")
	data=round(float(datalist[fieldnum])/div,deci)
	update_time=datalist[1]
	return {'data':data,'time':update_time}

def solar_history(fieldnum,datefrom,div,deci):
	command="getstatistic.jsp?"
	thisday= datetime.datetime.now()
	year=str(thisday.year)
	month=str(thisday.month).zfill(2)
	day=str(thisday.day).zfill(2)
	datestring=year+month+day
	url=url_prefix+command+"key="+api_key+"&sid="+site_id+"&df="+datefrom+"&dt="+datestring
	print url
	data=requests.get(url)
	datalist=data.text.split(",")
	print datalist
	data=round(float(datalist[fieldnum])/div,deci)
	update_time=datalist[1]
	return {'data':data,'time':update_time}

@ask.launch
def start():
    welcome_msg = 'What info would you like about my solar panels?'
    return statement(welcome_msg)

@ask.intent("DailyEnergyIntent")
def energy():
	fieldnum=2
	div=1000
	deci=1
	a=solar_info(fieldnum,div,deci)
	today_energy=a['data']
	hourmin=a['time']
	energy_msg='The energy produced as at '+hourmin+' today is '+str(today_energy)+" kilowatt hours"
	return statement(energy_msg)
    
@ask.intent("PowerIntent")
def power():
	fieldnum=3
	div=1000
	deci=0
	a=solar_info(fieldnum,div,deci)
	curr_power=a['data']
	hourmin=a['time']
	dailypower='The power produced at: '+hourmin+' is '+str(curr_power)+" kilowatts "
	return statement(dailypower)
    
@ask.intent("YearlyEnergyIntent")
def Yearlyenergy():
	fieldnum=0
	div=1000
	deci=2
	thisday= datetime.datetime.now()
	year=str(thisday.year)
	datefrom=year+"0101"	
	a=solar_history(fieldnum,datefrom,div,deci)
	yearly_energy=a['data']
	#add in code to deal with early in year when energy is just a few kWh
	if yearly_energy > 10000 :
		yearly_msg='The energy produced this year is '+str(yearly_energy/1000.0)+" megawatt hours"
	else:
		yearly_msg='The energy produced this year is '+str(yearly_energy)+" kilowatt hours"
	return statement(yearly_msg)

@ask.intent("LifetimeEnergyIntent")
def Lifetimeenergy():
	fieldnum=0
	div=1000000
	deci=2
	datefrom="20000101"
	a=solar_history(fieldnum,datefrom,div,deci)
	lifetime_energy=a['data']
	lifetime_msg='The energy produced in the life of the panels is '+str(lifetime_energy)+" megawatt hours"
	return statement(lifetime_msg)

@ask.intent("Terminate")
def Terminate():
    return statement('good bye')

if __name__ == '__main__':
	app.run(debug=True, port=5000)

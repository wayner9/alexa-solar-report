# alexa-solar-report
This project is an Amazon Alexa Skill that will respond with data abot solar panels.  Initially the project accessed the SolarEdge API, but it is being adapted to hit the PVOutput API.  This is not an official Aexa Skill that runs in the cloud - you will run this on your own PC and use a tunnel from your PC to allow Alexa.  If someone has an idea on how to set this up permanently on a cloud server while still allowing users to keep their Site ID and API keys private then I would love to be able to get this running in that way.

## Usage
"Alexa ask Solar Report what is my daily energy", "Alexa ask Solar Report for my current power production",
"Alexa ask Solar Report what is my annual energy", "Alexa ask Solar Report what is my lifetime energy"
Over time I hope to add my functionality - please feel free to contribute. Note that I only use PVOutput
for generation data due to the configuration of my panels.  My solar generation system is totally separate
from my power usage - where I live it makes financial sense to sell 100% of what you produce back to your
utility.  Note that my inverter is SolarEdge but that shouldn't matter as this Alexa Skill is solely interfacing
with PVOutput for the data.

Requires:
* flask_ask by John Wheeler (on GitHub);
* various other common python modules depending on your python install

## Notes
The Python program pvout.py contains the intent handlers required to
accept an Alexa Intent, query and post to the PVOutput API for a specific site,
and return a text response to be spoken on Alexa devices such as the Echo and Dot.

This program uses a program called ngrok to open a tunnel to your PC.
I have tried this out on Windows and on a Raspberry Pi running Raspbian- Jessie.

The following need to be entered as into the code because they contain private 
information:
* line 22 - enter your site ID;
* line 23 - enter your PVOutput API key (make sure that you use your PVOuput which is on your settings page (https://pvoutput.org/account.jsp) not the API for Weather or your Inverter.


## Key Files in this repository
Here are the most important files and what they do:
* <b>pvout.py</b> is the main Python program to handle the incoming Alexa intents, query the PVOutput API, issue commands through the API, formulate and return responses to be spoken by an Alexa device;
* <b>intents.txt</b> is the most current schema of intents, in JSON format, that defines the inquiries and commands that Alexa can pass to Nikola.  This must be copied and pasted into the "Intent Schema" section of the "Interaction Model" tab for a Nikola Skill that can be defined and managed in the Amazon Developer Console.
* <b>utterances</b> is a list of "Sample Utterances" that Alexa uses to decide which intent to send to the application.  Like the Intent Schema, this must be copied and pasted into the "Sample Utterances" section of the Interaction Model for an Alexa Skill;
## Setup and Installation
Prereqs - you should have Python installed an running on your PC.  I am using Python 2.7.
It also helps to have some knowledge of Python but that should be required.
For more background info I would suggest that you look at the following tutorial on flask-ask:
https://developer.amazon.com/blogs/post/Tx14R0IYYGH3SKT/Flask-Ask-A-New-Python-Framework-for-Rapid-Alexa-Skills-Kit-Development

Sign up for an Amazon Developer Account - you can likely use your existing Amazon credentials.

Download all of the files from this repository and place them in a folder you create on your PC.
I am assuming that you are using a folder called solarrep but that doesn't really matter.
You may have to download and install the following python package:  flask-ask.  That is
done by typing 'pip install flask-ask' or whatever.  You may have to install other python packages
if you get errors - such as logging, datetime or requests. 

Run the main python file by typing 'python pvout.py'.

Assuming the python program is working you now have your file waiting for commands
on port 5000.

The next step is to setup ngrok (https://ngrok.com/).  Download and run the version of ngrok for your
PC - on windows you will need the command 'ngrok.exe http 5000' and on Linux it is 
'./ngrok http 5000'.  You will need some info from this screen in a little while.

Sign in to the Amazon Developer Console.  Click on Alexa on the top of the screen.  Then click
on the Get Started button of the Alexa Skills Kit.  Next click on the Add a New Skill button.

On the first screen use Solar Report in both boxes.  Click Next.
On the next page copy everything from the intents.txt file and paste into the intent schema.
Copy everything from the utterances.txt file and paste into the Sample Utterances. Click next.
On the next screen for Endpoint click on HTTPS.  Pick your region.  In the box enter the https
URL from ngrok which should be the last Forwarding line.  For example if the line reads:
'Forwarding    https://ab12cd34.ngrok.io --> localost:5000' then enter this in the box.
Press Save or Next and you should now be working.

If you keep these two processes running you will be able to access this Skill continuously.

Ask Alexa for some info as in "Alexa ask Solar Report for daily energy".

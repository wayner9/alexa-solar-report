# alexa-solar-report
This project is an Amazon Alexa Skill that will respond with data abot solar panels.  Initially the project accessed the SolarEdge API, but it is being adapted to hit the PVOutput API.

Requires:
* flask_ask by John Wheeler (on GitHub);
* various other common python modules

## Notes
The Python program pvout.py contains the intent handlers required to
accept an Alexa Intent, query and post to the PVOutput API for a specific site,
and return a text response to be spoken on Alexa devices such as the Echo and Dot.

This program uses a program called ngrok to open a tunnel to your PC.
I have tried this out on Windows and on a Raspberry Pi running Raspbian- Jessie.

The following need to be entered as into the code because they contain private 
information:
* line 22 - enter your site ID;
* line 23 - enter your PVOutput API key (make sure that you use your PVOuput rather than
your inverter API);

## Key Files in this repository
Here are the most important files and what they do:
* <b>pvout.py</b> is the main Python program to handle the incoming Alexa intents, query the PVOutput API, issue commands through the API, formulate and return responses to be spoken by an Alexa device;
* <b>intents.txt</b> is the most current schema of intents, in JSON format, that defines the inquiries and commands that Alexa can pass to Nikola.  This must be copied and pasted into the "Intent Schema" section of the "Interaction Model" tab for a Nikola Skill that can be defined and managed in the Amazon Developer Console.
* <b>utterances</b> is a list of "Sample Utterances" that Alexa uses to decide which intent to send to the application.  Like the Intent Schema, this must be copied and pasted into the "Sample Utterances" section of the Interaction Model for an Alexa Skill;

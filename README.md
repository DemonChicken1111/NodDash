# **NodDash**
 A Python backend utility for smart deployables in [Project Awakening](https://phase3.projectawakening.io/).

 </br>
 </br>
 </br>

 <p style="text-align: center"><img src="https://harbor-webapp.s3.us-east-2.amazonaws.com/projects/6/global/logo.png"></p>
 
 </br>

 ## **FEATURES**

 NodDash is a fully featured activity and data collection backend which utilizes the JSON API provided by Projects Awakening Dev team. You can use NodDash to find your next kill, monitor selling data, or other various stats on any smart deployable in Project Awakening. NodDash is very configurable and code changes are encouraged for users who wish to expand functionality or cutomization.

 NodDash is intended for use on SBC's like Raspberry Pi's, However, it will work on anything with a python interpreter and an internet connection. If you would like to test or mess around with the project virtualization is encouraged if hardware is unavailible. If you would like to virtualize you can read our [virtualization docs](Docs/Virtualization.md), otherwise if you're experienced or have an enviroment already setup you can read the [installation and deployment section](https://github.com/DemonChicken1111/Python-Backend-For-PA?tab=readme-ov-file#installation-and-deployment)

 ### Current Functionality:

 - JSON API importing
 - Activity monitoring 
 - User configurable data extraction
 - Fully user controlled
 - Easy to use custom databases
 - Data visualization framework
 - CLI 
 - Hardware flexibility


# **INSTALLATION AND DEPLOYMENT**

 ### Requirements

 Python 3 and pip are required and can be downloaded [here](https://www.python.org/downloads/)

 If you are on linux you can download python and pip via your package manger in the terminal

 There is no storage requirements however if you are going to be running this for an extended period of time I would consider having a good amount of free storage.. You can also edit `Cleanup.py` and how often it runs in `main.py` if you need. 

 ### Clone or Download the repository

 You can download the lastest release at the [release pages](https://github.com/DemonChicken1111/NodDash/releases)

 ### Installing on Windows 

 Find the zipped release and unpack it. Then open up a cmd prompt and put in the following commands

 ```
cd PathToUnzippedRelease
pip install -r requirements.txt
 ```

 ### Installling on Linux

 Unpack the zipped release and in the terminal put in the following commands

 ```
 cd PathToUnzippedRelease
 pip install -r requirements.txt
 ```

 ### Configuration 

 There are two configuration files provided within the release with test values inside them. config.yaml and configMonitor.yaml control how NodDash behaves.

 config.yaml handles which smart deployable ID's will be used by the system. You can follow the convention in the file but if you're in doubt here is the layout of an example config.

 ```
  ---
  deployables:
  	One: "ID"
  	Two: "ID 2"
  	Three: "ID 3"
 ```

 configMonitor.yaml controls which values in the JSON API are compared for changes. Any key value can be used here. However it is important that you do not use nested key values as it will not be able to see them. The format is the same as the last, however the first key is `keyvalues` instead of `deployables`

 The third configuration option is coding, you can freely change code, add features, and tinker around with more capabilities or graph types in the source. However I would highly recommend creating a fork and contributing to the project if that is the case. Of course it is not required but who doesn't love open source projects!

 ### Deploying

 Now that NodDash is installed, configured, and dependancies are taken care of it's time to finally deploy it. Open up cmd or a terminal and enter the following

 ```
 cd PathToNodDash
 python3 main.py
 ```
 
 Once that is run you should be good to go! NodDash should pop up and it's processes should commence. Now you can have fun monitoring Project Awakenings Smart Deployables!

# SUBMITTING ISSUES

 If you are having an issue with NodDash please submit an issue. In this issue provide:

 - Errors
 - Any configuration changes
 - Any code changes 
 - Steps to reproduce if applicable

# TO-DO LIST

- [x] JSONImporting
- [x] Activity Monioring 
	- [x] Integrate logging of updates
- [x] UI
	- [x] Convert to CLI
- [x] Logging data (Basic)
- [x] Grabbing and storing data
	- [x] Deleting old files
- [ ] ~~Creating user supplied database (Might not completet)~~
	- [x] Pings sent to seperate db in monitor
	- [x] Graphing data from db's __(Or framework for furthur development)__
- [x] Configuration Options / Easy code changes
- [x] Dependancy setup script
- [ ] Presentation + Docs
- [x] Make release 

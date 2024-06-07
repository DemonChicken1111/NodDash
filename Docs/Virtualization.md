# **Virtualization**


## Installing VirtualBox

 You can install VirtualBox [here](https://www.virtualbox.org/wiki/Downloads) and follow their install process

## Installing an ISO

 Once you install VirtualBox we can get an image for our desired OS. For this guide we will be using [RaspianOS](https://www.raspberrypi.com/software/raspberry-pi-desktop/) to emulate the experience on hardware. Once installed you can move on to the next step

## Creating the virtual machine 

 In VirtualBox navigate to *Machine --> New*

 ![New Machine](Docs/NewMachine.PNG)

 Enter desired name, folder location, and then find the ISO we downloaded in the pervious step. Then click on next

 ![Setup](Docs/NewMachine.PNG)

 create your user and password, give the machine 4 cores and 4-8 GB of RAM, then allocate your desired harddrive space, for long term testing make sure you give the VM a decent amount of storage. You can then start up the machine and go through the install process!

## Installing NodDash

 To prepare the machine we first need to install a couple of things, which can be done with the following commands:

 ```
 sudo apt-get update
 sudo apt-get install git python3 
 ```

 Let these install, and when they're done you can move on the install instructions in the [readme file.](README.md)
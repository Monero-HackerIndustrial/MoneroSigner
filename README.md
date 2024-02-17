# This is an experimental project still being developed. 

# Build an offline, airgapped Monero signing device for less than $50!
## This started as a monero fork of the OG seedsigner  https://github.com/SeedSigner/seedsigner but is now considdered a completely seperate and independent code base

---------------

* [Project Summary](#project-summary)
* [Shopping List](#shopping-list)
* [Manual Installation Instructions](#manual-installation-instructions)


---------------

# Project Summary
The project aims to make it easy for anybody to make a dedicated offline signing device out of low-cost commodity computer components (raspberry pi zero). This helps in reducing the need to trust hardware verndors. The most private hardware wallet, is the only only **you** know about.

Supplychain poses a significant attack vector to hardware manufacturers, this threat is exacerbated when dealing with cryptocurrency devices. Monerosigner offers a DIY hardware wallet built out of easy* to source over the counter general hobbyist parts. This makes it easier for users to self custody their keys on their own devices.


Additional information about the project can be found at [seedsigner.com](https://monerosigner.com).

You can follow [@MoneroSigner](https://twitter.com/MoneroSigner) on Twitter for the latest project news and developments.

If you have specific questions about the project please reaach out via twitter DM, Github issues.

### Feature Highlights:
* Generate seed from dice rolls
* Generate seed from mnemonic phrase
* Import seed from QR code
* Generate Addresses from accounts
* Load unsigned transactions via QR
* Sign unsigned transactions
* Upload signed transactions to companion app via QR codes
* Generate view only wallet & Export

### [Monerosigner companion application (Desktop)](https://github.com/Monero-HackerIndustrial/MoneroSigner-Companion):

* Transfer unsigned transactions via QR code
* Transfer signed transactions and upload to network

### [PortableMoneroQR](https://github.com/Monero-HackerIndustrial/PortableMoneroQR):

* Data transfer standard for QR codes with a focus on lower end cameras and screens
* Variable data sizes with different frame rates
* Application agnostic


### Considerations:
* Built for compatibility with monerosigner companion app.
* Device takes up to 60 seconds to boot before menu appears (be patient!)
* Always test your setup before transfering larger amounts of Monero
* Slightly rotating the screen clockwise or counter-clockwise should resolve lighting/glare issues
* If you think SeedSigner adds value to the Monero ecosystem, please help us spread the word! (tweets, pics, videos, etc.)

### Planned Upcoming Improvements / Functionality:
*** This is still a work in progress. Once a stable version is out I can proceed
to add more features ***

---------------

# Shopping List

To build a MoneroSigner, you will need:

* Raspberry Pi Zero (preferably version 1.3 with no WiFi/Bluetooth capability, but any Raspberry Pi 2/3/4 or Zero model will work, Raspberry Pi 1 devices will require a hardware modification to the Waveshare LCD Hat, as per the [instructions here](./docs/legacy_hardware.md))
* Waveshare 1.3" 240x240 pxl LCD (correct pixel count is important, more info at https://www.waveshare.com/wiki/1.3inch_LCD_HAT)
* Pi Zero-compatible camera (tested to work with the Aokin / AuviPal 5MP 1080p with OV5647 Sensor)

Notes:
* You will need to solder the 40 GPIO pins (20 pins per row) to the Raspberry Pi Zero board. If you don't want to solder, purchase "GPIO Hammer Headers" for a solderless experience.
* Other cameras with the above sensor module should work, but may not fit in the Orange Pill enclosure
* Choose the Waveshare screen carefully; make sure to purchase the model that has a resolution of 240x240 pixels

---------------

# manual installation instructions

**This is for developer use only atm**
The current setup assumes you are a developer and as such as enable an ssh server. This is done to help enable a developemnt enviroment from a remote ssh session. 
This is done to help developers quickly test and restest new changes without requiring reflashing the sd card. For obvious reasons this should not be used to protect real funds as a production build
would not have networking enabled nor an ssh server (especially one locked down with a simple user:pass) 

The developer instructions assume you are using a raspberry pi model other than a zero. I chosse to develop on a raspberry pi instead of a pi zero because of the hardwired ethernet cable. 

The manual installation is different than seedsigner. Developer builds target rasbian based on ddebian version 12.0 (codenamed bookworm). 

## 1. Download Pi OS lite from the rasbian images.
https://downloads.raspberrypi.com/raspios_lite_armhf/images/raspios_lite_armhf-2023-12-11/2023-12-11-raspios-bookworm-armhf-lite.img.xz
Raspberry Pi OS Lite
Release date: December 11th 2023
System: 32-bit
Kernel version: 6.1
Debian version: 12 (bookworm)
sha256sum: 5df1850573c5e1418f70285c96deea2cfa87105cca976262f023c49b31cdd52b  2023-12-11-raspios-bookworm-armhf-lite.img.xz

## 2. Install the image to an sd card 
Us your prefered application such as DD or Disks utility to write the image to the sd card. (This will overide the whole sd card)

## 3. (For remote dev) Enable and configure SSH server 

Create a blank ```ssh``` file in the boot partion of your sd card. This enables the ssh server on your pi. 

Next you need to create a user password for the user. (By default there is no password set for the pi user. Without a password ssh can't log in). 
Instructions taken from here: 
https://www.raspberrypi.com/documentation/computers/configuration.html#configuring-a-user
**Configure a user manually**
At the root of your SD card, create a file named userconf.txt.

This file should contain a single line of text, consisting of <username>:<password>: your desired username, followed immediately by a colon, followed immediately by an encrypted representation of the password you want to use.


For example. If you want to use the password ```raspberry``` for the user pi you would run the following command 
```echo 'raspberry' | openssl passwd -6 -stdin``` 
Our example output: ```$6$HdV3bbnqr0hwKEfI$h3kjQVvgLeNz24kr5n4LFq9eMsnJ1H0QRCgnUrYolZWnSIj.aqK9wLKj3fJNn0jaL9VMiXbI9oH8vbhgoTeRK1``` (keep in mind that running the command again would give you a different string because of the random salt added)
Then we would take that output and insert it into the serconf.txt ```<password>``` placeholder. 
The userconf.txt file would look like so: 

```pi:$6$HdV3bbnqr0hwKEfI$h3kjQVvgLeNz24kr5n4LFq9eMsnJ1H0QRCgnUrYolZWnSIj.aqK9wLKj3fJNn0jaL9VMiXbI9oH8vbhgoTeRK1```
### 4. Updates and dependencies 
once you ssh onto the box pleas run these coommands:
```
sudo apt-get update
sudo apt-get upgrade
```
You might need to enable the spi inteface through raspi-config:
Type : ```sudo raspi-config```
Use the menu to go to : Inerface Options -> SPI -> Enable (It asks you if you want to enable. Select "yes"). 


Raspberry Pi OS Bullseye and later images by default run the libcamera camera stack, which is required for Picamera2.
You can check that libcamera is working by opening a command window and typing:

```rpicam-hello```
You will get text output from your camera in the terminal. If you get an error your camera physical connection might not be connected or you might need to troubleshoot the hardware. 

### 5. Install required python packages 

```
sudo apt-get install python3-pip
sudo apt-get install python3-pil
sudo apt-get install python3-numpy
sudo pip3 install spidev
```
### 6. Clone the repository to the pi 

``` git clone https://github.com/Monero-HackerIndustrial/MoneroSigner```





2. 
3. 
4.   https://downloads.raspberrypi.com/raspios_lite_armhf/release_notes.txt


5. 
6. https://downloads.raspberrypi.com/raspios_lite_armhf/release_notes.txt

---

---

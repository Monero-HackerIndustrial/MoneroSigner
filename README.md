# This is an experimental project still being developed. 

# Build an offline, airgapped Monero signing device for less than $50!
## This started as a monero fork of the OG seedsigner  https://github.com/SeedSigner/seedsigner but is now considdered a completely seperate and independent code base

---------------

* [Project Summary](#project-summary)
* [Shopping List](#shopping-list)
* [Software Installation](#software-installation)
  * [Verifying the Software](#verifying-the-software)
* [Enclosure Designs](#enclosure-designs)
* [SeedQR Printable Templates](#seedqr-printable-templates)
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

---

---

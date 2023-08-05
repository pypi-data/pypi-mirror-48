# way2smswrapper
<p>
  <img src="https://img.shields.io/badge/version-0.1.2-blue.svg?cacheSeconds=2592000" />
  <a href="https://github.com/probhakarroy/way2smswrapper#readme">
    <img alt="Documentation" src="https://img.shields.io/badge/documentation-yes-brightgreen.svg" target="_blank" />
  </a>
  <a href="https://github.com/probhakarroy/way2smswrapper/graphs/commit-activity">
    <img alt="Maintenance" src="https://img.shields.io/badge/Maintained%3F-yes-green.svg" target="_blank" />
  </a>
  <a href="https://github.com/probhakarroy/way2smswrapper/blob/master/LICENSE">
    <img alt="License: MIT" src="https://img.shields.io/badge/License-MIT-yellow.svg" target="_blank" />
  </a>
</p>

> A Python Messaging Module Using Way2SMS & Selenium Module.  
> Created By $implic@

## Install
```sh
$pip install way2smswrapper
```

Requirements :-

               Python3.
               Firefox Browser. 
               Geckodriver. 
               Xvfb - Installation. 
               Way2SMS Account.

The python module uses selenium module to control the firefox browser which is being controlled by geckodriver.
The module is using xvfb(x-virtual frame buffer) and the xvfb wrapper for python3 to run the firefox browser 
headlessly(in the background). Way2SMS Account is being used to send the message to the desired mobile number.

One can import the module in his/her own python3 program to send the status of the current running program to 
the user's mobile phone number through sms using the user's Way2SMS Account.

## Usage   :-
```sh          
import w2swrapper
```

## Methods : 
```sh          
wrapper.login()
wrapper.sms('Message')
```

Tested In Ubuntu-17.04

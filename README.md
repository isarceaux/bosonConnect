# Full setup protocole of the Boson with BosonSDK on Jetson

## Install the last BosonSDK

Download the SD from this page https://www.flir.co.uk/oem/thermal-integration-made-easy/software-integration---boson/

I personally opted for the version 3.0.

Copy and rename the last folder enclosing everything in your working directory. Rename the folder BosonSDK.

In my case the working directory is the following:
/home/isabelle/Documents/

Then you need to install the BosonSDK package into your python3 package library so that you can simply import it. We are doing so by creating a symbolic link:
ln -s /home/isabelle/Documents/BosonSDK /usr/lib/python3.8/site-packages/BosonSDK

If you want to find your own location for Python package (mine is /usr/lib/python3.8/site-packages/BosonSDK) you can use the following command in python:
import sys
print(sys.path)

From now on you can use import in console mode or even in your IDE (I use PyCharm and it recognised the package).

Hence at the beginning of my code I have 
from BosonSDK import *

However if you just do this it will not be working yet, you need to make the package. To do so navigate to your package library (in my case /usr/lib/python3.8/site-packages/BosonSDK).

Then go into the folderFSLP_Files and try “make all”.

You might get an m64 error here, in that case just edit the Makefile and delete all the -m64 parameters in the file.

## Install other packages
Next step you need to install the serial package from Python: pip3 install serial.
Then use “import serial” at the beginning of your code.

## Finding the right port for your Boson
In the little bit of code to connect to the Boson we need to know the port name of the Boson, which apparently could be in the manual (that I lost).

But I found another way to find it. Just unplug and replug the Boson then do :

dmesg | grep tty 

The last one should be the right port!

Code to connect

We can now connect to the Boson with the code attached in main here.

Enjoy !


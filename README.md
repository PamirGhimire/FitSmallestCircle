Find the smallest circle around a cluster of points in 2D

By default, a random number of random points are generated with each call of the script (25 to 60 points, x and y in range -15.0 to +15.0). The circle is defined with a center point (consisting of a X and a Y coordinate) and a radius, which are printed as outputs when you execute 'start.py'. All points are within this circle, and the radius of this circle is as small as possible.

The output results are plotted on a 2D plane, with all points and the computed circle. Example points are available in 'TestData.json' and can be used for testing the implementation through a command line option.


Sample output for stub data using external implementation: <br>
![Sample output for stub data using external implementation](sampleOutput.jpg)


Environment: <br>
It is assumed that python (version>=3.6.9) and pip (version>=20.2.3) <br>
Linux: <br>
$ python3 -m pip install virtualenv <br>
$ python3 -m virtualenv circleEnv -p python3 <br>
$ source circleEnv/bin/activate <br>
(circleEnv)$ pip install matplotlib <br>
*this implementation was tested on Ubuntu18.04 with python 3.6.9, matplotlib==3.3.2 <br>

Windows: <br>
make sure that python3 is installed, check using $ python3 --version <br>
pip should be installed by default with python3 on Windows (look for pip.exe at YourPythonInstallDir/Scripts/) <br>
c:..\> python3 -m pip install virtualenv <br>
c:..\> python3 -m virtualenv circleEnv -p python3 <br>
c:..\> circleEnv\Scripts\activate.bat <br>
(circleEnv)c:..\> pip install matplotlib <br>
*this implementation was tested on Windows10 with python 3.8, 3.7.9 and matplotlib==3.3.2 <br>

Usage: <br>
(circleEnv)$ python3 start.py --useStubData <true/false> --useExternalImpl <true/false> <br>
if --useStubData true is specified, circle is fitted to points specified in 'TestData.json', else, random points are generated as described above, and the smallest circle is fitted to the same <br>

if --useExternalImpl true is specified, an algorithm from a freely available third party source is used for fitting the smallest circle, else, a naive almost-correct custom implementation is used<br>

Tests: <br>
(circleEnv)$ python3 Tests.py -v <br>
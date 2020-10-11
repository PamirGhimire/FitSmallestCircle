Find the smallest circle around a cluster of points in 2D

By default, a random number of random points are generated with each call of the script (25 to 60 points, x and y in range -15.0 to +15.0). The circle is defined with a center point (consisting of a X and a Y coordinate) and a radius, which are printed as outputs when you execute 'start.py'. All points are within this circle, and the radius of this circle is as small as possible.

The output results are plotted on a 2D plane, with all points and the computed circle. Example points are available in 'TestData.csv' and can be used for testing the implementation through a command line option.


Environment:
It is assumed that python (version>=3.6.9) and pip (version>=20.2.3) are installed
$ sudo apt install virtualenv
$ virtualenv circleEnv -p python3
$ source circleEnv/bin/activate
$ pip install matplotlib==3.3.2


Usage:
python --useStubData <true/false> --useExternalImpl <true/false> 
if --useStubData true is specified, circle is fitted to points specified in 'TestData.csv', else, random points are generated as described above

if --useExternalImpl true is specified, an algorithm from a freely available third party source is used for fitting the smallest circle, else, a naive almost-correct custom implementation is used
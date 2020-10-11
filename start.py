import sys, getopt

from DataGenerator import Random2DPointsSetGenerator
from FitCircle import FitCircleTo2DPoints
from Visualization import CreateFigure, OpenSavedFigure

def _parseArgs(argv):
    useStubData = False
    useExternalImpl = True

    stubArg = ""
    implArg = ""
    try:
        opts, args = getopt.getopt(argv,"hi:o:",["useStubData=","useExternalImpl="])
    except getopt.GetoptError:
        print ('usage : start.py --useStubData <true/false> --useExternalImpl <true/false>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print ('usage : start.py --useStubData <true/false> --useExternalImpl <true/false>')
            sys.exit()
        elif opt in ("--useStubData"):
            stubArg = arg
        elif opt in ("--useExternalImpl"):
            implArg = arg

    validArgs = ["true", "false", ""]
    if(stubArg in validArgs and implArg in validArgs):
        if stubArg=="true":
            useStubData = True
        if implArg=="false":
            useExternalImpl = False        
    else:
        print ('usage : start.py --useStubData <true/false> --useExternalImpl <true/false>')
        sys.exit(2)

    return useStubData, useExternalImpl

def main(argv):
    useStubData, useExternalImpl = _parseArgs(argv)
    
    randomPointsGenerator = Random2DPointsSetGenerator(stub=useStubData)
    randomPoints = randomPointsGenerator.Generate()
    radius, center = FitCircleTo2DPoints(randomPoints, useExternalImpl=useExternalImpl)
    print("radius = ", round(radius, 2), ", center = ", center)

    CreateFigure(randomPoints, center, radius) #saves figure to disk by default as FitCircle.png
    OpenSavedFigure()

if __name__ == '__main__':
    main(sys.argv[1:])
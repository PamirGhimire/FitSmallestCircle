import sys

from CLIHelper import _parseArgs
from DataGenerator import Random2DPointsSetGenerator
from Circle import FitCircleTo2DPoints
from Visualization import CreateFigure, OpenSavedFigure


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
from DataGenerator import Random2DPointsSetGenerator
from FitCircle import FitCircleTo2DPoints
from Visualization import CreateFigure, OpenSavedFigure

def main():
    randomPointsGenerator = Random2DPointsSetGenerator(stub=False)
    randomPoints = randomPointsGenerator.Generate()
    radius, center = FitCircleTo2DPoints(randomPoints, useExternalImpl=True)
    print("radius = ", round(radius, 2), ", center = ", center)

    CreateFigure(randomPoints, center, radius) #saves figure to disk by default as FitCircle.png
    OpenSavedFigure()

if __name__ == '__main__':
    main()
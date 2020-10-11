import sys
import subprocess
import matplotlib.pyplot as plt

from DataGenerator import Random2DPointsSetGenerator
from FitCircle import FitCircleTo2DPoints

DefaultFigureName = "FitCircle.png"

def OpenSavedFigure(filename=DefaultFigureName):
    if sys.platform == "win32":
        os.startfile(filename)
    else:
        graphicsProgram = "open" if sys.platform == "darwin" else "xdg-open"
        subprocess.call([graphicsProgram, filename])

def CreateFigure(randomPoints, center, radius, filename=DefaultFigureName):
    #setup canvas
    figure, axes = plt.subplots()
    scale = 1.3
    plt.xlim(-center.x-scale*radius, center.x+scale*radius)
    plt.ylim(-center.y-scale*radius, center.y+scale*radius)
    
    #scatter plot random points
    for point in randomPoints:
        plt.scatter(point.x, point.y, color='black', marker='o')
    #plot center
    plt.scatter(center.x, center.y, color='blue', marker='x')
    #draw circle
    circle = plt.Circle((center.x, center.y), radius, color='blue', fill=False)
    axes.add_artist(circle)

    #save figure to disk
    plt.grid()
    axes.set_aspect(1)
    plt.savefig(DefaultFigureName)


def main():
    randomPointsGenerator = Random2DPointsSetGenerator(stub=False)
    randomPoints = randomPointsGenerator.Generate()
    radius, center = FitCircleTo2DPoints(randomPoints, useExternalImpl=True)
    print("radius = ", round(radius, 2), ", center = ", center)

    CreateFigure(randomPoints, center, radius)
    OpenSavedFigure()

if __name__ == '__main__':
    main()
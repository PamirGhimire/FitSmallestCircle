import os, sys
import subprocess
import matplotlib.pyplot as plt

from typing import List
from Point2D import Point2D

DefaultFigureName = "FitCircle.png"

def OpenSavedFigure(filename:str=DefaultFigureName):
    if sys.platform == "win32":
        os.startfile(filename)
    else:
        linuxOsCommand = "open" if sys.platform == "darwin" else "xdg-open"
        subprocess.call([linuxOsCommand, filename])

def CreateFigure(randomPoints:List[Point2D], center:Point2D, radius:float, filename:str=DefaultFigureName):
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
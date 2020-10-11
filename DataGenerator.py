import random, csv
from Point2D import Point2D, RandomPoint2D

class Random2DPointsSetGenerator:
    STUBDATAFILEPATH="TestData.csv"
    def __init__(self, nPointsMin=25, nPointsMax=60, xmin=-15, xmax=15, ymin=-15, ymax=15, stub=False):
        kwargs = locals()
        self.stub = stub
        # check that all input args are numeric, and if so, set them as attributes
        for argName, argVal in kwargs.items():
            if not (argName=="self" or argName=="stub"):
                if not Point2D.IsNumeric(argVal):
                    raise TypeError("All args must be numeric, " + argName + " is " + str(type(argVal)))
                setattr(self, argName, argVal)

    def Generate(self):
        if (self.stub):
            return Random2DPointsSetGenerator.GetStubDataFromFile(Random2DPointsSetGenerator.STUBDATAFILEPATH)

        nPoints = random.randint(self.nPointsMin, self.nPointsMax)
        points = set() #filter duplicate points
        while len(points) < nPoints:
            points.add(RandomPoint2D())
        return list(points)

    @staticmethod
    def GetStubDataFromFile(filepath):
        """
        Expected format in csv file:
        x1, y1
        x2, y2
        ...
        """
        if (filepath.split(".")[-1] != "csv"):
            raise ValueError("Expected csv filetype")
        points = set() #filter duplicate points
        with open(filepath) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            for row in csv_reader:
                points.add( Point2D(float(row[0]), float(row[1])) )
        return list(points)
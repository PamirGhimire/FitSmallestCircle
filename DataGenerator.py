import random, json
from Point2D import Point2D, RandomPoint2D

class Random2DPointsSetGenerator:
    STUBDATAFILEPATH="TestData.json"
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
        Expected format in json file:
        [
        {"x":x1, "y":y1},
        ...
        {"x":xN, "y":yN}
        ]
        """
        if (filepath.split(".")[-1] != "json"):
            raise ValueError("Expected json filetype")
        points = set() #filter duplicate points
        with open(filepath) as json_file:
            testPoints = json.load(json_file)
            for point in testPoints:
                points.add(Point2D(point["x"], point["y"]))
        return list(points)
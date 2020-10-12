import unittest, json, random, math
from DataGenerator import Random2DPointsSetGenerator
from Circle import FitCircleTo2DPoints, Circle
from Point2D import Point2D

MaxTestIter = 1000

class TestSuiteSmallestCircleFitting(unittest.TestCase):
    def test_PointInCircleMethod(self):
        r = 7
        c = Point2D(3, 5)
        circle = Circle(radius=r, center=c)

        # points inside circle
        for testIter in range(int(MaxTestIter/2)):
            rad = random.uniform(0, r)
            theta = random.uniform(0, 2*math.pi)
            x = c.x + rad*math.cos(theta)
            y = c.y + rad*math.sin(theta)
            if not circle.ContainsPoint(Point2D(x, y)):
                print(Point2D(x, y))
            self.assertTrue(circle.ContainsPoint(Point2D(x, y)))

        # points outside circle
        for testIter in range(int(MaxTestIter/2)):
            rad = r + random.uniform(Point2D.COMPARISONPRECISION, 100)
            theta = random.uniform(0, 2*math.pi)
            x = c.x + rad*math.cos(theta)
            y = c.y + rad*math.sin(theta)
            self.assertFalse(circle.ContainsPoint(Point2D(x, y)))


    def test_Random2DPointsGeneratedAsSpecified(self):
        generator = Random2DPointsSetGenerator(nPointsMin=25, nPointsMax=60, xmin=-15, xmax=15, ymin=-15, ymax=15, stub=False)        
        for testIter in range(MaxTestIter):
            randomPoints = generator.Generate()
            # there are between 25 and 60 points are generated
            self.assertTrue(25 <= len(randomPoints) <= 60)
            # all points have -15 <= x/y <= +15
            for point in randomPoints:
                self.assertTrue(-15 <= point.x <= 15)
                self.assertTrue(-15 <= point.y <= 15)

    def test_GettingStubDataFromRandom2DPointsGenerator(self):
        generator = Random2DPointsSetGenerator(stub=True)        
        generatedPoints = generator.Generate()

        #read stub data json
        points = set() #filter duplicate points
        with open("TestData.json") as json_file:
            testPoints = json.load(json_file)
            for point in testPoints:
                points.add(Point2D(point["x"], point["y"]))
        stubPoints = list(points)

        self.assertEqual(len(generatedPoints), len(stubPoints))
        for n in range(len(generatedPoints)):
            self.assertEqual(generatedPoints[n], stubPoints[n])

    def test_FitSmallestCircleExternalImpl(self):
        generator = Random2DPointsSetGenerator(nPointsMin=25, nPointsMax=60, xmin=-15, xmax=15, ymin=-15, ymax=15, stub=False)        
        for testIter in range(MaxTestIter):
            randomPoints = generator.Generate()
            radius, center = FitCircleTo2DPoints(randomPoints, useExternalImpl=True)
            circle = Circle(radius, center)
            
            #all random points must be inside the circle or on its perimeter
            for point in randomPoints:
                self.assertTrue(circle.ContainsPoint(point))

    def test_FitSmallestCircleCustomImpl(self):
        generator = Random2DPointsSetGenerator(nPointsMin=25, nPointsMax=60, xmin=-15, xmax=15, ymin=-15, ymax=15, stub=False)        
        for testIter in range(MaxTestIter):
            randomPoints = generator.Generate()
            radius, center = FitCircleTo2DPoints(randomPoints, useExternalImpl=False)
            circle = Circle(radius, center)

            radiusExt, centerExt = FitCircleTo2DPoints(randomPoints, useExternalImpl=True)
            
            #all random points must be inside the circle or on its perimeter, externalRadius <= customRadius
            for point in randomPoints:
                self.assertTrue(circle.ContainsPoint(point))
                self.assertTrue(radiusExt <= radius)

if __name__ == '__main__':
    unittest.main()
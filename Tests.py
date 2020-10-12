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
            rad = r + random.uniform(Point2D.COMPARISONTOLERANCE, 100)
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
        euclideanDist = lambda p1, p2 : pow(pow(p1.x-p2.x, 2) + pow(p1.y-p2.y, 2), 0.5)

        for testIter in range(MaxTestIter):
            randomPoints = generator.Generate()
            radius, center = FitCircleTo2DPoints(randomPoints, useExternalImpl=True)
            circle = Circle(radius, center)
            
            nRandomPointsOnPerimeter = 0
            #all random points must be inside the circle or on its perimeter
            for point in randomPoints:
                self.assertTrue(circle.ContainsPoint(point))
                if abs(euclideanDist(point, center) - radius) <= Point2D.COMPARISONTOLERANCE:
                    nRandomPointsOnPerimeter += 1
            #at least 2 points must be on the perimeter of the circle
            self.assertTrue(nRandomPointsOnPerimeter >= 2)

    def test_FitSmallestCircleCustomImpl(self):
        generator = Random2DPointsSetGenerator(nPointsMin=25, nPointsMax=60, xmin=-15, xmax=15, ymin=-15, ymax=15, stub=False)        
        for testIter in range(MaxTestIter):
            randomPoints = generator.Generate()
            radius, center = FitCircleTo2DPoints(randomPoints, useExternalImpl=False)
            circle = Circle(radius, center)

            radiusExt, centerExt = FitCircleTo2DPoints(randomPoints, useExternalImpl=True)
            
            #all random points must be inside the circle or on its perimeter
            for point in randomPoints:
                self.assertTrue(circle.ContainsPoint(point))

            #radius from custom impl. is often slightly larger than one from external impl., 
            #but sometimes, they are nearly identical
            if not radiusExt <= radius:
                print("\nFor a random set of " + str(len(randomPoints)) + " points :")
                print("radius, center from external impl. " + str(round(radiusExt, 4)) + ", " + str(centerExt))
                print("radius, center from custom impl. " + str(round(radius, 4)) + ", " + str(center))
            self.assertTrue(radiusExt < radius+Point2D.COMPARISONTOLERANCE)

if __name__ == '__main__':
    unittest.main()
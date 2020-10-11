class Point2D:
    PRINTPRECISION=2 #print till this decimal place
    COMPARISONPRECISION=2 #compare till this decimal place
    COMPARISONTOLERANCE=pow(10, -COMPARISONPRECISION)

    def __init__(self, x, y):
        if(Point2D.IsNumeric(x) and Point2D.IsNumeric(y)):
            self.x = x
            self.y = y
        else:
            raise TypeError("x and y must be numbers, got " + str(type(x)) + ", " + str(type(y)))

    def __str__(self):
        return str(round(self.x, Point2D.PRINTPRECISION)) + ","+ str(round(self.y, Point2D.PRINTPRECISION))

    def __eq__(self, other):
        areCLose = lambda f1, f2 : abs(f1-f2) < Point2D.COMPARISONTOLERANCE*max(abs(f1),abs(f2))
        return areCLose(self.x, other.x) and areCLose(self.y, other.y)

    def __ne__(self, other):
        areNotCLose = lambda f1, f2 : abs(f1-f2) > Point2D.COMPARISONTOLERANCE*max(abs(f1),abs(f2))
        return areNotCLose(self.x, other.x) or areNotCLose(self.y, other.y)

    def __hash__(self):
        return hash(round(self.x, Point2D.COMPARISONPRECISION))^hash(round(self.y, Point2D.COMPARISONPRECISION))


    @staticmethod
    def IsNumeric(n):
        if isinstance(n, int) or isinstance(n, float):
            return True
        return False

import random
class RandomPoint2D(Point2D):
    # initialize random number generator to get same sequence of 'random' points each time 
    # random.seed(1)

    def __init__(self, xmin=-15.0, xmax=15.0, ymin=-15.0, ymax=15.0):
        numcheck = Point2D.IsNumeric
        if (not (numcheck(xmin) and numcheck(xmax) and numcheck(ymin) and numcheck(ymax))):
            raise TypeError("All arguments must be ints or floats")
        if (xmin > xmax or ymin > ymax):
            raise ValueError("Expected xmin <= xmax and ymin <= ymax")
        
        self.xmin = xmin
        self.xmax = xmax
        self.ymin = ymin
        self.ymax = ymax

        x = random.uniform(xmin, xmax)
        y = random.uniform(ymin, ymax)
        super(RandomPoint2D, self).__init__(x, y)
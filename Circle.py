import sys
from Point2D import Point2D
import FitCircleExternal

class Circle(object):
    def __init__(self, radius, center):
        """
        radius of the circle is a float or int >= 0
        center is a Point2D object that specifies center (x, y) of the circle
        """
        if (isinstance(center, Point2D) and Point2D.IsNumeric(radius) and radius >= 0):
            self.radius = radius
            self.center = center
        else:
            raise ValueError("Center must be a Point2D and radius a float/int >= 0")

    def ContainsPoint(self, point):
        """
        returns true if point (of type Point2D) lies inside or on the boundary of the circle
        """
        if(not isinstance(point, Point2D)):
            raise ValueError("point must be of type Point2D")
        
        euclideanDist = lambda p1, p2 : pow(pow(p1.x-p2.x, 2) + pow(p1.y-p2.y, 2), 0.5)
        euclideanDistToCenter = euclideanDist(point, self.center)
        if (self.radius+Point2D.COMPARISONTOLERANCE > euclideanDistToCenter):
            return True
        return False

def FitCircleTo2DPoints(listOf2DPoints=[], useExternalImpl=False):
    """
    returns radius and center (of type Point2D) of circle that encloses all input points
    r and c are such that the enclosing circle has the smallest radius for the pointset
    """
    if not len(listOf2DPoints)>0 :
        raise ValueError("Can not fit a circle to an empty list of points")
    if len(listOf2DPoints)==1 :
        return 0, listOf2DPoints[0]
    
    if useExternalImpl:
        allPoints = []
        for point in listOf2DPoints:
            allPoints.append([point.x, point.y])
        centerAndRadius = FitCircleExternal.make_circle(allPoints)
        return centerAndRadius[2], Point2D(centerAndRadius[0], centerAndRadius[1])

    floatmin = sys.float_info.min
    floatmax = sys.float_info.max

    xmin = floatmax
    ymin = floatmax
    xmax = floatmin
    ymax = floatmin

    for point in listOf2DPoints:
        if(point.x < xmin):
            xmin = point.x
        if(point.y < ymin):
            ymin = point.y
        if(point.x > xmax):
            xmax = point.x
        if(point.y > ymax):
            ymax = point.y

    cx = (xmin + xmax)/2.0
    cy = (ymin + ymax)/2.0
    center = Point2D(cx, cy)

    euclideanDistSq = lambda p1, p2 : pow(p1.x-p2.x, 2) + pow(p1.y-p2.y, 2)
    radiusSq = floatmin
    for point in listOf2DPoints:
        distFromCenterSq = euclideanDistSq(point, center)
        if distFromCenterSq > radiusSq:
            radiusSq = distFromCenterSq
    
    return pow(radiusSq, 0.5), center 
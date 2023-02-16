.. _scriptingJavascript/creatingPathsShapes:

Creating paths and shapes
################################################################################

This section explains how to create items that contain paths.

----

Paths
================================================================================

To create line or a freeform path, specify a series of path points, as a series of x-y coordinates or ``path`` point objects.

Using x-y coordinates limits the path to straight segments. To created a curved path, you must create ``pathPoint`` objects. Your path can comprise a combination of page coordinates and ``pathPoint`` objects.

Specifying a series of x-y coordinates
********************************************************************************

To specify a path using page-coordinate pairs, use the ``setEntirePath()`` property of the ``pathItems`` object. The following script specifies three pairs of x-y coordinates, to create a path with three points

::

  var myDoc = app.activeDocument;
  var myLine = myDoc.pathItems.add();
  //set stroked to true so we can see the path
  myLine.stroked = true;
  myLine.setEntirePath([[220, 475], [375, 300], [200, 300]]);

Using path point objects
********************************************************************************

To create a ``pathPoint`` object, you must define three values for the point.

- A fixed ``anchor`` point, which is the point on the path.
- A pair of direction points— ``left direction`` and ``right direction`` —which allow you to control the path segment’s curve.

You define each property as an array of page coordinates in the format [x, y]:

- If all three properties of a ``pathPoint`` object have the same coordinates, and the properties of the next ``pathPoint`` in the line are equal to each other, you create a straight-line segment.
- If two or more properties in a ``pathPoint`` object have different values, the segment connected to the point is curved.

To create a path or add points to an existing path using ``pathPoint`` objects, create a ``pathItem`` object, then add the path points as child objects in the ``pathItem``::

  var myDoc = app.activeDocument;
  var myLine = myDoc.pathItems.add();

  //set stroked to true so we can see the path
  myLine.stroked = true;

  var newPoint = myLine.pathPoints.add();
  newPoint.anchor = [220, 475];
  //giving the direction points the same value as the
  //anchor point creates a straight line segment
  newPoint.leftDirection = newPoint.anchor;
  newPoint.rightDirection = newPoint.anchor;
  newPoint.pointType = PointType.CORNER;

  var newPoint1 = myLine.pathPoints.add();
  newPoint1.anchor = [375, 300];
  newPoint1.leftDirection = newPoint1.anchor;
  newPoint1.rightDirection = newPoint1.anchor;
  newPoint1.pointType = PointType.CORNER;

  var newPoint2 = myLine.pathPoints.add();
  newPoint2.anchor = [220, 300];
  //giving the direction points different values
  //than the anchor point creates a curve
  newPoint2.leftDirection =[180, 260];
  newPoint2.rightDirection = [240, 320];
  newPoint2.pointType = PointType.CORNER;

Combining path point types
********************************************************************************

The following script sample creates a path with three points::

  var myDoc = app.activeDocument;
  var myLine = myDoc.pathItems.add();
  myLine.stroked = true;
  myLine.setEntirePath( [[220, 475], [375, 300]]);

  // Append another point to the line
  var newPoint = myLine.pathPoints.add();
  newPoint.anchor = [220, 300];
  newPoint.leftDirection = newPoint.anchor;
  newPoint.rightDirection = newPoint.anchor;
  newPoint.pointType = PointType.CORNER;

----

Shapes
================================================================================

To create a shape, you use the object that corresponds to the shape’s name (like ``ellipse``, ``rectangle``, or ``polygon``), and use the object’s properties to specify the shape’s position, size, and other information like the number of sides in a polygon.

Remember:

- All measurements and page coordinates are processed as points by the scripting engine. For details, see :ref:`scripting/measurementUnits`.
- x and y coordinates are measured from the bottom-left corner of the document, as indicated in the Info panel in the Illustrator application. For details, see :ref:`scripting/positioning`.

Creating a rectangle
********************************************************************************

Consider the following sample::

  var myDocument = app.documents.add()
  var artLayer = myDocument.layers.add()
  var rect = artLayer.pathItems.rectangle( 144, 144, 72, 216 );

The sample uses the ``pathItems`` object’s ``rectangle()`` method to create a rectangle with these properties:

- The top of the rectangle is 2 inches (144 points) from the bottom edge of the page.
- The left edge is 2 inches (144 points) from the left edge of the page.
- The rectangle is 1 inch (72 points) wide and 3 inches (216 points) long.

Creating a polygon
********************************************************************************

Consider the following sample::

  var myDocument = app.documents.add()
  var artLayer = myDocument.layers.add()
  var poly = artLayer.pathItems.polygon( 144, 288, 72.0, 7 );

The sample uses the ``polygon()`` method to create a polygon with these properties:

- The center point of the object is inset is 2 inches (144 points) on the horizontal axis and 4 inches (288 points) on the vertical axis.
- The length of the radius from the center point to each corner is 1 inch (72 points).
- The polygon has 7 sides.

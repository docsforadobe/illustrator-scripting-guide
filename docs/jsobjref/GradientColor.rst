.. _jsobjref/GradientColor:

GradientColor
################################################################################

``gradientColor``

**Description**

A gradient color specification in a Gradient object. A script can create a new gradient color using a reference to an existing gradient in the document. If no existing gradient object is referenced, a default gradient is supplied.

----

==========
Properties
==========

.. _jsobjref/GradientColor.angle:

GradientColor.angle
********************************************************************************

``gradientColor.angle``

**Description**

The gradient vector angle in degrees. Default: 0.0.

**Type**

Number (double).

----

.. _jsobjref/GradientColor.gradient:

GradientColor.gradient
********************************************************************************

``gradientColor.gradient``

**Description**

Reference to the object defining the gradient.

**Type**

:ref:`jsobjref/Gradient`

----

.. _jsobjref/GradientColor.hiliteAngle:

GradientColor.hiliteAngle
********************************************************************************

``gradientColor.hiliteAngle``

**Description**

The gradient highlight vector angle in degrees.

**Type**

Number (double).

----

.. _jsobjref/GradientColor.hiliteLength:

GradientColor.hiliteLength
********************************************************************************

``gradientColor.hiliteLength``

**Description**

The gradient highlight vector length.

**Type**

Number (double).

----

.. _jsobjref/GradientColor.length:

GradientColor.length
********************************************************************************

``gradientColor.length``

**Description**

The gradient vector length.

**Type**

Number (double).

----

.. _jsobjref/GradientColor.matrix:

GradientColor.matrix
********************************************************************************

``gradientColor.matrix``

**Description**

An additional transformation matrix to manipulate the gradient path.

**Type**

Matrix.

----

.. _jsobjref/GradientColor.origin:

GradientColor.origin
********************************************************************************

``gradientColor.origin``

**Description**

The gradient vector origin, the center point of the gradient in this color.

**Type**

Array of 2 numbers.

----

.. _jsobjref/GradientColor.typename:

GradientColor.typename
********************************************************************************

``gradientColor.typename``

**Description**

The class name of the referenced object.

**Type**

String, read-only.

----

=======
Example
=======

.. _jsobjref/GradientColor.changingGradientStopColor:

Changing a gradient stop color
********************************************************************************

::

  // Creates a new RGB document, then changes the color of the first gradient stop of an indexed gradient
  app.documents.add(DocumentColorSpace.RGB);

  // Get a reference to the gradient that you want to change
  var gradientRef = app.activeDocument.gradients[1];

  // Create the new color
  var startColor = new RGBColor();
  startColor.red = 255;
  startColor.green = 238;
  startColor.blue = 98;

  // apply new color to the first gradient stop
  gradientRef.gradientStops[0].color = startColor;

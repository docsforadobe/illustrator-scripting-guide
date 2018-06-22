.. _jsobjref/gradientStop:

Gradient Stop
################################################################################

``gradientStop``

**Description**

A gradient stop definition that represents a point on a specific gradient defined in the document. Each gradient stop specifies a color change in the containing gradient. See :ref:`jsobjref/gradientColor.changingGradientStopColor` for an example.

----

==========
Properties
==========

.. _jsobjref/gradientStop.color:

GradientStop.color
********************************************************************************

``gradientStop.color``

**Description**

The color linked to this gradient stop.

**Type**

:ref:`jsobjref/color`

----

.. _jsobjref/gradientStop.midPoint:

GradientStop.midPoint
********************************************************************************

``gradientStop.midPoint``

**Description**

The midpoint key value, specified as a percentage from 13.0 to 87.0.

**Type**

Number (double).

----

.. _jsobjref/gradientStop.opacity:

GradientStop.opacity
********************************************************************************

``gradientStop.opacity``

**Description**

The opacity value for the gradient stop. Range: 0.0 to 100.0

**Type**

Number (double).

----

.. _jsobjref/gradientStop.parent:

GradientStop.parent
********************************************************************************

``gradientStop.parent``

**Description**

The gradient that contains this gradient stop.

**Type**

:ref:`jsobjref/gradient`, read-only.

----

.. _jsobjref/gradientStop.rampPoint:

GradientStop.rampPoint
********************************************************************************

``gradientStop.rampPoint``

**Description**

The location of the color in the blend in a range from 0.0 to 100.0, where 100.0 is 100%.

**Type**

Number (double).

----

.. _jsobjref/gradientStop.typename:

GradientStop.typename
********************************************************************************

``gradientStop.typename``

**Description**

The class name of the referenced object.

**Type**

String, read-only.

----

=======
Methods
=======

.. _jsobjref/gradientStop.remove:

GradientStop.remove()
********************************************************************************

``app.activeDocument.gradients[index].gradientStops[index].remove()``

**Description**

Deletes this object.

**Returns**

Nothing.

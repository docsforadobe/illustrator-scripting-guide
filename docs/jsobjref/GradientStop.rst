.. _jsobjref/GradientStop:

GradientStop
################################################################################

``gradientStop``

**Description**

A gradient stop definition that represents a point on a specific gradient defined in the document. Each gradient stop specifies a color change in the containing gradient. See :ref:`jsobjref/GradientColor.changingGradientStopColor` for an example.

----

==========
Properties
==========

.. _jsobjref/GradientStop.color:

GradientStop.color
********************************************************************************

``gradientStop.color``

**Description**

The color linked to this gradient stop.

**Type**

:ref:`jsobjref/Color`

----

.. _jsobjref/GradientStop.midPoint:

GradientStop.midPoint
********************************************************************************

``gradientStop.midPoint``

**Description**

The midpoint key value, specified as a percentage from 13.0 to 87.0.

**Type**

Number (double).

----

.. _jsobjref/GradientStop.opacity:

GradientStop.opacity
********************************************************************************

``gradientStop.opacity``

**Description**

The opacity value for the gradient stop. Range: 0.0 to 100.0

**Type**

Number (double).

----

.. _jsobjref/GradientStop.parent:

GradientStop.parent
********************************************************************************

``gradientStop.parent``

**Description**

The gradient that contains this gradient stop.

**Type**

:ref:`jsobjref/Gradient`, read-only.

----

.. _jsobjref/GradientStop.rampPoint:

GradientStop.rampPoint
********************************************************************************

``gradientStop.rampPoint``

**Description**

The location of the color in the blend in a range from 0.0 to 100.0, where 100.0 is 100%.

**Type**

Number (double).

----

.. _jsobjref/GradientStop.typename:

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

.. _jsobjref/GradientStop.remove:

GradientStop.remove()
********************************************************************************

``app.activeDocument.gradients[index].gradientStops[index].remove()``

**Description**

Deletes this object.

**Returns**

Nothing.

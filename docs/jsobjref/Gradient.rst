.. _jsobjref/Gradient:

Gradient
################################################################################

``gradient``

**Description**

A gradient definition contained in a document. Scripts can create new gradients.

----

==========
Properties
==========

.. _jsobjref/Gradient.gradientStops:

Gradient.gradientStops
********************************************************************************

``gradient.gradientStops``

**Description**

The gradient stops contained in this gradient.

**Type**

:ref:`jsobjref/GradientStops`, read-only.

----

.. _jsobjref/Gradient.name:

Gradient.name
********************************************************************************

``gradient.name``

**Description**

The gradient’s name.

**Type**

String.

----

.. _jsobjref/Gradient.parent:

Gradient.parent
********************************************************************************

``gradient.parent``

**Description**

The document that contains this gradient.

**Type**

:ref:`jsobjref/Document`, read-only.

----

.. _jsobjref/Gradient.type:

Gradient.type
********************************************************************************

``gradient.type``

**Description**

The kind of the gradient, either radial or linear.

**Type**

:ref:`jsobjref/scripting-constants.GradientType`

----

.. _jsobjref/Gradient.typename:

Gradient.typename
********************************************************************************

``gradient.typename``

**Description**

The class name of the referenced object.

**Type**

String, read-only.

----

=======
Methods
=======

.. _jsobjref/Gradient.remove:

Gradient.remove()
********************************************************************************

``app.activeDocument.gradients[index].remove()``

**Description**

Removes the referenced object from the document.

**Returns**

Nothing.

----

=======
Example
=======

Creating and applying a gradient
********************************************************************************

::

	// Creates a new gradient in current document then applies the gradient to the frontmost path item

	if (app.documents.length > 0) {
		// Create a color for both ends of the gradient
		var startColor = new RGBColor();
		startColor.red = 0;
		startColor.green = 100;
		startColor.blue = 255;

		var endColor = new RGBColor();
		endColor.red = 220;
		endColor.green = 0;
		endColor.blue = 100;

		// Create a new gradient
		// A new gradient always has 2 stops
		var newGradient = app.activeDocument.gradients.add();
		newGradient.name = "NewGradient";
		newGradient.type = GradientType.LINEAR;

		// Modify the first gradient stop
		newGradient.gradientStops[0].rampPoint = 30;
		newGradient.gradientStops[0].midPoint = 60;
		newGradient.gradientStops[0].color = startColor;

		// Modify the last gradient stop
		newGradient.gradientStops[1].rampPoint = 80;
		newGradient.gradientStops[1].color = endColor;

		// construct an Illustrator.GradientColor object referring to the newly created gradient
		var colorOfGradient = new GradientColor();
		colorOfGradient.gradient = newGradient;

		// get first path item, apply new gradient as its fill
		var topPath = app.activeDocument.pathItems[0];
		topPath.filled = true;
		topPath.fillColor = colorOfGradient;
	}

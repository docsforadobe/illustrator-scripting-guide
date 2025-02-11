.. _jsobjref/PatternColor:

PatternColor
################################################################################

``patternColor``

**Description**

A pattern color specification. You can create a new pattern color by modifying an existing pattern in the document. Any modification you make to a pattern affects that pattern in the Palette.

``PatternColor`` objects can be used in any property that takes a color object, such as ``fillColor`` or ``strokeColor``.

----

==========
Properties
==========

.. _jsobjref/PatternColor.matrix:

PatternColor.matrix
********************************************************************************

``patternColor.matrix``

**Description**

Additional transformation arising from manipulating the path.

**Type**

:ref:`jsobjref/Matrix`

----

.. _jsobjref/PatternColor.pattern:

PatternColor.pattern
********************************************************************************

``patternColor.pattern``

**Description**

A reference to the pattern object that defines the pattern to use in this color definition.

**Type**

:ref:`jsobjref/Pattern`

----

.. _jsobjref/PatternColor.reflect:

PatternColor.reflect
********************************************************************************

``patternColor.reflect``

**Description**

If ``true``, the prototype should be reflected before filling.

Default: ``false``

**Type**

Boolean

----

.. _jsobjref/PatternColor.reflectAngle:

PatternColor.reflectAngle
********************************************************************************

``patternColor.reflectAngle``

**Description**

The axis around which to reflect, in points.

Default: 0.0

**Type**

Number (double)

----

.. _jsobjref/PatternColor.rotation:

PatternColor.rotation
********************************************************************************

``patternColor.rotation``

**Description**

The angle in radians to rotate the prototype pattern before filling.

Default: 0.0

**Type**

Number (double)

----

.. _jsobjref/PatternColor.scaleFactor:

PatternColor.scaleFactor
********************************************************************************

``patternColor.scaleFactor``

**Description**

The fraction to which to scale the prototype pattern before filling, represented as a point containing horizontal and vertical scaling percentages.

**Type**

Array of 2 numbers

----

.. _jsobjref/PatternColor.shearAngle:

PatternColor.shearAngle
********************************************************************************

``patternColor.shearAngle``

**Description**

The angle in radians by which to slant the shear.

Default: 0.0

**Type**

Number (double)

----

.. _jsobjref/PatternColor.shearAxis:

PatternColor.shearAxis
********************************************************************************

``patternColor.shearAxis``

**Description**

The axis to shear with respect to, in points.

Default: 0.0

**Type**

Number (double)

----

.. _jsobjref/PatternColor.shiftAngle:

PatternColor.shiftAngle
********************************************************************************

``patternColor.shiftAngle``

**Description**

The angle in radians to which to translate the unscaled prototype pattern before filling.

Default: 0.0

**Type**

Number (double)

----

.. _jsobjref/PatternColor.shiftDistance:

PatternColor.shiftDistance
********************************************************************************

``patternColor.shiftDistance``

**Description**

The distance in points to which to translate the unscaled prototype pattern before filling.

Default: 0.0

**Type**

Number (double)

----

.. _jsobjref/PatternColor.typename:

PatternColor.typename
********************************************************************************

``patternColor.typename``

**Description**

The class name of the referenced object.

**Type**

String; read-only.

----

=======
Example
=======

Modifying and applying pattern colors
********************************************************************************

::

  // Rotates the color of each pattern in the current document,
  // then applies the last pattern to the first path item
  if (app.documents.length > 0 && app.activeDocument.pathItems.length > 0) {
    var doc = app.activeDocument;
    var swatchIndex = 0;

    for (i = 0; i < doc.swatches.length; i++) {
      // Get the generic color object of the swatch
      var currentSwatch = doc.swatches[i];
      var swatchColor = currentSwatch.color;

      // Only operate on patterns
      if (currentSwatch.color.typename == "PatternColor") {

        // Change a pattern property
        currentSwatch.color.rotation = 10;
        swatchIndex = i;
      }
    }

    // Apply the last pattern color swatch to the frontmost path
    var firstPath = app.activeDocument.pathItems[0];
    firstPath.filled = true;
    firstPath.fillColor = doc.swatches[swatchIndex].color;
  }

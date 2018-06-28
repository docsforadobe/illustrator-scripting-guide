.. _jsobjref/Spot:

Spot
################################################################################

``app.activeDocument.spots[index``

**Description**

A custom color definition contained in a :ref:`jsobjref/SpotColor` object.

If no properties are specified when creating a spot, default values are provided.

However, if specifying the color, you must use the same color space as the document, either CMYK or RGB. Otherwise, an error results.

The new spot is added to the end of the swatches list in the Swatches palette.

----

==========
Properties
==========

.. _jsobjref/Spot.color:

Spot.color
********************************************************************************

``app.activeDocument.spots[index].color``

**Description**

The color information for this spot color.

**Type**

:ref:`jsobjref/Color`

----

.. _jsobjref/Spot.colorType:

Spot.colorType
********************************************************************************

``app.activeDocument.spots[index].colorType``

**Description**

The color model for this custom color.

**Type**

:ref:`jsobjref/scripting-constants.ColorModel`

----

.. _jsobjref/Spot.name:

Spot.name
********************************************************************************

``app.activeDocument.spots[index].name``

**Description**

The spot color’s name.

**Type**

String

----

.. _jsobjref/Spot.parent:

Spot.parent
********************************************************************************

``app.activeDocument.spots[index].parent``

**Description**

The document that contains this spot color.

**Type**

:ref:`jsobjref/Document`; read-only.

----

.. _jsobjref/Spot.spotKind:

Spot.spotKind
********************************************************************************

``app.activeDocument.spots[index].spotKind``

**Description**

The kind of spot color (RGB, CMYK or LAB). This is the name of the color kind contained in the spot object.

**Type**

:ref:`jsobjref/scripting-constants.SpotColorKind`; read-only.

----

.. _jsobjref/Spot.typename:

Spot.typename
********************************************************************************

``app.activeDocument.spots[index].typename``

**Description**

The class name of the referenced object.

**Type**

String; read-only.

----

=======
Methods
=======

.. _jsobjref/Spot.getInternalColor:

Spot.getInternalColor()
********************************************************************************

``app.activeDocument.spots[index].getInternalColor()``

**Description**

Gets the internal color of a spot.

**Returns**

Color components.

----

.. _jsobjref/Spot.remove:

Spot.remove()
********************************************************************************

``app.activeDocument.spots[index].remove()``

**Description**

Deletes this object.

**Returns**

Nothing.

----

=======
Example
=======

Creating a new spot color
********************************************************************************

::

  // Creates a new spot color in the current document, then applies an 80% tint to the color
  if ( app.documents.length > 0 ) {
    var doc = app.activeDocument;

    // Create the new spot
    var newSpot = doc.spots.add();

    // Define the new color value
    var newColor = new CMYKColor();
    newColor.cyan = 35;
    newColor.magenta = 0;
    newColor.yellow = 50;
    newColor.black = 0;

    // Define a new SpotColor with an 80% tint
    // of the new Spot's color. The spot color can then
    // be applied to an art item like any other color.
    newSpot.name = "Pea-Green";
    newSpot.colorType = ColorModel.SPOT;
    newSpot.color = newColor;

    var newSpotColor = new SpotColor();
    newSpotColor.spot = newSpot;
    newSpotColor.tint = 80;
  }

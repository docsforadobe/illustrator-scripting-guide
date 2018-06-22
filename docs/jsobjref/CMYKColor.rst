.. _jsobjref/cmykColor:

CMYK Color
################################################################################

``cmykColor``

**Description**

A CMYK color specification, used where a ``color`` object is required.

If the color space of a document is ``RGB`` and you specify the color value for a page item in that document
using CMYK, Illustrator will translate the CMYK color specification into an RGB color specification. The same
thing happens if the document’s color space is CMYK and you specify colors using RGB. Since this
translation can lose information, you should specify colors using the class that matches the document’s
actual color space.

----

==========
Properties
==========

.. _jsobjref/cmykColor.black:

CMYKColor.black
********************************************************************************

``cmykColor.black``

**Description**

The black color value. Range 0.0–100.0. Default: 0.0

**Type**

Number (double)

----

.. _jsobjref/cmykColor.cyan:

CMYKColor.cyan
********************************************************************************

``cmykColor.cyan``

**Description**

The cyan color value. Range 0.0–100.0. Default: 0.0

**Type**

Number (double)

----

.. _jsobjref/cmykColor.magenta:

CMYKColor.magenta
********************************************************************************

``cmykColor.magenta``

**Description**

The magenta color value. Range 0.0–100.0. Default: 0.0

**Type**

Number (double)

----

.. _jsobjref/cmykColor.typename:

CMYKColor.typename
********************************************************************************

``cmykColor.typename``

**Description**

The class name of the referenced object.

**Type**

String; read-only.

----

.. _jsobjref/cmykColor.yellow:

CMYKColor.yellow
********************************************************************************

``cmykColor.yellow``

**Description**

The yellow color value. Range 0.0–100.0. Default: 0.0

**Type**

Number (double)

----

=======
Example
=======

Setting a CMYK color
********************************************************************************

::

  // Sets the fill color of the frontmost path item in
  // the current document to a light purple CMYK color

  if ( app.documents.length > 0 && app.activeDocument.pathItems.length > 0) {
    frontPath = app.activeDocument.pathItems[0];
    // Set color values for the CMYK object
    newcmykColor = new cmykColor();
    newcmykColor.black = 0;
    newcmykColor.cyan = 30.4;
    newcmykColor.magenta = 32;
    newcmykColor.yellow = 0;
    // Use the color object in the path item
    frontPath.filled = true;
    frontPath.fillColor = newcmykColor;
  }

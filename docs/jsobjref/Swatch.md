.. _jsobjref/Swatch:

Swatch
################################################################################

``app.activeDocument.swatches[index``

**Description**

A color swatch definition contained in a document. The swatches correspond to the swatch palette in the Illustrator user interface.

A script can create a new swatch.

The swatch can hold all types of color data, such as pattern, gradient, CMYK, RGB, gray, and spot.

----

==========
Properties
==========

.. _jsobjref/Swatch.color:

Swatch.color
********************************************************************************

``app.activeDocument.swatches[index].color``

**Description**

The color information for this swatch.

**Type**

:ref:`jsobjref/Color`

----

.. _jsobjref/Swatch.name:

Swatch.name
********************************************************************************

``app.activeDocument.swatches[index].name``

**Description**

The swatch's name.

**Type**

String.

----

.. _jsobjref/Swatch.parent:

Swatch.parent
********************************************************************************

``app.activeDocument.swatches[index].parent``

**Description**

The object that contains this swatch.

**Type**

:ref:`jsobjref/Document`, read-only.

----

.. _jsobjref/Swatch.typename:

Swatch.typename
********************************************************************************

``app.activeDocument.swatches[index].typename``

**Description**

The class name of the object.

**Type**

String, read-only.

----

=======
Methods
=======

.. _jsobjref/Swatch.remove:

Swatch.remove()
********************************************************************************

``app.activeDocument.swatches[index].remove()``

**Description**

Deletes this object.

**Returns**

Nothing.

----

=======
Example
=======

Modifying a swatch
********************************************************************************

::

  // Changes the name of the last swatch
  if ( app.documents.length > 0 && app.activeDocument.swatches.length > 0 ) {
    var lastIndex = app.activeDocument.swatches.length - 1;
    var lastSwatch = app.activeDocument.swatches[lastIndex];
    lastSwatch.name = "TheLastSwatch";
  }

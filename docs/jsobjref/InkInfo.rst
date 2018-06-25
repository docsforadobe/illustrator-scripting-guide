.. _jsobjref/InkInfo:

InkInfo
################################################################################

``app.activeDocument.inkList[index].inkInfo``

**Description**

Ink information for printing a document.

----

==========
Properties
==========

.. _jsobjref/InkInfo.angle:

InkInfo.angle
********************************************************************************

``app.activeDocument.inkList[index].inkInfo.angle``

**Description**

The ink’s screen angle in degrees. Range: -360 to 360.

**Type**

Number (double).

----

.. _jsobjref/InkInfo.customColor:

InkInfo.customColor
********************************************************************************

``app.activeDocument.inkList[index].inkInfo.customColor``

**Description**

The color of the custom ink.

**Type**

:ref:`jsobjref/Color`

----

.. _jsobjref/InkInfo.density:

InkInfo.density
********************************************************************************

``app.activeDocument.inkList[index].inkInfo.density``

**Description**

The neutral density. Minimum: 0.0.

**Type**

Number (double).

----

.. _jsobjref/InkInfo.dotShape:

InkInfo.dotShape
********************************************************************************

``app.activeDocument.inkList[index].inkInfo.dotShape``

**Description**

The dot shape name.

**Type**

String.

----

.. _jsobjref/InkInfo.frequency:

InkInfo.frequency
********************************************************************************

``app.activeDocument.inkList[index].inkInfo.frequency``

**Description**

The ink’s frequency. Range: 0.0 to 1000.0.

**Type**

Number (double).

----

.. _jsobjref/InkInfo.kind:

InkInfo.kind
********************************************************************************

``app.activeDocument.inkList[index].inkInfo.kind``

**Description**

The ink type.

**Type**

:ref:`jsobjref/scripting-constants.InkType`

----

.. _jsobjref/InkInfo.printingStatus:

InkInfo.printingStatus
********************************************************************************

``app.activeDocument.inkList[index].inkInfo.printingStatus``

**Description**

The ink printing status.

**Type**

:ref:`jsobjref/scripting-constants.InkPrintStatus`

----

.. _jsobjref/InkInfo.trapping:

InkInfo.trapping
********************************************************************************

``app.activeDocument.inkList[index].inkInfo.trapping``

**Description**

The trapping type.

**Type**

:ref:`jsobjref/scripting-constants.TrappingType`

----

.. _jsobjref/InkInfo.trappingOrder:

InkInfo.trappingOrder
********************************************************************************

``app.activeDocument.inkList[index].inkInfo.trappingOrder``

**Description**

The order of trapping for the ink. Range: 1 to 4 for CMYK.

**Type**

Number (long).

----

.. _jsobjref/InkInfo.typename:

InkInfo.typename
********************************************************************************

``app.activeDocument.inkList[index].inkInfo.typename``

**Description**

The class name of the object.

**Type**

String, read-only.

----

=======
Example
=======

Getting ink information
********************************************************************************

::

  // Displays the current documents inks in a text frame

  var docRef = documents.add();

  // assemble a string of the inks in this document
  var sInks = "";
  var iLength = activeDocument.inkList.length;
  for (var i = 0; i < iLength; i++) {
    sInks += docRef.inkList[i].name;
    sInks += "\r\t";
    sInks += "Frequency = " + docRef.inkList[i].inkInfo.frequency;
    sInks += "\r\t";
    sInks += "Density = " + docRef.inkList[i].inkInfo.density;
    sInks += "\r";
  }

  var textRef = docRef.textFrames.add();
  textRef.contents = sInks;
  textRef.top = 600;
  textRef.left = 200;

  redraw();

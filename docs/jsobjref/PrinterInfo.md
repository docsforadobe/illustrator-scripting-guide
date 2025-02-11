.. _jsobjref/PrinterInfo:

PrinterInfo
################################################################################

``printerInfo``

**Description**

Configuration information about a printer.

----

==========
Properties
==========

.. _jsobjref/PrinterInfo.binaryPrintingSupport:

PrinterInfo.binaryPrintingSupport
********************************************************************************

``printerInfo.binaryPrintingSupport``

**Description**

If ``true``, the printer supports binary printing.

**Type**

Boolean

----

.. _jsobjref/PrinterInfo.colorSupport:

PrinterInfo.colorSupport
********************************************************************************

``printerInfo.colorSupport``

**Description**

The printer color capability.

**Type**

:ref:`jsobjref/scripting-constants.PrinterColorMode`

----

.. _jsobjref/PrinterInfo.customPaperSupport:

PrinterInfo.customPaperSupport
********************************************************************************

``printerInfo.customPaperSupport``

**Description**

If ``true``, the printer supports custom paper size.

**Type**

Boolean

----

.. _jsobjref/PrinterInfo.customPaperTransverseSupport:

PrinterInfo.customPaperTransverseSupport
********************************************************************************

``printerInfo.customPaperTransverseSupport``

**Description**

If ``true``, the printer supports custom paper transverse.

**Type**

Boolean

----

.. _jsobjref/PrinterInfo.deviceResolution:

PrinterInfo.deviceResolution
********************************************************************************

``printerInfo.deviceResolution``

**Description**

The printer default resolution.

**Type**

Number (double)

----

.. _jsobjref/PrinterInfo.inRIPSeparationSupport:

PrinterInfo.inRIPSeparationSupport
********************************************************************************

``printerInfo.inRIPSeparationSupport``

**Description**

If ``true``, the printer supports InRIP color separation.

**Type**

Boolean

----

.. _jsobjref/PrinterInfo.maxDeviceResolution:

PrinterInfo.maxDeviceResolution
********************************************************************************

``printerInfo.maxDeviceResolution``

**Description**

The printer maximum device resolution.

**Type**

Number (double)

----

.. _jsobjref/PrinterInfo.maxPaperHeight:

PrinterInfo.maxPaperHeight
********************************************************************************

``printerInfo.maxPaperHeight``

**Description**

Custom paper’s maximum height.

**Type**

Number (double)

----

.. _jsobjref/PrinterInfo.maxPaperHeightOffset:

PrinterInfo.maxPaperHeightOffset
********************************************************************************

``printerInfo.maxPaperHeightOffset``

**Description**

Custom paper’s maximum height offset.

**Type**

Number (double)

----

.. _jsobjref/PrinterInfo.maxPaperWidth:

PrinterInfo.maxPaperWidth
********************************************************************************

``printerInfo.maxPaperWidth``

**Description**

Custom paper’s maximum width.

**Type**

Number (double)

----

.. _jsobjref/PrinterInfo.maxPaperWidthOffset:

PrinterInfo.maxPaperWidthOffset
********************************************************************************

``printerInfo.maxPaperWidthOffset``

**Description**

Custom paper’s maximum width offset.

**Type**

Number (double)

----

.. _jsobjref/PrinterInfo.minPaperHeight:

PrinterInfo.minPaperHeight
********************************************************************************

``printerInfo.minPaperHeight``

**Description**

Custom paper’s minimum height.

**Type**

Number (double)

----

.. _jsobjref/PrinterInfo.minPaperHeightOffset:

PrinterInfo.minPaperHeightOffset
********************************************************************************

``printerInfo.minPaperHeightOffset``

**Description**

Custom paper’s minimum height offset.

**Type**

Number (double)

----

.. _jsobjref/PrinterInfo.minPaperWidth:

PrinterInfo.minPaperWidth
********************************************************************************

``printerInfo.minPaperWidth``

**Description**

Custom paper’s minimum width.

**Type**

Number (double)

----

.. _jsobjref/PrinterInfo.minPaperWidthOffset:

PrinterInfo.minPaperWidthOffset
********************************************************************************

``printerInfo.minPaperWidthOffset``

**Description**

Custom paper’s minimum width offset.

**Type**

Number (double)

----

.. _jsobjref/PrinterInfo.paperSizes:

PrinterInfo.paperSizes
********************************************************************************

``printerInfo.paperSizes``

**Description**

The list of supported paper sizes.

**Type**

Array of :ref:`jsobjref/Paper`

----

.. _jsobjref/PrinterInfo.postScriptLevel:

PrinterInfo.postScriptLevel
********************************************************************************

``printerInfo.postScriptLevel``

**Description**

The PostScript Language level.

**Type**

:ref:`jsobjref/scripting-constants.PrinterPostScriptLevelEnum`

----

.. _jsobjref/PrinterInfo.printerType:

PrinterInfo.printerType
********************************************************************************

``printerInfo.printerType``

**Description**

The printer type.

**Type**

:ref:`jsobjref/scripting-constants.PrinterTypeEnum`

----

.. _jsobjref/PrinterInfo.typename:

PrinterInfo.typename
********************************************************************************

``printerInfo.typename``

**Description**

The class name of the object.

**Type**

String; read-only.

----

=======
Example
=======

Finding available printers
********************************************************************************

::

   // Displays a list of available printers in a new text frame
   var docRef = documents.add();
   var iCount = printerList.length;

   var textRef = docRef.textFrames.add();
   textRef.contents += "Printers...\r";

   for (var i = 0; i < iCount; i++) {
     textRef.contents += printerList[i].name;
     textRef.contents += "\r\t";
   }

   textRef.top = 600;
   textRef.left = 200;

   redraw();

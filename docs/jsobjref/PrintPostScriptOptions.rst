.. _jsobjref/PrintPostScriptOptions:

PrintPostScriptOptions
################################################################################

``new PrintPostScriptOptions()``

**Description**

Options for printing to a PostScript printer.

----

==========
Properties
==========

.. _jsobjref/PrintPostScriptOptions.binaryPrinting:

PrintPostScriptOptions.binaryPrinting
********************************************************************************

``printPostScriptOptions.binaryPrinting``

**Description**

If ``true``, printing should be in binary mode.

Default: ``false``

**Type**

Boolean

----

.. _jsobjref/PrintPostScriptOptions.compatibleShading:

PrintPostScriptOptions.compatibleShading
********************************************************************************

``printPostScriptOptions.compatibleShading``

**Description**

If ``true``, use PostScript Level 1-compatible gradient and gradient mesh printing.

Default: ``false``

**Type**

Boolean

----

.. _jsobjref/PrintPostScriptOptions.forceContinuousTone:

PrintPostScriptOptions.forceContinuousTone
********************************************************************************

``printPostScriptOptions.forceContinuousTone``

**Description**

If ``true``, force continuous tone.

Default: ``false``

**Type**

Boolean

----

.. _jsobjref/PrintPostScriptOptions.imageCompression:

PrintPostScriptOptions.imageCompression
********************************************************************************

``printPostScriptOptions.imageCompression``

**Description**

The image compression type.

Default: ``PostScriptImageCompressionType.IMAGECOMPRESSIONNONE``

**Type**

:ref:`jsobjref/scripting-constants.PostScriptImageCompressionType`

----

.. _jsobjref/PrintPostScriptOptions.negativePrinting:

PrintPostScriptOptions.negativePrinting
********************************************************************************

``printPostScriptOptions.negativePrinting``

**Description**

If ``true``, print in negative mode.

Default: ``false``

**Type**

Boolean

----

.. _jsobjref/PrintPostScriptOptions.postScriptLevel:

PrintPostScriptOptions.postScriptLevel
********************************************************************************

``printPostScriptOptions.postScriptLevel``

**Description**

The PostScript language level.

Default: ``PrinterPostScriptLevelEnum.LEVEL2``

**Type**

:ref:`jsobjref/scripting-constants.PrinterPostScriptLevelEnum`

----

.. _jsobjref/PrintPostScriptOptions.shadingResolution:

PrintPostScriptOptions.shadingResolution
********************************************************************************

``printPostScriptOptions.shadingResolution``

**Description**

The shading resolution. Range: 1.0 to 9600.0

Default: 300.0

**Type**

Number (double)

----

.. _jsobjref/PrintPostScriptOptions.typename:

PrintPostScriptOptions.typename
********************************************************************************

``printPostScriptOptions.typename``

**Description**

Read-only. The class name of the object.

**Type**

String

----

=======
Example
=======

Setting PostScript printing options
********************************************************************************

::

   // Prints current document with various postscript levels
   // Create new postscript options object, assign to print options
   var psOpts = new PrintPostScriptOptions();

   var printOpts = new PrintOptions();
   printOpts.postScriptOptions = psOpts;

   // Assign PS level, print
   psOpts.postScriptLevel = PrinterPostScriptLevelEnum.PSLEVEL2;
   activeDocument.print(printOpts);

   psOpts.postScriptLevel = PrinterPostScriptLevelEnum.PSLEVEL3;
   activeDocument.print(printOpts);

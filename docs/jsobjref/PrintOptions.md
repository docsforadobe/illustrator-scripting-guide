.. _jsobjref/PrintOptions:

PrintOptions
################################################################################

``new PrintOptions()``

**Description**

Contains information about all printing options including flattening, color management, coordinates, fonts, and paper.

----

==========
Properties
==========

.. _jsobjref/PrintOptions.colorManagementOptions:

PrintOptions.colorManagementOptions
********************************************************************************

``printOptions.colorManagementOptions``

**Description**

The printing color management options.

**Type**

:ref:`jsobjref/PrintColorManagementOptions`

----

.. _jsobjref/PrintOptions.colorSeparationOptions:

PrintOptions.colorSeparationOptions
********************************************************************************

``printOptions.colorSeparationOptions``

**Description**

The printing color separation options.

**Type**

:ref:`jsobjref/PrintColorSeparationOptions`

----

.. _jsobjref/PrintOptions.coordinateOptions:

PrintOptions.coordinateOptions
********************************************************************************

``printOptions.coordinateOptions``

**Description**

The printing coordinate options.

**Type**

:ref:`jsobjref/PrintCoordinateOptions`

----

.. _jsobjref/PrintOptions.flattenerOptions:

PrintOptions.flattenerOptions
********************************************************************************

``printOptions.flattenerOptions``

**Description**

The printing flattener options.

**Type**

:ref:`jsobjref/PrintFlattenerOptions`

----

.. _jsobjref/PrintOptions.flattenerPreset:

PrintOptions.flattenerPreset
********************************************************************************

``printOptions.flattenerPreset``

**Description**

The transparency flattener preset name.

**Type**

String

----

.. _jsobjref/PrintOptions.fontOptions:

PrintOptions.fontOptions
********************************************************************************

``printOptions.fontOptions``

**Description**

The printing font options.

**Type**

:ref:`jsobjref/PrintFontOptions`

----

.. _jsobjref/PrintOptions.jobOptions:

PrintOptions.jobOptions
********************************************************************************

``printOptions.jobOptions``

**Description**

The printing job options.

**Type**

:ref:`jsobjref/PrintJobOptions`

----

.. _jsobjref/PrintOptions.pageMarksOptions:

PrintOptions.pageMarksOptions
********************************************************************************

``printOptions.pageMarksOptions``

**Description**

The printing page marks options.

**Type**

:ref:`jsobjref/PrintPageMarksOptions`

----

.. _jsobjref/PrintOptions.paperOptions:

PrintOptions.paperOptions
********************************************************************************

``printOptions.paperOptions``

**Description**

The paper options.

**Type**

:ref:`jsobjref/PrintPaperOptions`

----

.. _jsobjref/PrintOptions.postScriptOptions:

PrintOptions.postScriptOptions
********************************************************************************

``printOptions.postScriptOptions``

**Description**

The printing PostScript options.

**Type**

:ref:`jsobjref/PrintPostScriptOptions`

----

.. _jsobjref/PrintOptions.PPDName:

PrintOptions.PPDName
********************************************************************************

``printOptions.PPDName``

**Description**

The PPD name.

**Type**

String

----

.. _jsobjref/PrintOptions.printerName:

PrintOptions.printerName
********************************************************************************

``printOptions.printerName``

**Description**

The printer name.

**Type**

String

----

.. _jsobjref/PrintOptions.printPreset:

PrintOptions.printPreset
********************************************************************************

``printOptions.printPreset``

**Description**

The print style.

**Type**

String

----

=======
Example
=======

Setting print options
********************************************************************************

::

  // Creates a new document, adds symbols, specifies a variety of print options,
  // assigns each print option to a PrintOptions object,
  // then prints with those options
  // Create a new document and add some symbol items
  var docRef = documents.add();
  var y = docRef.height - 30;

  for (var i = 0; i < (docRef.symbols.length); i++) {
    symbolRef = docRef.symbols[i];

    symbolItemRef1 = docRef.symbolItems.add(symbolRef);
    symbolItemRef1.top = y;

    symbolItemRef1.left = 100;

    y -= (symbolItemRef1.height + 10);
  }

  redraw();

  // Create multiple options and assign to PrintOptions
  var options = new PrintOptions();

  var colorOptions = new PrintColorManagementOptions();
  colorOptions.name = "ColorMatch RGB";
  colorOptions.intent = PrintColorIntent.SATURATIONINTENT;
  options.colorManagementOptions = colorOptions;

  var printJobOptions = new PrintJobOptions();
  printJobOptions.designation = PrintArtworkDesignation.ALLLAYERS;
  printJobOptions.reverse = true;

  options.jobOptions = printJobOptions;

  var coordinateOptions = new PrintCoordinateOptions();
  coordinateOptions.fitToPage = true;
  options.coordinateOptions = coordinateOptions;

  var flatOpts = new PrintFlattenerOptions();
  flatOpts.ClipComplexRegions = true;
  flatOpts.GradientResoultion = 60;

  flatOpts.RasterizatonResotion = 60;
  options.flattenerOptions = flatOpts;

  // Print with options
  docRef.print(options);

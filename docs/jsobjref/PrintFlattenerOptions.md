.. _jsobjref/PrintFlattenerOptions:

PrintFlattenerOptions
################################################################################

``new PrintFlattenerOptions()``

**Description**

Contains flattening options for use when Illustrator outputs artwork that contains transparency into a non-native format.

----

==========
Properties
==========


.. _jsobjref/PrintFlattenerOptions.clipComplexRegions:

PrintFlattenerOptions.clipComplexRegions
********************************************************************************

``printFlattenerOptions.clipComplexRegions``

**Description**

If ``true``, complex regions should be clipped.

Default: ``false``

**Type**

Boolean

----

.. _jsobjref/PrintFlattenerOptions.convertStrokesToOutlines:

PrintFlattenerOptions.convertStrokesToOutlines
********************************************************************************

``printFlattenerOptions.convertStrokesToOutlines``

**Description**

If ``true``, convert all strokes to outlines.

Default: ``false``

**Type**

Boolean

----

.. _jsobjref/PrintFlattenerOptions.convertTextToOutlines:

PrintFlattenerOptions.convertTextToOutlines
********************************************************************************

``printFlattenerOptions.convertTextToOutlines``

**Description**

If ``true``, all text is converted to vector paths; preserves the visual appearance of type.

Default: ``false``

**Type**

Boolean

----

.. _jsobjref/PrintFlattenerOptions.flatteningBalance:

PrintFlattenerOptions.flatteningBalance
********************************************************************************

``printFlattenerOptions.flatteningBalance``

**Description**

The flattening balance.

Range: 0.0 to 100.0.

Default: 100.0

**Type**

Number (long)

----

.. _jsobjref/PrintFlattenerOptions.gradientResolution:

PrintFlattenerOptions.gradientResolution
********************************************************************************

``printFlattenerOptions.gradientResolution``

**Description**

The gradient resolution in dots per inch (dpi).

Range: 1.0 to 9600.0.

Default: 300.0

**Type**

Number (double)

----

.. _jsobjref/PrintFlattenerOptions.overprint:

PrintFlattenerOptions.overprint
********************************************************************************

``printFlattenerOptions.overprint``

**Description**

Whether to preserve, discard, or simulate overprinting.

Default: ``PDFOverprint.PRESERVEPDFOVERPRINT``

**Type**

:ref:`jsobjref/scripting-constants.PDFOverprint`

----

.. _jsobjref/PrintFlattenerOptions.rasterizationResolution:

PrintFlattenerOptions.rasterizationResolution
********************************************************************************

``printFlattenerOptions.rasterizationResolution``

**Description**

The rasterization resolution in dots per inch (dpi). Range: 1.0 to 9600.0.

Default: 300.0

**Type**

Number (double)

----

.. _jsobjref/PrintFlattenerOptions.typename:

PrintFlattenerOptions.typename
********************************************************************************

``printFlattenerOptions.typename``

**Description**

The class name of the object.

**Type**

String; read-only.

----

=======
Example
=======

Setting print flattening
********************************************************************************

::

  // Creates a new document, adds symbols to the document
  // then prints with a range of flattener balance settings
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

  // Create PrintFlattenerOptions object and assign to a PrintOptions object
  var flatOpts = new PrintFlattenerOptions();
  var printOpts = new PrintOptions();
  printOpts.flattenerOptions = flatOpts;

  // Set other print options
  printOpts.ClipComplexRegions = true;
  printOpts.GradientResoultion = 360;
  printOpts.RasterizatonResotion = 360;

  // Print the current document with flattening balance increments of 20
  for (var i = 0; i <= 100; i += 20) {
    flatOpts.flatteningBalance = i;
    activeDocument.print(printOpts);
  }

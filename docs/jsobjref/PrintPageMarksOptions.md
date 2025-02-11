.. _jsobjref/PrintPageMarksOptions:

PrintPageMarksOptions
################################################################################

``new PrintPageMarksOptions()``

**Description**

The options for printing page marks.

----

==========
Properties
==========

.. _jsobjref/PrintPageMarksOptions.bleedOffsetRect:

PrintPageMarksOptions.bleedOffsetRect
********************************************************************************

``printPageMarksOptions.bleedOffsetRect``

**Description**

The bleed offset rectangle.

**Type**

Array of 4 numbers

----

.. _jsobjref/PrintPageMarksOptions.colorBars:

PrintPageMarksOptions.colorBars
********************************************************************************

``printPageMarksOptions.colorBars``

**Description**

If ``true``, enable printing of color bars.

Default: ``false``

**Type**

Boolean

----

.. _jsobjref/PrintPageMarksOptions.marksOffsetRect:

PrintPageMarksOptions.marksOffsetRect
********************************************************************************

``printPageMarksOptions.marksOffsetRect``

**Description**

The page marks offset rectangle.

**Type**

Array of 4 numbers

----

.. _jsobjref/PrintPageMarksOptions.pageInfoMarks:

PrintPageMarksOptions.pageInfoMarks
********************************************************************************

``printPageMarksOptions.pageInfoMarks``

**Description**

If ``true``, page info marks printing is enabled.

Default: ``false``

**Type**

Boolean

----

.. _jsobjref/PrintPageMarksOptions.pageMarksType:

PrintPageMarksOptions.pageMarksType
********************************************************************************

``printPageMarksOptions.pageMarksType``

**Description**

The page marks style.

Default: ``PageMarksType.Roman``

**Type**

:ref:`jsobjref/scripting-constants.PageMarksTypes`

----

.. _jsobjref/PrintPageMarksOptions.registrationMarks:

PrintPageMarksOptions.registrationMarks
********************************************************************************

``printPageMarksOptions.registrationMarks``

**Description**

If ``true``, registration marks should be printed.

Default: ``false``

**Type**

Boolean

----

.. _jsobjref/PrintPageMarksOptions.trimMarks:

PrintPageMarksOptions.trimMarks
********************************************************************************

``printPageMarksOptions.trimMarks``

**Description**

If ``true``, trim marks should be printed.

Default: ``false``

**Type**

Boolean

----

.. _jsobjref/PrintPageMarksOptions.trimMarksWeight:

PrintPageMarksOptions.trimMarksWeight
********************************************************************************

``printPageMarksOptions.trimMarksWeight``

**Description**

Stroke weight of trim marks. Minimum: 0.0.

Default: 0.125

**Type**

Number (double)

----

.. _jsobjref/PrintPageMarksOptions.typename:

PrintPageMarksOptions.typename
********************************************************************************

``printPageMarksOptions.typename``

**Description**

The class name of the object.

**Type**

String; read-only.

----

=======
Example
=======

Setting page mark printing options
********************************************************************************

::

  // Creates a PrintPageMarksOptions object, assigns it
  // to a PrintOptions object, then prints the current document.
  var docRef = activeDocument;
  var pageMarkOptions= new PrintPageMarksOptions();

  var options = new PrintOptions();
  options.pageMarksOptions = pageMarkOptions;

  pageMarkOptions.colorBars = true;
  pageMarkOptions.pageInfoMarks = true;
  pageMarkOptions.registrationMarks = true;
  pageMarkOptions.trimMarks = true;

  docRef.print(options);


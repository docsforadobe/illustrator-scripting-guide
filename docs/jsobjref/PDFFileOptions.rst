.. _jsobjref/PDFFileOptions:

PDFFileOptions
################################################################################

``app.preferences.PDFFileOptions``

**Description**

Options for opening a PDF file, used with the :ref:`jsobjref/Application.open` method.

All properties are optional.

----

==========
Properties
==========

.. _jsobjref/PDFFileOptions.pageToOpen:

PDFFileOptions.pageToOpen
********************************************************************************

``app.preferences.PDFFileOptions.pageToOpen``

**Description**

What page should be used when opening a multipage document.

Default: 1

**Type**

Number (long)

----

.. _jsobjref/PDFFileOptions.parent:

PDFFileOptions.parent
********************************************************************************

``app.preferences.PDFFileOptions.parent``

**Description**

The object’s container.

**Type**

Object; read-only.

----

.. _jsobjref/PDFFileOptions.pDFCropToBox:

PDFFileOptions.pDFCropToBox
********************************************************************************

``app.preferences.PDFFileOptions.pDFCropToBox``

**Description**

Which box should be used when placing a multipage document.

Default: ``PDFBoxType.PDFMediaBox``

**Type**

:ref:`jsobjref/scripting-constants.PDFBoxType`

----

.. _jsobjref/PDFFileOptions.typename:

PDFFileOptions.typename
********************************************************************************

``app.preferences.PDFFileOptions.typename``

**Description**

The class name of the object.

**Type**

String; read-only.

----

==========
Example
==========

Opening a PDF with options
********************************************************************************

::

  // Opens a PDF file with specified options
  var pdfOptions = app.preferences.PDFFileOptions;
  pdfOptions.pDFCropToBox = PDFBoxType.PDFBOUNDINGBOX;
  pdfOptions.pageToOpen = 2;

  // Open a file using these preferences
  var fileRef = filePath;

  if (fileRef != null) {
    var docRef = open(fileRef, DocumentColorSpace.RGB);
  }

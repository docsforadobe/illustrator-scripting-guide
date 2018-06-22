.. _jsobjref/documentPreset:

Document Preset
################################################################################

``documentPreset``

**Description**

A preset document template to use when creating a new document. See :ref:`jsobjref/documents.addDocument`.

----

==========
Properties
==========

.. _jsobjref/documentPreset.artboardLayout:

DocumentPreset.artboardLayout
********************************************************************************

``documentPreset.artboardLayout``

**Description**

The layout of artboards in the new document. Default: ``GridByRow``.

**Type**

:ref:`jsobjref/scriptingConstants.documentArtboardLayout`

----

.. _jsobjref/documentPreset.artboardRowsOrCols:

DocumentPreset.artboardRowsOrCols
********************************************************************************

``documentPreset.artboardRowsOrCols``

**Description**

The number of rows (for rows layout) or columns (for column layout) of artboards. Range: 1 to (``numArtboards`` - 1) or 1 for single row or column layouts. Default: 1

**Type**

Number (long).

----

.. _jsobjref/documentPreset.artboardSpacing:

DocumentPreset.artboardSpacing
********************************************************************************

``documentPreset.artboardSpacing``

**Description**

The spacing between artboards in the new document. Default: 20.0

**Type**

Number (double).

----

.. _jsobjref/documentPreset.colorMode:

DocumentPreset.colorMode
********************************************************************************

``documentPreset.colorMode``

**Description**

The color space for the new document.

**Type**

:ref:`jsobjref/scriptingConstants.documentColorSpace`

----

.. _jsobjref/documentPreset.documentBleedLink:

DocumentPreset.documentBleedLink
********************************************************************************

``documentPreset.documentBleedLink``

**Description**

The document link for bleed values.

**Type**

Boolean.

----

.. _jsobjref/documentPreset.documentBleedOffsetRect:

DocumentPreset.documentBleedOffsetRect
********************************************************************************

``documentPreset.documentBleedOffsetRect``

**Description**

The document bleed offset rectangle.

**Type**

Rectangle.

----

.. _jsobjref/documentPreset.height:

DocumentPreset.height
********************************************************************************

``documentPreset.height``

**Description**

The height in document points. Default: 792.0

**Type**

Number (double).

----

.. _jsobjref/documentPreset.numArtboards:

DocumentPreset.numArtboards
********************************************************************************

``documentPreset.numArtboards``

**Description**

The number of artboards for the new document. Range: 1 to 100. Default: 1.

**Type**

Number (long).

----

.. _jsobjref/documentPreset.previewMode:

DocumentPreset.previewMode
********************************************************************************

``documentPreset.previewMode``

**Description**

The preview mode for the new document.

**Type**

:ref:`jsobjref/scriptingConstants.documentPreviewMode`

----

.. _jsobjref/documentPreset.rasterResolution:

DocumentPreset.rasterResolution
********************************************************************************

``documentPreset.rasterResolution``

**Description**

The raster resolution for the new document.

**Type**

:ref:`jsobjref/scriptingConstants.documentRasterResolution`

----

.. _jsobjref/documentPreset.title:

DocumentPreset.title
********************************************************************************

``documentPreset.title``

**Description**

The document title.

**Type**

String.

----

.. _jsobjref/documentPreset.transparencyGrid:

DocumentPreset.transparencyGrid
********************************************************************************

``documentPreset.transparencyGrid``

**Description**

The transparency grid color for the new document.

**Type**

:ref:`jsobjref/scriptingConstants.DocumentTransparencyGrid`

----

.. _jsobjref/documentPreset.typename:

DocumentPreset.typename
********************************************************************************

``documentPreset.typename``

**Description**

The class name of the referenced object.

**Type**

String, read-only.

----

.. _jsobjref/documentPreset.units:

DocumentPreset.units
********************************************************************************

``documentPreset.units``

**Description**

The ruler units for the new document.

**Type**

:ref:`jsobjref/scriptingConstants.RulerUnits`

----

.. _jsobjref/documentPreset.width:

DocumentPreset.width
********************************************************************************

``documentPreset.width``

**Description**

The width in document points. Default: 612.0

**Type**

Number (double).

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

documentPreset.artboardLayout
********************************************************************************

``documentPreset.artboardLayout``

**Description**

The layout of artboards in the new document. Default: ``GridByRow``.

**Type**

:ref:`jsobjref/documentArtboardLayout`

----

.. _jsobjref/documentPreset.artboardRowsOrCols:

documentPreset.artboardRowsOrCols
********************************************************************************

``documentPreset.artboardRowsOrCols``

**Description**

The number of rows (for rows layout) or columns (for column layout) of artboards. Range: 1 to (``numArtboards`` - 1) or 1 for single row or column layouts. Default: 1

**Type**

Number (long).

----

.. _jsobjref/documentPreset.artboardSpacing:

documentPreset.artboardSpacing
********************************************************************************

``documentPreset.artboardSpacing``

**Description**

The spacing between artboards in the new document. Default: 20.0

**Type**

Number (double).

----

.. _jsobjref/documentPreset.colorMode:

documentPreset.colorMode
********************************************************************************

``documentPreset.colorMode``

**Description**

The color space for the new document.

**Type**

:ref:`jsobjref/documentColorSpace`

----

.. _jsobjref/documentPreset.documentBleedLink:

documentPreset.documentBleedLink
********************************************************************************

``documentPreset.documentBleedLink``

**Description**

The document link for bleed values.

**Type**

Boolean.

----

.. _jsobjref/documentPreset.documentBleedOffsetRect:

documentPreset.documentBleedOffsetRect
********************************************************************************

``documentPreset.documentBleedOffsetRect``

**Description**

The document bleed offset rectangle.

**Type**

Rectangle.

----

.. _jsobjref/documentPreset.height:

documentPreset.height
********************************************************************************

``documentPreset.height``

**Description**

The height in document points. Default: 792.0

**Type**

Number (double).

----

.. _jsobjref/documentPreset.numArtboards:

documentPreset.numArtboards
********************************************************************************

``documentPreset.numArtboards``

**Description**

The number of artboards for the new document. Range: 1 to 100. Default: 1.

**Type**

Number (long).

----

.. _jsobjref/documentPreset.previewMode:

documentPreset.previewMode
********************************************************************************

``documentPreset.previewMode``

**Description**

The preview mode for the new document.

**Type**

:ref:`jsobjref/previewMode`

----

.. _jsobjref/documentPreset.rasterResolution:

documentPreset.rasterResolution
********************************************************************************

``documentPreset.rasterResolution``

**Description**

The raster resolution for the new document.

**Type**

:ref:`jsobjref/rasterResolution`

----

.. _jsobjref/documentPreset.title:

documentPreset.title
********************************************************************************

``documentPreset.title``

**Description**

The document title.

**Type**

String.

----

.. _jsobjref/documentPreset.transparencyGrid:

documentPreset.transparencyGrid
********************************************************************************

``documentPreset.transparencyGrid``

**Description**

The transparency grid color for the new document.

**Type**

:ref:`jsobjref/documentTransparencyGrid`

----

.. _jsobjref/documentPreset.typename:

documentPreset.typename
********************************************************************************

``documentPreset.typename``

**Description**

The class name of the referenced object.

**Type**

String, read-only.

----

.. _jsobjref/documentPreset.units:

documentPreset.units
********************************************************************************

``documentPreset.units``

**Description**

The ruler units for the new document.

**Type**

:ref:`jsobjref/rulerUnits`

----

.. _jsobjref/documentPreset.width:

documentPreset.width
********************************************************************************

``documentPreset.width``

**Description**

The width in document points. Default: 612.0

**Type**

Number (double).

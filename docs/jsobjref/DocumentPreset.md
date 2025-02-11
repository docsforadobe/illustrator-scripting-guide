.. _jsobjref/DocumentPreset:

DocumentPreset
################################################################################

``documentPreset``

**Description**

A preset document template to use when creating a new document. See :ref:`jsobjref/Documents.addDocument`.

----

==========
Properties
==========

.. _jsobjref/DocumentPreset.artboardLayout:

DocumentPreset.artboardLayout
********************************************************************************

``documentPreset.artboardLayout``

**Description**

The layout of artboards in the new document. Default: ``GridByRow``.

**Type**

:ref:`jsobjref/scripting-constants.DocumentArtboardLayout`

----

.. _jsobjref/DocumentPreset.artboardRowsOrCols:

DocumentPreset.artboardRowsOrCols
********************************************************************************

``documentPreset.artboardRowsOrCols``

**Description**

The number of rows (for rows layout) or columns (for column layout) of artboards. Range: 1 to (``numArtboards`` - 1) or 1 for single row or column layouts. Default: 1

**Type**

Number (long).

----

.. _jsobjref/DocumentPreset.artboardSpacing:

DocumentPreset.artboardSpacing
********************************************************************************

``documentPreset.artboardSpacing``

**Description**

The spacing between artboards in the new document. Default: 20.0

**Type**

Number (double).

----

.. _jsobjref/DocumentPreset.colorMode:

DocumentPreset.colorMode
********************************************************************************

``documentPreset.colorMode``

**Description**

The color space for the new document.

**Type**

:ref:`jsobjref/scripting-constants.DocumentColorSpace`

----

.. _jsobjref/DocumentPreset.documentBleedLink:

DocumentPreset.documentBleedLink
********************************************************************************

``documentPreset.documentBleedLink``

**Description**

The document link for bleed values.

**Type**

Boolean.

----

.. _jsobjref/DocumentPreset.documentBleedOffsetRect:

DocumentPreset.documentBleedOffsetRect
********************************************************************************

``documentPreset.documentBleedOffsetRect``

**Description**

The document bleed offset rectangle.

**Type**

Rectangle.

----

.. _jsobjref/DocumentPreset.height:

DocumentPreset.height
********************************************************************************

``documentPreset.height``

**Description**

The height in document points. Default: 792.0

**Type**

Number (double).

----

.. _jsobjref/DocumentPreset.numArtboards:

DocumentPreset.numArtboards
********************************************************************************

``documentPreset.numArtboards``

**Description**

The number of artboards for the new document. Range: 1 to 100. Default: 1.

**Type**

Number (long).

----

.. _jsobjref/DocumentPreset.previewMode:

DocumentPreset.previewMode
********************************************************************************

``documentPreset.previewMode``

**Description**

The preview mode for the new document.

**Type**

:ref:`jsobjref/scripting-constants.DocumentPreviewMode`

----

.. _jsobjref/DocumentPreset.rasterResolution:

DocumentPreset.rasterResolution
********************************************************************************

``documentPreset.rasterResolution``

**Description**

The raster resolution for the new document.

**Type**

:ref:`jsobjref/scripting-constants.DocumentRasterResolution`

----

.. _jsobjref/DocumentPreset.title:

DocumentPreset.title
********************************************************************************

``documentPreset.title``

**Description**

The document title.

**Type**

String.

----

.. _jsobjref/DocumentPreset.transparencyGrid:

DocumentPreset.transparencyGrid
********************************************************************************

``documentPreset.transparencyGrid``

**Description**

The transparency grid color for the new document.

**Type**

:ref:`jsobjref/scripting-constants.DocumentTransparencyGrid`

----

.. _jsobjref/DocumentPreset.typename:

DocumentPreset.typename
********************************************************************************

``documentPreset.typename``

**Description**

The class name of the referenced object.

**Type**

String, read-only.

----

.. _jsobjref/DocumentPreset.units:

DocumentPreset.units
********************************************************************************

``documentPreset.units``

**Description**

The ruler units for the new document.

**Type**

:ref:`jsobjref/scripting-constants.RulerUnits`

----

.. _jsobjref/DocumentPreset.width:

DocumentPreset.width
********************************************************************************

``documentPreset.width``

**Description**

The width in document points. Default: 612.0

**Type**

Number (double).

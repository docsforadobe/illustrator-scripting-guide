.. _jsobjref/documentPreset:

Document Preset
################################################################################

``documentPreset``

**Description**

A preset document template to use when creating a new document. See **Documents.addDocument()**.

//todo: Add link to **Documents.addDocument()** in above paragraph.

----

==========
Properties
==========

.. _documentPreset.artboardLayout:

documentPreset.artboardLayout
********************************************************************************

``documentPreset.artboardLayout``

**Description**

The layout of artboards in the new document. Default: ``GridByRow``.

**Type**

// todo: link to **DocumentArtboardLayout** in Chapter 2 "Scripting Constants"

**DocumentArtboardLayout**

----

.. _documentPreset.artboardRowsOrCols:

documentPreset.artboardRowsOrCols
********************************************************************************

``documentPreset.artboardRowsOrCols``

**Description**

The number of rows (for rows layout) or columns (for column layout) of artboards. Range: 1 to (``numArtboards`` - 1) or 1 for single row or column layouts. Default: 1

**Type**

Number (long).

----

.. _documentPreset.artboardSpacing:

documentPreset.artboardSpacing
********************************************************************************

``documentPreset.artboardSpacing``

**Description**

The spacing between artboards in the new document. Default: 20.0

**Type**

Number (double).

----

.. _documentPreset.colorMode:

documentPreset.colorMode
********************************************************************************

``documentPreset.colorMode``

**Description**

The color space for the new document.

**Type**

// todo: link to **DocumentColorSpace** in Chapter 2 "Scripting Constants"

**DocumentColorSpace**

----

.. _documentPreset.documentBleedLink:

documentPreset.documentBleedLink
********************************************************************************

``documentPreset.documentBleedLink``

**Description**

The document link for bleed values.

**Type**

Boolean.

----

.. _documentPreset.documentBleedOffsetRect:

documentPreset.documentBleedOffsetRect
********************************************************************************

``documentPreset.documentBleedOffsetRect``

**Description**

The document bleed offset rectangle.

**Type**

Rectangle.

----

.. _documentPreset.height:

documentPreset.height
********************************************************************************

``documentPreset.height``

**Description**

The height in document points. Default: 792.0

**Type**

Number (double).

----

.. _documentPreset.numArtboards:

documentPreset.numArtboards
********************************************************************************

``documentPreset.numArtboards``

**Description**

The number of artboards for the new document. Range: 1 to 100. Default: 1.

**Type**

Number (long).

----

.. _documentPreset.previewMode:

documentPreset.previewMode
********************************************************************************

``documentPreset.previewMode``

**Description**

The preview mode for the new document.

**Type**

// todo: link to **DocumentPreviewMode** in Chapter 2 "Scripting Constants"

**DocumentPreviewMode**

----

.. _documentPreset.rasterResolution:

documentPreset.rasterResolution
********************************************************************************

``documentPreset.rasterResolution``

**Description**

The raster resolution for the new document.

**Type**

// todo: link to **DocumentRasterResolution** in Chapter 2 "Scripting Constants"

**DocumentRasterResolution**

----

.. _documentPreset.title:

documentPreset.title
********************************************************************************

``documentPreset.title``

**Description**

The document title.

**Type**

String.

----

.. _documentPreset.transparencyGrid:

documentPreset.transparencyGrid
********************************************************************************

``documentPreset.transparencyGrid``

**Description**

The transparency grid color for the new document.

**Type**

// todo: link to **DocumentTransparencyGrid** in Chapter 2 "Scripting Constants"

**DocumentTransparencyGrid**

----

.. _documentPreset.typename:

documentPreset.typename
********************************************************************************

``documentPreset.typename``

**Description**

The class name of the referenced object.

**Type**

String, read-only.

----

.. _documentPreset.units:

documentPreset.units
********************************************************************************

``documentPreset.units``

**Description**

The ruler units for the new document.

**Type**

// todo: link to **RulerUnits** in Chapter 2 "Scripting Constants"

**RulerUnits**

----

.. _documentPreset.width:

documentPreset.width
********************************************************************************

``documentPreset.width``

**Description**

The width in document points. Default: 612.0

**Type**

Number (double).

----
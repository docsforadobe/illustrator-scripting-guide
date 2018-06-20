.. _jsobjref/document:

Document
################################################################################

``document``

**Description**

An Illustrator document. Documents are contained in the Application object.

The default document settings—those properties starting with the word “default”—are global settings that affect the current document. Be sure to modify these default properties only when a document is open. Note that if you set default properties to desired values before creating new objects, you can streamline your scripts, eliminating the need to specify specific properties such as ``fillColor`` and ``stroked`` that have default properties.

A document’s color space, height, and width can only be set when the document is created. You cannot modify these properties in an existing document. See Application.open for more information on how document color spaces are handled.

//todo: Add link to **Application.open** in above paragraph.

----

==========
Properties
==========

.. _document.activeDataset:

document.activeDataset
********************************************************************************

``app.activeDocument.activeDataset``

**Description**

The currently opened dataset.

**Type**

:ref:`jsobjref/dataset`

----

.. _document.activeLayer:

document.activeLayer
********************************************************************************

``app.activeDocument.activeLayer``

**Description**

The active layer in the document.

**Type**

:ref:`jsobjref/layer`

----

.. _document.activeView:

document.activeView
********************************************************************************

``app.activeDocument.activeView``

**Description**

The document’s current view.

**Type**

:ref:`jsobjref/view`, read-only.

----

.. _document.artboards:

document.artboards
********************************************************************************

``app.activeDocument.artboards``

**Description**

All artboards in the document.

**Type**

:ref:`jsobjref/artboards`, read-only.

----

.. _document.brushes:

document.brushes
********************************************************************************

``app.activeDocument.brushes``

**Description**

The brushes contained in the document.

**Type**

:ref:`jsobjref/brushes`, read-only.

----

.. _document.characterStyles:

document.characterStyles
********************************************************************************

``app.activeDocument.characterStyles``

**Description**

The list of character styles in this document.

**Type**

:ref:`jsobjref/characterStyles`, read-only.

----

.. _document.compoundPathItems:

document.compoundPathItems
********************************************************************************

``app.activeDocument.compoundPathItems``

**Description**

The compound path items contained in the document.

**Type**

:ref:`jsobjref/compoundPathItems`, read-only.

----

.. _document.cropBox:

document.cropBox
********************************************************************************

``app.activeDocument.cropBox``

**Description**

The boundary of the document’s cropping box for output, or ``null`` if no value has been set.

**Type**

Array of 4 numbers.

----

.. _document.cropStyle:

document.cropStyle
********************************************************************************

``app.activeDocument.cropStyle``

**Description**

The style of the document’s cropping box.

**Type**

// todo: link to **CropOptions** in Chapter 2 "Scripting Constants"

CropOptions.

----

.. _document.dataSets:

document.dataSets
********************************************************************************

``app.activeDocument.dataSets``

**Description**

The datasets contained in the document.

**Type**

:ref:`jsobjref/dataSets`, read-only.

----

.. _document.defaultFillColor:

document.defaultFillColor
********************************************************************************

``app.activeDocument.defaultFillColor``

**Description**

The color to use to fill new paths if ``defaultFilled`` is ``true``.

**Type**

:ref:`jsobjref/color`

----

.. _document.defaultFilled:

document.defaultFilled
********************************************************************************

``app.activeDocument.defaultFilled``

**Description**

If ``true``, a new path should be filled.

**Type**

Boolean.

----

.. _document.defaultFilled:

document.defaultFilled
********************************************************************************

``app.activeDocument.defaultFilled``

**Description**

If ``true``, a new path should be filled.

**Type**

Boolean.

----

.. _document.defaultFilled:

document.defaultFilled
********************************************************************************

``app.activeDocument.defaultFilled``

**Description**

If ``true``, a new path should be filled.

**Type**

Boolean.

----

.. _document.defaultFillOverprint:

document.defaultFillOverprint
********************************************************************************

``app.activeDocument.defaultFillOverprint``

**Description**

If ``true``, the art beneath a filled object should be overprinted by default.

**Type**

Boolean.

----

.. _document.defaultStrokeCap:

document.defaultStrokeCap
********************************************************************************

``app.activeDocument.defaultStrokeCap``

**Description**

Default type of line capping for paths created.

**Type**

// todo: link to **StrokeCap** in Chapter 2 "Scripting Constants"

StrokeCap.

----

.. _document.defaultStrokeColor:

document.defaultStrokeColor
********************************************************************************

``app.activeDocument.defaultStrokeColor``

**Description**

The stroke color for new paths if default stroked is ``true``.

**Type**

:ref:`jsobjref/color`

----

.. _document.defaultStroked:

document.defaultStroked
********************************************************************************

``app.activeDocument.defaultStroked``

**Description**

If ``true``, a new path should be stroked.

**Type**

Boolean.

----

.. _document.defaultStrokeDashes:

document.defaultStrokeDashes
********************************************************************************

``app.activeDocument.defaultStrokeDashes``

**Description**

Default lengths for dashes and gaps in dashed lines, starting with the first dash length, followed by the first gap length, and so on. Set to an empty object, {}, for solid line.

**Type**

Object.

----

.. _document.defaultStrokeDashOffset:

document.defaultStrokeDashOffset
********************************************************************************

``app.activeDocument.defaultStrokeDashOffset``

**Description**

The default distance into the dash pattern at which the pattern should be started for new paths.

**Type**

Number (double).

----

.. _document.defaultStrokeJoin:

document.defaultStrokeJoin
********************************************************************************

``app.activeDocument.defaultStrokeJoin``

**Description**

Default type of joints in new paths.

**Type**

// todo: link to **StrokeJoin** in Chapter 2 "Scripting Constants"

StrokeJoin.

----

.. _document.defaultStrokeMiterLimit:

document.defaultStrokeMiterLimit
********************************************************************************

``app.activeDocument.defaultStrokeMiterLimit``

**Description**

When a default stroke join is set to ``mitered``, this property specifies when the join will be converted to beveled (squared-off ) by default. The default miter limit of 4 means that when the length of the point reaches four times the stroke weight, the join switches from a miter join to a bevel join. Range: 1 to 500; a value of 1 specifies a bevel join.

**Type**

Number (double).

----

.. _document.defaultStrokeOverprint:

document.defaultStrokeOverprint
********************************************************************************

``app.activeDocument.defaultStrokeOverprint``

**Description**

If ``true``, the art beneath a stroked object should be overprinted by default.

**Type**

Boolean.

----

.. _document.defaultStrokeWidth:

document.defaultStrokeWidth
********************************************************************************

``app.activeDocument.defaultStrokeWidth``

**Description**

Default width of stroke for new paths.

**Type**

Number (double).

----

.. _document.documentColorSpace:

document.documentColorSpace
********************************************************************************

``app.activeDocument.documentColorSpace``

**Description**

The color specification system to use for this document’s color space.

**Type**

// todo: link to **DocumentColorSpace** in Chapter 2 "Scripting Constants"

DocumentColorSpace, read-only.

----

.. _document.fullName:

document.fullName
********************************************************************************

``app.activeDocument.fullName``

**Description**

The file associated with the document, which includes the complete path to the file.

**Type**

File, read-only.

----

.. _document.geometricBounds:

document.geometricBounds
********************************************************************************

``app.activeDocument.geometricBounds``

**Description**

The bounds of the illustration excluding the stroke width of any objects in the document.

**Type**

Array of 4 numbers, read-only.

----

.. _document.gradients:

document.gradients
********************************************************************************

``app.activeDocument.gradients``

**Description**

The gradients contained in the document.

**Type**

:ref:`jsobjref/gradients`, read-only.

----

.. _document.graphicStyles:

document.graphicStyles
********************************************************************************

``app.activeDocument.graphicStyles``

**Description**

The graphic styles defined in this document.

**Type**

:ref:`jsobjref/graphicStyles`, read-only.

----

.. _document.graphItems:

document.graphItems
********************************************************************************

``app.activeDocument.graphItems``

**Description**

The graph art items in this document.

**Type**

:ref:`jsobjref/graphItems`, read-only.

----

.. _document.groupItems:

document.groupItems
********************************************************************************

``app.activeDocument.groupItems``

**Description**

The group items contained in the document.

**Type**

:ref:`jsobjref/groupItems`, read-only.

----

.. _document.height:

document.height
********************************************************************************

``app.activeDocument.height``

**Description**

The height of the document.

**Type**

Number (double), read-only.

----

.. _document.inkList:

document.inkList
********************************************************************************

``app.activeDocument.inkList``

**Description**

The list of inks in this document.

**Type**

Object, read-only.

----

.. _document.kinsokuSet:

document.kinsokuSet
********************************************************************************

``app.activeDocument.kinsokuSet``

**Description**

The Kinsoku set of characters that cannot begin or end a line of Japanese text.

**Type**

Object, read-only.

----










=======
Methods
=======


----

=======
Example
=======


********************************************************************************

::


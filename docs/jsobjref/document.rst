.. _jsobjref/document:

Document
################################################################################

``document``

**Description**

An Illustrator document. Documents are contained in the :ref:`jsobjref/application` object.

The default document settings—those properties starting with the word "default"—are global settings that affect the current document. Be sure to modify these default properties only when a document is open. Note that if you set default properties to desired values before creating new objects, you can streamline your scripts, eliminating the need to specify specific properties such as ``fillColor`` and ``stroked`` that have default properties.

A document’s color space, height, and width can only be set when the document is created. You cannot modify these properties in an existing document. See :ref:`jsobjref/application.open` for more information on how document color spaces are handled.

----

==========
Properties
==========

.. _jsobjref/document.activeDataset:

Document.activeDataset
********************************************************************************

``app.activeDocument.activeDataset``

**Description**

The currently opened dataset.

**Type**

:ref:`jsobjref/dataset`

----

.. _jsobjref/document.activeLayer:

Document.activeLayer
********************************************************************************

``app.activeDocument.activeLayer``

**Description**

The active layer in the document.

**Type**

:ref:`jsobjref/layer`

----

.. _jsobjref/document.activeView:

Document.activeView
********************************************************************************

``app.activeDocument.activeView``

**Description**

The document’s current view.

**Type**

:ref:`jsobjref/view`, read-only.

----

.. _jsobjref/document.artboards:

Document.artboards
********************************************************************************

``app.activeDocument.artboards``

**Description**

All artboards in the document.

**Type**

:ref:`jsobjref/artboards`, read-only.

----

.. _jsobjref/document.brushes:

Document.brushes
********************************************************************************

``app.activeDocument.brushes``

**Description**

The brushes contained in the document.

**Type**

:ref:`jsobjref/brushes`, read-only.

----

.. _jsobjref/document.characterStyles:

Document.characterStyles
********************************************************************************

``app.activeDocument.characterStyles``

**Description**

The list of character styles in this document.

**Type**

:ref:`jsobjref/characterStyles`, read-only.

----

.. _jsobjref/document.compoundPathItems:

Document.compoundPathItems
********************************************************************************

``app.activeDocument.compoundPathItems``

**Description**

The compound path items contained in the document.

**Type**

:ref:`jsobjref/compoundPathItems`, read-only.

----

.. _jsobjref/document.cropBox:

Document.cropBox
********************************************************************************

``app.activeDocument.cropBox``

**Description**

The boundary of the document’s cropping box for output, or ``null`` if no value has been set.

**Type**

Array of 4 numbers.

----

.. _jsobjref/document.cropStyle:

Document.cropStyle
********************************************************************************

``app.activeDocument.cropStyle``

**Description**

The style of the document’s cropping box.

**Type**

:ref:`jsobjref/scriptingConstants.cropOptions`

----

.. _jsobjref/document.dataSets:

Document.dataSets
********************************************************************************

``app.activeDocument.dataSets``

**Description**

The datasets contained in the document.

**Type**

:ref:`jsobjref/dataSets`, read-only.

----

.. _jsobjref/document.defaultFillColor:

Document.defaultFillColor
********************************************************************************

``app.activeDocument.defaultFillColor``

**Description**

The color to use to fill new paths if ``defaultFilled`` is ``true``.

**Type**

:ref:`jsobjref/color`

----

.. _jsobjref/document.defaultFilled:

Document.defaultFilled
********************************************************************************

``app.activeDocument.defaultFilled``

**Description**

If ``true``, a new path should be filled.

**Type**

Boolean.

----

.. _jsobjref/document.defaultFillOverprint:

Document.defaultFillOverprint
********************************************************************************

``app.activeDocument.defaultFillOverprint``

**Description**

If ``true``, the art beneath a filled object should be overprinted by default.

**Type**

Boolean.

----

.. _jsobjref/document.defaultStrokeCap:

Document.defaultStrokeCap
********************************************************************************

``app.activeDocument.defaultStrokeCap``

**Description**

Default type of line capping for paths created.

**Type**

:ref:`jsobjref/scriptingConstants.StrokeCap`

----

.. _jsobjref/document.defaultStrokeColor:

Document.defaultStrokeColor
********************************************************************************

``app.activeDocument.defaultStrokeColor``

**Description**

The stroke color for new paths if default stroked is ``true``.

**Type**

:ref:`jsobjref/color`

----

.. _jsobjref/document.defaultStroked:

Document.defaultStroked
********************************************************************************

``app.activeDocument.defaultStroked``

**Description**

If ``true``, a new path should be stroked.

**Type**

Boolean.

----

.. _jsobjref/document.defaultStrokeDashes:

Document.defaultStrokeDashes
********************************************************************************

``app.activeDocument.defaultStrokeDashes``

**Description**

Default lengths for dashes and gaps in dashed lines, starting with the first dash length, followed by the first gap length, and so on. Set to an empty object, {}, for solid line.

**Type**

Object.

----

.. _jsobjref/document.defaultStrokeDashOffset:

Document.defaultStrokeDashOffset
********************************************************************************

``app.activeDocument.defaultStrokeDashOffset``

**Description**

The default distance into the dash pattern at which the pattern should be started for new paths.

**Type**

Number (double).

----

.. _jsobjref/document.defaultStrokeJoin:

Document.defaultStrokeJoin
********************************************************************************

``app.activeDocument.defaultStrokeJoin``

**Description**

Default type of joints in new paths.

**Type**

:ref:`jsobjref/scriptingConstants.StrokeJoin`

----

.. _jsobjref/document.defaultStrokeMiterLimit:

Document.defaultStrokeMiterLimit
********************************************************************************

``app.activeDocument.defaultStrokeMiterLimit``

**Description**

When a default stroke join is set to ``mitered``, this property specifies when the join will be converted to beveled (squared-off ) by default. The default miter limit of 4 means that when the length of the point reaches four times the stroke weight, the join switches from a miter join to a bevel join. Range: 1 to 500; a value of 1 specifies a bevel join.

**Type**

Number (double).

----

.. _jsobjref/document.defaultStrokeOverprint:

Document.defaultStrokeOverprint
********************************************************************************

``app.activeDocument.defaultStrokeOverprint``

**Description**

If ``true``, the art beneath a stroked object should be overprinted by default.

**Type**

Boolean.

----

.. _jsobjref/document.defaultStrokeWidth:

Document.defaultStrokeWidth
********************************************************************************

``app.activeDocument.defaultStrokeWidth``

**Description**

Default width of stroke for new paths.

**Type**

Number (double).

----

.. _jsobjref/document.documentColorSpace:

Document.documentColorSpace
********************************************************************************

``app.activeDocument.documentColorSpace``

**Description**

The color specification system to use for this document’s color space.

**Type**

:ref:`jsobjref/scriptingConstants.documentColorSpace`

----

.. _jsobjref/document.fullName:

Document.fullName
********************************************************************************

``app.activeDocument.fullName``

**Description**

The file associated with the document, which includes the complete path to the file.

**Type**

File, read-only.

----

.. _jsobjref/document.geometricBounds:

Document.geometricBounds
********************************************************************************

``app.activeDocument.geometricBounds``

**Description**

The bounds of the illustration excluding the stroke width of any objects in the document.

**Type**

Array of 4 numbers, read-only.

----

.. _jsobjref/document.gradients:

Document.gradients
********************************************************************************

``app.activeDocument.gradients``

**Description**

The gradients contained in the document.

**Type**

:ref:`jsobjref/gradients`, read-only.

----

.. _jsobjref/document.graphicStyles:

Document.graphicStyles
********************************************************************************

``app.activeDocument.graphicStyles``

**Description**

The graphic styles defined in this document.

**Type**

:ref:`jsobjref/graphicStyles`, read-only.

----

.. _jsobjref/document.graphItems:

Document.graphItems
********************************************************************************

``app.activeDocument.graphItems``

**Description**

The graph art items in this document.

**Type**

:ref:`jsobjref/graphItems`, read-only.

----

.. _jsobjref/document.groupItems:

Document.groupItems
********************************************************************************

``app.activeDocument.groupItems``

**Description**

The group items contained in the document.

**Type**

:ref:`jsobjref/groupItems`, read-only.

----

.. _jsobjref/document.height:

Document.height
********************************************************************************

``app.activeDocument.height``

**Description**

The height of the document.

**Type**

Number (double), read-only.

----

.. _jsobjref/document.inkList:

Document.inkList
********************************************************************************

``app.activeDocument.inkList``

**Description**

The list of inks in this document.

**Type**

Object, read-only.

----

.. _jsobjref/document.kinsokuSet:

Document.kinsokuSet
********************************************************************************

``app.activeDocument.kinsokuSet``

**Description**

The Kinsoku set of characters that cannot begin or end a line of Japanese text.

**Type**

Object, read-only.

----

.. _jsobjref/document.layers:

Document.layers
********************************************************************************

``app.activeDocument.layers``

**Description**

The layers contained in the document.

**Type**

:ref:`jsobjref/layers`, read-only.

----

.. _jsobjref/document.legacyTextItems:

Document.legacyTextItems
********************************************************************************

``app.activeDocument.legacyTextItems``

**Description**

The legacy text items in the document.

**Type**

:ref:`jsobjref/legacyTextItems`, read-only.

----

.. _jsobjref/document.meshItems:

Document.meshItems
********************************************************************************

``app.activeDocument.meshItems``

**Description**

The mesh art items contained in the document.

**Type**

:ref:`jsobjref/meshItems`, read-only.

----

.. _jsobjref/document.mojikumiSet:

Document.mojikumiSet
********************************************************************************

``app.activeDocument.mojikumiSet``

**Description**

A list of names of predefined Mojikumi sets which specify the spacing for the layout and composition of Japanese text.

**Type**

Object, read-only.

----

.. _jsobjref/document.name:

Document.name
********************************************************************************

``app.activeDocument.name``

**Description**

The document’s name (not the complete file path to the document).

**Type**

String, read-only.

----

.. _jsobjref/document.nonNativeItems:

Document.nonNativeItems
********************************************************************************

``app.activeDocument.nonNativeItems``

**Description**

The non-native art items in this document.

**Type**

:ref:`jsobjref/nonNativeItems`, read-only.

----

.. _jsobjref/document.outputResolution:

Document.outputResolution
********************************************************************************

``app.activeDocument.outputResolution``

**Description**

The current output resolution for the document in dots per inch (dpi).

**Type**

Number (double), read-only.

----

.. _jsobjref/document.pageItems:

Document.pageItems
********************************************************************************

``app.activeDocument.pageItems``

**Description**

The page items (all art item classes) contained in the document.

**Type**

:ref:`jsobjref/pageItems`, read-only.

----

.. _jsobjref/document.pageOrigin:

Document.pageOrigin
********************************************************************************

``app.activeDocument.pageOrigin``

**Description**

The zero-point of the page in the document without margins, relative to the overall height and width.

**Type**

Array of 2 numbers.

----

.. _jsobjref/document.paragraphStyles:

Document.paragraphStyles
********************************************************************************

``app.activeDocument.paragraphStyles``

**Description**

The list of paragraph styles in this document.

**Type**

:ref:`jsobjref/paragraphStyles`, read-only.

----

.. _jsobjref/document.parent:

Document.parent
********************************************************************************

``app.activeDocument.parent``

**Description**

The application that contains this document.

**Type**

:ref:`jsobjref/application`, read-only.

----

.. _jsobjref/document.path:

Document.path
********************************************************************************

``app.activeDocument.path``

**Description**

The file associated with the document, which includes the complete path to the file.

**Type**

File, read-only.

----

.. _jsobjref/document.pathItems:

Document.pathItems
********************************************************************************

``app.activeDocument.pathItems``

**Description**

The path items contained in this document.

**Type**

:ref:`jsobjref/pathItems`, read-only.

----

.. _jsobjref/document.patterns:

Document.patterns
********************************************************************************

``app.activeDocument.patterns``

**Description**

The patterns contained in this document.

**Type**

:ref:`jsobjref/patterns`, read-only.

----

.. _jsobjref/document.placedItems:

Document.placedItems
********************************************************************************

``app.activeDocument.placedItems``

**Description**

The placed items contained in this document.

**Type**

:ref:`jsobjref/placedItems`, read-only.

----

.. _jsobjref/document.pluginItems:

Document.pluginItems
********************************************************************************

``app.activeDocument.pluginItems``

**Description**

The plug-in items contained in this document.

**Type**

:ref:`jsobjref/pluginItems`, read-only.

----

.. _jsobjref/document.printTiles:

Document.printTiles
********************************************************************************

``app.activeDocument.printTiles``

**Description**

If ``true``, this document should be printed as tiled output.

**Type**

Boolean, read-only.

----

.. _jsobjref/document.rasterEffectSettings:

Document.rasterEffectSettings
********************************************************************************

``app.activeDocument.rasterEffectSettings``

**Description**

The document’s raster effect settings.

**Type**

:ref:`jsobjref/rasterEffectOptions`, read-only.

----

.. _jsobjref/document.rasterItems:

Document.rasterItems
********************************************************************************

``app.activeDocument.rasterItems``

**Description**

The raster items contained in this document.

**Type**

:ref:`jsobjref/rasterItems`, read-only.

----

.. _jsobjref/document.rulerOrigin:

Document.rulerOrigin
********************************************************************************

``app.activeDocument.rulerOrigin``

**Description**

The zero-point of the rulers in the document relative to the bottom left of the document.

**Type**

Array of 2 numbers.

----

.. _jsobjref/document.rulerUnits:

Document.rulerUnits
********************************************************************************

``app.activeDocument.rulerUnits``

**Description**

The default measurement units for the rulers in the document.

**Type**

:ref:`jsobjref/scriptingConstants.RulerUnits`, read-only.

----

.. _jsobjref/document.saved:

Document.saved
********************************************************************************

``app.activeDocument.saved``

**Description**

If ``true``, the document has not been changed since last time it was saved.

**Type**

Boolean.

----

.. _jsobjref/document.selection:

Document.selection
********************************************************************************

``app.activeDocument.selection``

**Description**

References to the objects in this document’s current selection, or ``null`` when nothing is selected.

A reference to an insertion point is returned when there is an active insertion point in the contents of a selected text art item. Similarly, a reference to a range of text is returned when characters are selected in the contents of a text art item.

**Type**

Array of objects.

----

.. _jsobjref/document.showPlacedImages:

Document.showPlacedImages
********************************************************************************

``app.activeDocument.showPlacedImages``

**Description**

If ``true``, placed images should be displayed in the document.

**Type**

Boolean, read-only.

----

.. _jsobjref/document.splitLongPaths:

Document.splitLongPaths
********************************************************************************

``app.activeDocument.splitLongPaths``

**Description**

If ``true``, long paths should be split when printing.

**Type**

Boolean, read-only.

----

.. _jsobjref/document.spots:

Document.spots
********************************************************************************

``app.activeDocument.spots``

**Description**

The spot colors contained in this document.

**Type**

:ref:`jsobjref/spots`, read-only.

----

.. _jsobjref/document.stationery:

Document.stationery
********************************************************************************

``app.activeDocument.stationery``

**Description**

If ``true``, the file is a stationery file.

**Type**

Boolean, read-only.

----

.. _jsobjref/document.stories:

Document.stories
********************************************************************************

``app.activeDocument.stories``

**Description**

The story items in this document.

**Type**

:ref:`jsobjref/stories`, read-only.

----

.. _jsobjref/document.swatches:

Document.swatches
********************************************************************************

``app.activeDocument.swatches``

**Description**

The swatches in this document.

**Type**

:ref:`jsobjref/swatches`, read-only.

----

.. _jsobjref/document.swatchGroups:

Document.swatchGroups
********************************************************************************

``app.activeDocument.swatchGroups``

**Description**

The swatch groups in this document.

**Type**

:ref:`jsobjref/swatchGroups`, read-only.

----

.. _jsobjref/document.symbolItems:

Document.symbolItems
********************************************************************************

``app.activeDocument.symbolItems``

**Description**

The art items in the document linked to symbols.

**Type**

:ref:`jsobjref/symbolItems`, read-only.

----

.. _jsobjref/document.symbols:

Document.symbols
********************************************************************************

``app.activeDocument.symbols``

**Description**

The symbols in this document.

**Type**

:ref:`jsobjref/symbols`, read-only.

----

.. _jsobjref/document.tags:

Document.tags
********************************************************************************

``app.activeDocument.tags``

**Description**

The tags in this document.

**Type**

:ref:`jsobjref/tags`, read-only.

----

.. _jsobjref/document.textFrames:

Document.textFrames
********************************************************************************

``app.activeDocument.textFrames``

**Description**

The text frames in this document.

**Type**

:ref:`jsobjref/textFrameItems`, read-only.

----

.. _jsobjref/document.tileFullPages:

Document.tileFullPages
********************************************************************************

``app.activeDocument.tileFullPages``

**Description**

If ``true``, full pages should be tiled when printing this document.

**Type**

Boolean, read-only.

----

.. _jsobjref/document.typename:

Document.typename
********************************************************************************

``app.activeDocument.typename``

**Description**

The class name of the referenced object.

**Type**

String, read-only.

----

.. _jsobjref/document.useDefaultScreen:

Document.useDefaultScreen
********************************************************************************

``app.activeDocument.useDefaultScreen``

**Description**

If ``true``, the printer’s default screen should be used when printing this document.

**Type**

Boolean, read-only.

----

.. _jsobjref/document.variables:

Document.variables
********************************************************************************

``app.activeDocument.variables``

**Description**

The variables defined in this document.

**Type**

:ref:`jsobjref/variables`, read-only.

----

.. _jsobjref/document.variablesLocked:

Document.variablesLocked
********************************************************************************

``app.activeDocument.variablesLocked``

**Description**

If true, the variables are locked.

**Type**

Boolean.

----

.. _jsobjref/document.views:

Document.views
********************************************************************************

``app.activeDocument.views``

**Description**

The views contained in this document.

**Type**

:ref:`jsobjref/views`, read-only.

----

.. _jsobjref/document.visibleBounds:

Document.visibleBounds
********************************************************************************

``app.activeDocument.visibleBounds``

**Description**

The visible bounds of the document, including stroke width of any objects in the illustration.

**Type**

Array of 4 numbers, read-only.

----

.. _jsobjref/document.width:

Document.width
********************************************************************************

``app.activeDocument.width``

**Description**

The width of this document.

**Type**

Number (double), read-only.

----

.. _jsobjref/document.XMPString:

Document.XMPString
********************************************************************************

``app.activeDocument.XMPString``

**Description**

The XMP metadata packet associated with this document.

**Type**

String.

----

=======
Methods
=======

.. _jsobjref/document.activate:

Document.activate()
********************************************************************************

``app.activeDocument.activate()``

**Description**

Brings the first window associated with the document to the front.

**Returns**

Nothing.

----

.. _jsobjref/document.arrange:

Document.arrange()
********************************************************************************

``app.activeDocument.arrange([layoutStyle])``

**Description**

Arranges multiple documents in the given layout style.

**Parameters**

+-------------------+------------------------------------------------------------------+-------------+
|     Parameter     |                               Type                               | Description |
+===================+==================================================================+=============+
| ``[layoutStyle]`` | :ref:`jsobjref/scriptingConstants.DocumentLayoutStyle`, optional | todo        |
+-------------------+------------------------------------------------------------------+-------------+

**Returns**

Boolean.

----

.. _jsobjref/document.close:

Document.close()
********************************************************************************

``app.activeDocument.close([saveOptions])``

**Description**

Closes a document using specified save options.

When you close a document, you should set your document reference to ``null`` to prevent your script from accidentally trying to access closed documents.

**Parameters**

+-------------------+------------------------------------------------+-------------+
|     Parameter     |                      Type                      | Description |
+===================+================================================+=============+
| ``[saveOptions]`` | :ref:`jsobjref/scriptingConstants.SaveOptions` | todo        |
+-------------------+------------------------------------------------+-------------+

**Returns**

Nothing.

----

.. _jsobjref/document.closeNoUI:

Document.closeNoUI()
********************************************************************************

``app.activeDocument.closeNoUI()``

**Description**

Closes the specified non-UI document.

**Returns**

Nothing.

----

.. _jsobjref/document.convertCoordinate:

Document.convertCoordinate()
********************************************************************************

``app.activeDocument.convertCoordinate(coordinate, source, destination)``

**Description**

Converts the given point between artboard and document coordinate systems. Returns the converted point coordinates.

**Parameters**

+-----------------+-----------------------------------------------------+-------------+
|    Parameter    |                        Type                         | Description |
+=================+=====================================================+=============+
| ``coordinate``  | Point                                               | todo        |
+-----------------+-----------------------------------------------------+-------------+
| ``source``      | :ref:`jsobjref/scriptingConstants.coordinateSystem` | todo        |
+-----------------+-----------------------------------------------------+-------------+
| ``destination`` | :ref:`jsobjref/scriptingConstants.coordinateSystem` | todo        |
+-----------------+-----------------------------------------------------+-------------+

**Returns**

Point.

----

.. _jsobjref/document.exportFile:

Document.exportFile()
********************************************************************************

``app.activeDocument.exportFile(exportFile, exportFormat [,options])``

**Description**

Exports the document to the specified file using one of the predefined export file formats. The appropriate file extension is automatically appended to the file name, except for Photoshop® documents. For these, you must include the file extension (PSD) in the file specification.

**Parameters**

+------------------+-----------------------------------------------+-------------+
|    Parameter     |                     Type                      | Description |
+==================+===============================================+=============+
| ``exportFile``   | File                                          | todo        |
+------------------+-----------------------------------------------+-------------+
| ``exportFormat`` | :ref:`jsobjref/scriptingConstants.exportType` | todo        |
+------------------+-----------------------------------------------+-------------+
| ``[options]``    | Variant, optional                             | todo        |
+------------------+-----------------------------------------------+-------------+

**Returns**

Nothing.

----

.. _jsobjref/document.exportPDFPreset:

Document.exportPDFPreset()
********************************************************************************

``app.activeDocument.exportPDFPreset(file)``

**Description**

Exports the current PDF preset values to the file.

**Parameters**

+-----------+------+-------------+
| Parameter | Type | Description |
+===========+======+=============+
| ``file``  | File | todo        |
+-----------+------+-------------+

**Returns**

Nothing.

----

.. _jsobjref/document.exportPerspectiveGridPreset:

Document.exportPerspectiveGridPreset()
********************************************************************************

``app.activeDocument.exportPerspectiveGridPreset(file)``

**Description**

Exports the current perspective grid preset values to the file.

**Parameters**

+-----------+------+-------------+
| Parameter | Type | Description |
+===========+======+=============+
| ``file``  | File | todo        |
+-----------+------+-------------+

**Returns**

Nothing.

----

.. _jsobjref/document.exportPrintPreset:

Document.exportPrintPreset()
********************************************************************************

``app.activeDocument.exportPrintPreset(file)``

**Description**

Exports the current print preset values to the file.

**Parameters**

+-----------+------+-------------+
| Parameter | Type | Description |
+===========+======+=============+
| ``file``  | File | todo        |
+-----------+------+-------------+

**Returns**

Nothing.

----

.. _jsobjref/document.exportVariables:

Document.exportVariables()
********************************************************************************

``app.activeDocument.exportVariables(fileSpec)``

**Description**

Saves datasets into an XML library. The datasets contain variables and their associated dynamic data.

**Parameters**

+--------------+------+-------------+
|  Parameter   | Type | Description |
+==============+======+=============+
| ``fileSpec`` | File | todo        |
+--------------+------+-------------+

**Returns**

Nothing.

----

.. _jsobjref/document.fitArtboardToSelectedArt:

Document.fitArtboardToSelectedArt()
********************************************************************************

``app.activeDocument.fitArtboardToSelectedArt([index])``

**Description**

Resizes the artboard at the given index to fit currently selected art. Index default is 0. Returns ``true`` on success.

**Parameters**

+-------------+-------------------------+-------------+
|  Parameter  |          Type           | Description |
+=============+=========================+=============+
| ``[index]`` | Number (long), optional | todo        |
+-------------+-------------------------+-------------+

**Returns**

Boolean.

----

.. _jsobjref/document.getPerspectiveActivePlane:

Document.getPerspectiveActivePlane()
********************************************************************************

``app.activeDocument.getPerspectiveActivePlane()``

**Description**

Retrieves the active plane of the active perspective grid of the document.

**Returns**

:ref:`jsobjref/scriptingConstants.PerspectiveGridPlaneType`

----

.. _jsobjref/document.hidePerspectiveGrid:

Document.hidePerspectiveGrid()
********************************************************************************

``app.activeDocument.hidePerspectiveGrid()``

**Description**

Hides the current active grid for the document. If no grid is visible, does nothing. Returns ``true`` if a grid is hidden.

**Returns**

Boolean.

----

.. _jsobjref/document.imageCapture:

Document.imageCapture()
********************************************************************************

``app.activeDocument.imageCapture(imageFile [,clipBounds] [,options])``

**Description**

Captures the artwork content within the clipping boundaries in this document as a raster image, and writes the image data to a specified file.

If the bounds parameter is omitted, captures the entire artwork.

**Parameters**

+------------------+-----------------------------------------------+-------------+
|    Parameter     |                     Type                      | Description |
+==================+===============================================+=============+
| ``imageFile``    | File                                          | todo        |
+------------------+-----------------------------------------------+-------------+
| ``[clipBounds]`` | Rect, optional                                | todo        |
+------------------+-----------------------------------------------+-------------+
| ``[options]``    | :ref:`jsobjref/imageCaptureOptions`, optional | todo        |
+------------------+-----------------------------------------------+-------------+

**Returns**

Nothing.

----

.. _jsobjref/document.importCharacterStyles:

Document.importCharacterStyles()
********************************************************************************

``app.activeDocument.importCharacterStyles(fileSpec)``

**Description**

Loads the character styles from the Illustrator file.

**Parameters**

+--------------+------+-------------+
|  Parameter   | Type | Description |
+==============+======+=============+
| ``fileSpec`` | File | todo        |
+--------------+------+-------------+

**Returns**

Nothing.

----

.. _jsobjref/document.importParagraphStyles:

Document.importParagraphStyles()
********************************************************************************

``app.activeDocument.importParagraphStyles(fileSpec)``

**Description**

Loads the paragraph styles from the Illustrator file.

**Parameters**

+--------------+------+-------------+
|  Parameter   | Type | Description |
+==============+======+=============+
| ``fileSpec`` | File | todo        |
+--------------+------+-------------+

**Returns**

Nothing.

----

.. _jsobjref/document.importPDFPreset:

Document.importPDFPreset()
********************************************************************************

``app.activeDocument.importPDFPreset(fileSpec [, replacingPreset])``

**Description**

Loads all PDF presets from a file.

**Parameters**

+-----------------------+------------------+-------------+
|       Parameter       |       Type       | Description |
+=======================+==================+=============+
| ``fileSpec``          | File             | todo        |
+-----------------------+------------------+-------------+
| ``[replacingPreset]`` | String, optional | todo        |
+-----------------------+------------------+-------------+

**Returns**

Nothing.

----

.. _jsobjref/document.importPrintPreset:

Document.importPrintPreset()
********************************************************************************

``app.activeDocument.importPrintPreset(printPreset, fileSpec)``

**Description**

Loads the named print preset from the file.

**Parameters**

+-----------------+--------+-------------+
|    Parameter    |  Type  | Description |
+=================+========+=============+
| ``printPreset`` | String | todo        |
+-----------------+--------+-------------+
| ``fileSpec``    | File   | todo        |
+-----------------+--------+-------------+

**Returns**

Nothing.

----

.. _jsobjref/document.importVariables:

Document.importVariables()
********************************************************************************

``app.activeDocument.importVariables(fileSpec)``

**Description**

Imports a library containing datasets, variables, and their associated dynamic data. Importing variables overwrites existing variables and datasets.

**Parameters**

+--------------+------+-------------+
|  Parameter   | Type | Description |
+==============+======+=============+
| ``fileSpec`` | File | todo        |
+--------------+------+-------------+

**Returns**

Nothing.

----

.. _jsobjref/document.print:

Document.print()
********************************************************************************

``app.activeDocument.print([options])``

**Description**

Prints the document.

**Parameters**

+---------------+----------------------------------------+-------------+
|   Parameter   |                  Type                  | Description |
+===============+========================================+=============+
| ``[options]`` | :ref:`jsobjref/printOptions`, optional | todo        |
+---------------+----------------------------------------+-------------+

**Returns**

Nothing.

----

.. _jsobjref/document.rasterize:

Document.rasterize()
********************************************************************************

``app.activeDocument.rasterize(sourceArt [, clipBounds] [, options])``

**Description**

Rasterizes the source art(s) within the specified clip bounds. The source art(s) is disposed of as a result of the rasterization.

**Parameters**

+------------------+--------------------------------------------+-------------+
|    Parameter     |                    Type                    | Description |
+==================+============================================+=============+
| ``sourceArt``    | Variant                                    | todo        |
+------------------+--------------------------------------------+-------------+
| ``[clipBounds]`` | Rect, optional                             | todo        |
+------------------+--------------------------------------------+-------------+
| ``[options]``    | :ref:`jsobjref/rasterizeOptions`, optional | todo        |
+------------------+--------------------------------------------+-------------+

**Returns**

:ref:`jsobjref/rasterItem`

----

.. _jsobjref/document.rearrangeArboards:

Document.rearrangeArboards()
********************************************************************************

``app.activeDocument.rearrangeArboards([artboardLayout] [, artboardRowsOrCols] [, artboardSpacing] [, artboardMoveArtwork])``

**Description**

Rearranges artboards in the document. All arguments are optional. Default layout style is ``DocumentArtboard Layout.GridByRow``.

The second argument specifies the number of rows or columns, as appropriate for the chosen layout style, in the range ``[1..docNumArtboards-1]``, or 1 (the default) for single row/column layouts.

Spacing is a number of pixels, default 20.

When last argument is true (the default), artwork is moved with the artboards.

**Parameters**

+---------------------------+---------------------------------------------------------------------+-------------+
|         Parameter         |                                Type                                 | Description |
+===========================+=====================================================================+=============+
| ``[artboardLayout]``      | :ref:`jsobjref/scriptingConstants.documentArtboardLayout`, optional | todo        |
+---------------------------+---------------------------------------------------------------------+-------------+
| ``[artboardRowsOrCols]``  | Integer, optional                                                   | todo        |
+---------------------------+---------------------------------------------------------------------+-------------+
| ``[artboardSpacing]``     | Number, optional                                                    | todo        |
+---------------------------+---------------------------------------------------------------------+-------------+
| ``[artboardMoveArtwork]`` | Boolean, optional                                                   | todo        |
+---------------------------+---------------------------------------------------------------------+-------------+

**Returns**

Boolean.

----

.. _jsobjref/document.save:

Document.save()
********************************************************************************

``app.activeDocument.save()``

**Description**

Saves the document in it current location.

**Returns**

Nothing.

----

.. _jsobjref/document.saveAs:

Document.saveAs()
********************************************************************************

``app.activeDocument.saveAs(saveIn [, options])``

**Description**

Saves the document in the specified file as an Illustrator, EPS, or PDF file.

**Parameters**

+---------------+----------------------------------------------------------+-------------+
|   Parameter   |                           Type                           | Description |
+===============+==========================================================+=============+
| ``saveIn``    | File                                                     | todo        |
+---------------+----------------------------------------------------------+-------------+
| ``[options]`` | :ref:`jsobjref/scriptingConstants.SaveOptions`, optional | todo        |
+---------------+----------------------------------------------------------+-------------+

**Returns**

Nothing.

----

.. _jsobjref/document.saveNoUI:

Document.saveNoUI()
********************************************************************************

``app.activeDocument.saveNoUI(saveIn)``

**Description**

Saves the non-UI document at the specified path

**Parameters**

+------------+------+-------------+
| Parameter  | Type | Description |
+============+======+=============+
| ``saveIn`` | File | todo        |
+------------+------+-------------+

**Returns**

Nothing.

----

.. _jsobjref/document.selectObjectsOnActiveArtboard:

Document.selectObjectsOnActiveArtboard()
********************************************************************************

``app.activeDocument.selectObjectsOnActiveArtboard()``

**Description**

Selects the objects on the currently active artboard. Returns ``true`` on success.

**Returns**

Boolean.

----

.. _jsobjref/document.setActivePlane:

Document.setActivePlane()
********************************************************************************

``app.activeDocument.setActivePlane(gridPlane)``

**Description**

Sets the active plane of the active perspective grid of the document. Returns ``true`` on success.

**Parameters**

+---------------+-------------------------------------------------------------+-------------+
|   Parameter   |                            Type                             | Description |
+===============+=============================================================+=============+
| ``gridPlane`` | :ref:`jsobjref/scriptingConstants.PerspectiveGridPlaneType` | todo        |
+---------------+-------------------------------------------------------------+-------------+

**Returns**

Boolean.

----

.. _jsobjref/document.selectPerspectivePreset:

Document.selectPerspectivePreset()
********************************************************************************

``app.activeDocument.selectPerspectivePreset(gridType, presetName)``

**Description**

Selects a predefined preset to define grid for the current document. Returns ``true`` on success.

**Parameters**

+----------------+--------------------------------------------------------+-------------+
|   Parameter    |                          Type                          | Description |
+================+========================================================+=============+
| ``gridType``   | :ref:`jsobjref/scriptingConstants.PerspectiveGridType` | todo        |
+----------------+--------------------------------------------------------+-------------+
| ``presetName`` | String                                                 | todo        |
+----------------+--------------------------------------------------------+-------------+

**Returns**

Boolean.

----

.. _jsobjref/document.showPerspectiveGrid:

Document.showPerspectiveGrid()
********************************************************************************

``app.activeDocument.showPerspectiveGrid()``

**Description**

Shows the current active grid for the document, or if no grid is active, shows the default grid. Returns ``true`` on success.

**Returns**

Boolean.

----

.. _jsobjref/document.windowCapture:

Document.windowCapture()
********************************************************************************

``app.activeDocument.windowCapture(imageFile, windowSize)``

**Description**

Captures the current document window to the target TIFF image file.

**Parameters**

+----------------+--------------------+-------------+
|   Parameter    |        Type        | Description |
+================+====================+=============+
| ``imageFile``  | File               | todo        |
+----------------+--------------------+-------------+
| ``windowSize`` | Array of 2 numbers | todo        |
+----------------+--------------------+-------------+

**Returns**

Nothing.

----

=======
Example
=======

Deselecting all objects in the current document
********************************************************************************

.. note::
    The frontmost document can be referred to as either ``activeDocument`` or ``documents[0]``.

::

    var docRef = activeDocument;
    docRef.selection = null;

----

Closing a document
********************************************************************************

::

    // Closes the active document without saving changes
    if ( app.documents.length > 0 ) {
        var aiDocument = app.activeDocument;
        aiDocument.close( SaveOptions.DONOTSAVECHANGES );
        aiDocument = null;
    }

----

Creating a document with defaults
********************************************************************************

::

    // Creates a new document if none exists then sets fill and stroke defaults to true
    if ( app.documents.length == 0 ) {
        var doc = app.documents.add();
    } else {
        var doc = app.activeDocument;
    }

    doc.defaultFilled = true;
    doc.defaultStroked = true;

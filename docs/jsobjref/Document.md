# Document

`app.activeDocument`

**Description**

An Illustrator document. Documents are contained in the [Application](./Application.md) object.

The default document settings—those properties starting with the word "default"—are global settings that affect the current document. Be sure to modify these default properties only when a document is open. Note that if you set default properties to desired values before creating new objects, you can streamline your scripts, eliminating the need to specify specific properties such as `fillColor` and `stroked` that have default properties.

A document's color space, height, and width can only be set when the document is created. You cannot modify these properties in an existing document. See [Application.open()](Application.md#jsobjref-application-open) for more information on how document color spaces are handled.

---

## Properties

### Document.activeDataset

`app.activeDocument.activeDataset`

**Description**

The currently opened dataset.

**Type**

[Dataset](./Dataset.md)

---

### Document.activeLayer

`app.activeDocument.activeLayer`

**Description**

The active layer in the document.

**Type**

[Layer](./Layer.md)

---

### Document.activeView

`app.activeDocument.activeView`

**Description**

The document's current view.

**Type**

[View](./View.md), read-only.

---

### Document.artboards

`app.activeDocument.artboards`

**Description**

All artboards in the document.

**Type**

[Artboards](./Artboards.md), read-only.

---

### Document.brushes

`app.activeDocument.brushes`

**Description**

The brushes contained in the document.

**Type**

[Brushes](./Brushes.md), read-only.

---

### Document.characterStyles

`app.activeDocument.characterStyles`

**Description**

The list of character styles in this document.

**Type**

[CharacterStyles](./CharacterStyles.md), read-only.

---

### Document.compoundPathItems

`app.activeDocument.compoundPathItems`

**Description**

The compound path items contained in the document.

**Type**

[CompoundPathItems](./CompoundPathItems.md), read-only.

---

### Document.cropBox

`app.activeDocument.cropBox`

**Description**

The boundary of the document's cropping box for output, or `null` if no value has been set.

**Type**

Array of 4 numbers.

---

### Document.cropStyle

`app.activeDocument.cropStyle`

**Description**

The style of the document's cropping box.

**Type**

[CropOptions](scripting-constants.md#jsobjref-scripting-constants-cropoptions)

---

### Document.dataSets

`app.activeDocument.dataSets`

**Description**

The datasets contained in the document.

**Type**

[Datasets](./Datasets.md), read-only.

---

### Document.defaultFillColor

`app.activeDocument.defaultFillColor`

**Description**

The color to use to fill new paths if `defaultFilled` is `true`.

**Type**

[Color](./Color.md)

---

### Document.defaultFilled

`app.activeDocument.defaultFilled`

**Description**

If `true`, a new path should be filled.

**Type**

Boolean.

---

### Document.defaultFillOverprint

`app.activeDocument.defaultFillOverprint`

**Description**

If `true`, the art beneath a filled object should be overprinted by default.

**Type**

Boolean.

---

### Document.defaultStrokeCap

`app.activeDocument.defaultStrokeCap`

**Description**

Default type of line capping for paths created.

**Type**

[StrokeCap](scripting-constants.md#jsobjref-scripting-constants-strokecap)

---

### Document.defaultStrokeColor

`app.activeDocument.defaultStrokeColor`

**Description**

The stroke color for new paths if default stroked is `true`.

**Type**

[Color](./Color.md)

---

### Document.defaultStroked

`app.activeDocument.defaultStroked`

**Description**

If `true`, a new path should be stroked.

**Type**

Boolean.

---

### Document.defaultStrokeDashes

`app.activeDocument.defaultStrokeDashes`

**Description**

Default lengths for dashes and gaps in dashed lines, starting with the first dash length, followed by the first gap length, and so on. Set to an empty object, {}, for solid line.

**Type**

Object.

---

### Document.defaultStrokeDashOffset

`app.activeDocument.defaultStrokeDashOffset`

**Description**

The default distance into the dash pattern at which the pattern should be started for new paths.

**Type**

Number (double).

---

### Document.defaultStrokeJoin

`app.activeDocument.defaultStrokeJoin`

**Description**

Default type of joints in new paths.

**Type**

[StrokeJoin](scripting-constants.md#jsobjref-scripting-constants-strokejoin)

---

### Document.defaultStrokeMiterLimit

`app.activeDocument.defaultStrokeMiterLimit`

**Description**

When a default stroke join is set to `mitered`, this property specifies when the join will be converted to beveled (squared-off ) by default. The default miter limit of 4 means that when the length of the point reaches four times the stroke weight, the join switches from a miter join to a bevel join. Range: 1 to 500; a value of 1 specifies a bevel join.

**Type**

Number (double).

---

### Document.defaultStrokeOverprint

`app.activeDocument.defaultStrokeOverprint`

**Description**

If `true`, the art beneath a stroked object should be overprinted by default.

**Type**

Boolean.

---

### Document.defaultStrokeWidth

`app.activeDocument.defaultStrokeWidth`

**Description**

Default width of stroke for new paths.

**Type**

Number (double).

---

### Document.documentColorSpace

`app.activeDocument.documentColorSpace`

**Description**

The color specification system to use for this document's color space.

**Type**

[DocumentColorSpace](scripting-constants.md#jsobjref-scripting-constants-documentcolorspace)

---

### Document.fullName

`app.activeDocument.fullName`

**Description**

The file associated with the document, which includes the complete path to the file.

**Type**

File, read-only.

---

### Document.geometricBounds

`app.activeDocument.geometricBounds`

**Description**

The bounds of the illustration excluding the stroke width of any objects in the document.

**Type**

Array of 4 numbers, read-only.

---

### Document.gradients

`app.activeDocument.gradients`

**Description**

The gradients contained in the document.

**Type**

[Gradients](./Gradients.md), read-only.

---

### Document.graphicStyles

`app.activeDocument.graphicStyles`

**Description**

The graphic styles defined in this document.

**Type**

[GraphicStyles](./GraphicStyles.md), read-only.

---

### Document.graphItems

`app.activeDocument.graphItems`

**Description**

The graph art items in this document.

**Type**

[GraphItems](./GraphItems.md), read-only.

---

### Document.groupItems

`app.activeDocument.groupItems`

**Description**

The group items contained in the document.

**Type**

[GroupItems](./GroupItems.md), read-only.

---

### Document.height

`app.activeDocument.height`

**Description**

The height of the document.

**Type**

Number (double), read-only.

---

### Document.inkList

`app.activeDocument.inkList`

**Description**

The list of inks in this document.

**Type**

Object, read-only.

---

### Document.kinsokuSet

`app.activeDocument.kinsokuSet`

**Description**

The Kinsoku set of characters that cannot begin or end a line of Japanese text.

**Type**

Object, read-only.

---

### Document.layers

`app.activeDocument.layers`

**Description**

The layers contained in the document.

**Type**

[Layers](./Layers.md), read-only.

---

### Document.legacyTextItems

`app.activeDocument.legacyTextItems`

**Description**

The legacy text items in the document.

**Type**

[LegacyTextItems](./LegacyTextItems.md), read-only.

---

### Document.meshItems

`app.activeDocument.meshItems`

**Description**

The mesh art items contained in the document.

**Type**

[MeshItems](./MeshItems.md), read-only.

---

### Document.mojikumiSet

`app.activeDocument.mojikumiSet`

**Description**

A list of names of predefined Mojikumi sets which specify the spacing for the layout and composition of Japanese text.

**Type**

Object, read-only.

---

### Document.name

`app.activeDocument.name`

**Description**

The document's name (not the complete file path to the document).

**Type**

String, read-only.

---

### Document.nonNativeItems

`app.activeDocument.nonNativeItems`

**Description**

The non-native art items in this document.

**Type**

[NonNativeItems](./NonNativeItems.md), read-only.

---

### Document.outputResolution

`app.activeDocument.outputResolution`

**Description**

The current output resolution for the document in dots per inch (dpi).

**Type**

Number (double), read-only.

---

### Document.pageItems

`app.activeDocument.pageItems`

**Description**

The page items (all art item classes) contained in the document.

**Type**

[PageItems](./PageItems.md), read-only.

---

### Document.pageOrigin

`app.activeDocument.pageOrigin`

**Description**

The zero-point of the page in the document without margins, relative to the overall height and width.

**Type**

Array of 2 numbers.

---

### Document.paragraphStyles

`app.activeDocument.paragraphStyles`

**Description**

The list of paragraph styles in this document.

**Type**

[ParagraphStyles](./ParagraphStyles.md), read-only.

---

### Document.parent

`app.activeDocument.parent`

**Description**

The application that contains this document.

**Type**

[Application](./Application.md), read-only.

---

### Document.path

`app.activeDocument.path`

**Description**

The file associated with the document, which includes the complete path to the file.

**Type**

File, read-only.

---

### Document.pathItems

`app.activeDocument.pathItems`

**Description**

The path items contained in this document.

**Type**

[PathItems](./PathItems.md), read-only.

---

### Document.patterns

`app.activeDocument.patterns`

**Description**

The patterns contained in this document.

**Type**

[Patterns](./Patterns.md), read-only.

---

### Document.placedItems

`app.activeDocument.placedItems`

**Description**

The placed items contained in this document.

**Type**

[PlacedItems](./PlacedItems.md), read-only.

---

### Document.pluginItems

`app.activeDocument.pluginItems`

**Description**

The plug-in items contained in this document.

**Type**

[PluginItems](./PluginItems.md), read-only.

---

### Document.printTiles

`app.activeDocument.printTiles`

**Description**

If `true`, this document should be printed as tiled output.

**Type**

Boolean, read-only.

---

### Document.rasterEffectSettings

`app.activeDocument.rasterEffectSettings`

**Description**

The document's raster effect settings.

**Type**

[RasterEffectOptions](./RasterEffectOptions.md), read-only.

---

### Document.rasterItems

`app.activeDocument.rasterItems`

**Description**

The raster items contained in this document.

**Type**

[RasterItems](./RasterItems.md), read-only.

---

### Document.rulerOrigin

`app.activeDocument.rulerOrigin`

**Description**

The zero-point of the rulers in the document relative to the bottom left of the document.

**Type**

Array of 2 numbers.

---

### Document.rulerUnits

`app.activeDocument.rulerUnits`

**Description**

The default measurement units for the rulers in the document.

**Type**

[RulerUnits](scripting-constants.md#jsobjref-scripting-constants-rulerunits), read-only.

---

### Document.saved

`app.activeDocument.saved`

**Description**

If `true`, the document has not been changed since last time it was saved.

**Type**

Boolean.

---

### Document.selection

`app.activeDocument.selection`

**Description**

References to the objects in this document's current selection, or `null` when nothing is selected.

A reference to an insertion point is returned when there is an active insertion point in the contents of a selected text art item. Similarly, a reference to a range of text is returned when characters are selected in the contents of a text art item.

**Type**

Array of objects.

---

### Document.showPlacedImages

`app.activeDocument.showPlacedImages`

**Description**

If `true`, placed images should be displayed in the document.

**Type**

Boolean, read-only.

---

### Document.splitLongPaths

`app.activeDocument.splitLongPaths`

**Description**

If `true`, long paths should be split when printing.

**Type**

Boolean, read-only.

---

### Document.spots

`app.activeDocument.spots`

**Description**

The spot colors contained in this document.

**Type**

[Spots](./Spots.md), read-only.

---

### Document.stationery

`app.activeDocument.stationery`

**Description**

If `true`, the file is a stationery file.

**Type**

Boolean, read-only.

---

### Document.stories

`app.activeDocument.stories`

**Description**

The story items in this document.

**Type**

[Stories](./Stories.md), read-only.

---

### Document.swatches

`app.activeDocument.swatches`

**Description**

The swatches in this document.

**Type**

[Swatches](./Swatches.md), read-only.

---

### Document.swatchGroups

`app.activeDocument.swatchGroups`

**Description**

The swatch groups in this document.

**Type**

[SwatchGroups](./SwatchGroups.md), read-only.

---

### Document.symbolItems

`app.activeDocument.symbolItems`

**Description**

The art items in the document linked to symbols.

**Type**

[SymbolItems](./SymbolItems.md), read-only.

---

### Document.symbols

`app.activeDocument.symbols`

**Description**

The symbols in this document.

**Type**

[Symbols](./Symbols.md), read-only.

---

### Document.tags

`app.activeDocument.tags`

**Description**

The tags in this document.

**Type**

[Tags](./Tags.md), read-only.

---

### Document.textFrames

`app.activeDocument.textFrames`

**Description**

The text frames in this document.

**Type**

[TextFrameItems](./TextFrameItems.md), read-only.

---

### Document.tileFullPages

`app.activeDocument.tileFullPages`

**Description**

If `true`, full pages should be tiled when printing this document.

**Type**

Boolean, read-only.

---

### Document.typename

`app.activeDocument.typename`

**Description**

The class name of the referenced object.

**Type**

String, read-only.

---

### Document.useDefaultScreen

`app.activeDocument.useDefaultScreen`

**Description**

If `true`, the printer's default screen should be used when printing this document.

**Type**

Boolean, read-only.

---

### Document.variables

`app.activeDocument.variables`

**Description**

The variables defined in this document.

**Type**

[Variables](./Variables.md), read-only.

---

### Document.variablesLocked

`app.activeDocument.variablesLocked`

**Description**

If true, the variables are locked.

**Type**

Boolean.

---

### Document.views

`app.activeDocument.views`

**Description**

The views contained in this document.

**Type**

[Views](./Views.md), read-only.

---

### Document.visibleBounds

`app.activeDocument.visibleBounds`

**Description**

The visible bounds of the document, including stroke width of any objects in the illustration.

**Type**

Array of 4 numbers, read-only.

---

### Document.width

`app.activeDocument.width`

**Description**

The width of this document.

**Type**

Number (double), read-only.

---

### Document.XMPString

`app.activeDocument.XMPString`

**Description**

The XMP metadata packet associated with this document.

**Type**

String.

---

## Methods

### Document.activate()

`app.activeDocument.activate()`

**Description**

Brings the first window associated with the document to the front.

**Returns**

Nothing.

---

### Document.arrange()

`app.activeDocument.arrange([layoutStyle])`

**Description**

Arranges multiple documents in the given layout style.

**Parameters**

| Parameter     | Type                                                                                                     | Description                              |
|---------------|----------------------------------------------------------------------------------------------------------|------------------------------------------|
| `layoutStyle` | [DocumentLayoutStyle](scripting-constants.md#jsobjref-scripting-constants-documentlayoutstyle), optional | The layout style to arrange documents in |

**Returns**

Boolean.

---

### Document.close()

`app.activeDocument.close([saveOptions])`

**Description**

Closes a document using specified save options.

When you close a document, you should set your document reference to `null` to prevent your script from accidentally trying to access closed documents.

**Parameters**

| Parameter     | Type                                                                           | Description                |
|---------------|--------------------------------------------------------------------------------|----------------------------|
| `saveOptions` | [SaveOptions](scripting-constants.md#jsobjref-scripting-constants-saveoptions) | Save options to close with |

**Returns**

Nothing.

---

### Document.closeNoUI()

`app.activeDocument.closeNoUI()`

**Description**

Closes the specified non-UI document.

**Returns**

Nothing.

---

### Document.convertCoordinate()

`app.activeDocument.convertCoordinate(coordinate, source, destination)`

**Description**

Converts the given point between artboard and document coordinate systems. Returns the converted point coordinates.

**Parameters**

| Parameter     | Type                                                                                     | Description                   |
|---------------|------------------------------------------------------------------------------------------|-------------------------------|
| `coordinate`  | Point                                                                                    | Point to convert              |
| `source`      | [CoordinateSystem](scripting-constants.md#jsobjref-scripting-constants-coordinatesystem) | Source coordinate system      |
| `destination` | [CoordinateSystem](scripting-constants.md#jsobjref-scripting-constants-coordinatesystem) | Destination coordinate system |

**Returns**

Point.

---

### Document.exportFile()

`app.activeDocument.exportFile(exportFile, exportFormat [,options])`

**Description**

Exports the document to the specified file using one of the predefined export file formats. The appropriate file extension is automatically appended to the file name, except for Photoshop® documents. For these, you must include the file extension (PSD) in the file specification.

**Parameters**

| Parameter      | Type                                                                         | Description        |
|----------------|------------------------------------------------------------------------------|--------------------|
| `exportFile`   | File                                                                         | File to save       |
| `exportFormat` | [ExportType](scripting-constants.md#jsobjref-scripting-constants-exporttype) | Export file format |
| `options`      | [Variable](./Variable.md), optional                          | todo               |

**Returns**

Nothing.

---

### Document.exportPDFPreset()

`app.activeDocument.exportPDFPreset(file)`

**Description**

Exports the current PDF preset values to the file.

**Parameters**

| Parameter   | Type   | Description              |
|-------------|--------|--------------------------|
| `file`      | File   | Preset file to export to |

**Returns**

Nothing.

---

### Document.exportPerspectiveGridPreset()

`app.activeDocument.exportPerspectiveGridPreset(file)`

**Description**

Exports the current perspective grid preset values to the file.

**Parameters**

| Parameter   | Type   | Description              |
|-------------|--------|--------------------------|
| `file`      | File   | Preset file to export to |

**Returns**

Nothing.

---

### Document.exportPrintPreset()

`app.activeDocument.exportPrintPreset(file)`

**Description**

Exports the current print preset values to the file.

**Parameters**

| Parameter   | Type   | Description              |
|-------------|--------|--------------------------|
| `file`      | File   | Preset file to export to |

**Returns**

Nothing.

---

### Document.exportVariables()

`app.activeDocument.exportVariables(fileSpec)`

**Description**

Saves datasets into an XML library. The datasets contain variables and their associated dynamic data.

**Parameters**

| Parameter   | Type   | Description                   |
|-------------|--------|-------------------------------|
| `fileSpec`  | File   | XML Library file to export to |

**Returns**

Nothing.

---

### Document.fitArtboardToSelectedArt()

`app.activeDocument.fitArtboardToSelectedArt([index])`

**Description**

Resizes the artboard at the given index to fit currently selected art. Index default is 0. Returns `true` on success.

**Parameters**

| Parameter   | Type                    | Description              |
|-------------|-------------------------|--------------------------|
| `index`     | Number (long), optional | Artboard index to resize |

**Returns**

Boolean.

---

### Document.getPageItemFromUuid()

`app.activeDocument.getPageItemFromUuid(uuid)`

!!! note
    This functionality was added in Illustrator 24.0. (CC2020)

**Description**

Retrieves the pageitem using Uuid.

**Parameters**

| Parameter   | Type   | Description      |
|-------------|--------|------------------|
| `uuid`      | String | uuid of PageItem |

**Returns**

[PageItem](./PageItem.md).

---

### Document.getPerspectiveActivePlane()

`app.activeDocument.getPerspectiveActivePlane()`

**Description**

Retrieves the active plane of the active perspective grid of the document.

**Returns**

[PerspectiveGridPlaneType](scripting-constants.md#jsobjref-scripting-constants-perspectivegridplanetype)

---

### Document.hidePerspectiveGrid()

`app.activeDocument.hidePerspectiveGrid()`

**Description**

Hides the current active grid for the document. If no grid is visible, does nothing. Returns `true` if a grid is hidden.

**Returns**

Boolean.

---

### Document.imageCapture()

`app.activeDocument.imageCapture(imageFile [,clipBounds] [,options])`

**Description**

Captures the artwork content within the clipping boundaries in this document as a raster image, and writes the image data to a specified file.

If the bounds parameter is omitted, captures the entire artwork.

**Parameters**

| Parameter    | Type                                                                                 | Description            |
|--------------|--------------------------------------------------------------------------------------|------------------------|
| `imageFile`  | File                                                                                 | Image file to write to |
| `clipBounds` | Rect, optional                                                                       | Clipping bounds        |
| `options`    | [ImageCaptureOptions](./ImageCaptureOptions.md), optional | todo                   |

**Returns**

Nothing.

---

### Document.importCharacterStyles()

`app.activeDocument.importCharacterStyles(fileSpec)`

**Description**

Loads the character styles from the Illustrator file.

**Parameters**

| Parameter   | Type   | Description                        |
|-------------|--------|------------------------------------|
| `fileSpec`  | File   | File to load character styles from |

**Returns**

Nothing.

---

### Document.importParagraphStyles()

`app.activeDocument.importParagraphStyles(fileSpec)`

**Description**

Loads the paragraph styles from the Illustrator file.

**Parameters**

| Parameter   | Type   | Description                        |
|-------------|--------|------------------------------------|
| `fileSpec`  | File   | File to load paragraph styles from |

**Returns**

Nothing.

---

### Document.importPDFPreset()

`app.activeDocument.importPDFPreset(fileSpec [, replacingPreset])`

**Description**

Loads all PDF presets from a file.

**Parameters**

| Parameter         | Type             | Description                         |
|-------------------|------------------|-------------------------------------|
| `fileSpec`        | File             | File to load PDF presets from       |
| `replacingPreset` | String, optional | Whether to replace existing presets |

**Returns**

Nothing.

---

### Document.importPrintPreset()

`app.activeDocument.importPrintPreset(printPreset, fileSpec)`

**Description**

Loads the named print preset from the file.

**Parameters**

| Parameter     | Type   | Description                     |
|---------------|--------|---------------------------------|
| `printPreset` | String | Name of preset to load          |
| `fileSpec`    | File   | File to load print presets from |

**Returns**

Nothing.

---

### Document.importVariables()

`app.activeDocument.importVariables(fileSpec)`

**Description**

Imports a library containing datasets, variables, and their associated dynamic data. Importing variables overwrites existing variables and datasets.

**Parameters**

| Parameter   | Type   | Description                   |
|-------------|--------|-------------------------------|
| `fileSpec`  | File   | File to import variables from |

**Returns**

Nothing.

---

### Document.print()

`app.activeDocument.print([options])`

**Description**

Prints the document.

**Parameters**

| Parameter   | Type                                                            | Description   |
|-------------|-----------------------------------------------------------------|---------------|
| `options`   | [PrintOptions](./PrintOptions.md), optional | todo          |

**Returns**

Nothing.

---

### Document.rasterize()

`app.activeDocument.rasterize(sourceArt [, clipBounds] [, options])`

**Description**

Rasterizes the source art(s) within the specified clip bounds. The source art(s) is disposed of as a result of the rasterization.

**Parameters**

| Parameter    | Type                                                                        | Description             |
|--------------|-----------------------------------------------------------------------------|-------------------------|
| `sourceArt`  | [Variable](./Variable.md)                                   | Source art to rasterize |
| `clipBounds` | Rect, optional                                                              | Clipping bounds         |
| `options`    | [RasterizeOptions](./RasterizeOptions.md), optional | todo                    |

**Returns**

[RasterItem](./RasterItem.md)

---

### Document.rearrangeArboards()

`app.activeDocument.rearrangeArboards([artboardLayout] [, artboardRowsOrCols] [, artboardSpacing] [, artboardMoveArtwork])`

**Description**

Rearranges artboards in the document. All arguments are optional.

Default layout style is `DocumentArtboard Layout.GridByRow`.

The second argument specifies the number of rows or columns, as appropriate for the chosen layout style, in the range `1..docNumArtboards-1`, or 1 (the default) for single row/column layouts.

Spacing is a number of pixels, default 20.

When last argument is true (the default), artwork is moved with the artboards.

**Parameters**

| Parameter             | Type                                                                                                           | Description                                |
|-----------------------|----------------------------------------------------------------------------------------------------------------|--------------------------------------------|
| `artboardLayout`      | [DocumentArtboardLayout](scripting-constants.md#jsobjref-scripting-constants-documentartboardlayout), optional | Artboard layout                            |
| `artboardRowsOrCols`  | Integer, optional                                                                                              | Number of rows or columns                  |
| `artboardSpacing`     | Number, optional                                                                                               | Number of pixels for spacing               |
| `artboardMoveArtwork` | Boolean, optional                                                                                              | Whether to move artwork with the artboards |

**Returns**

Boolean.

---

### Document.save()

`app.activeDocument.save()`

**Description**

Saves the document in it current location.

**Returns**

Nothing.

---

### Document.saveAs()

`app.activeDocument.saveAs(saveIn [, options])`

**Description**

Saves the document in the specified file as an Illustrator, EPS, or PDF file.

**Parameters**

| Parameter   | Type                                                                                     | Description                  |
|-------------|------------------------------------------------------------------------------------------|------------------------------|
| `saveIn`    | File                                                                                     | File to save the document as |
| `options`   | [SaveOptions](scripting-constants.md#jsobjref-scripting-constants-saveoptions), optional | Save options to close with   |

**Returns**

Nothing.

---

### Document.saveNoUI()

`app.activeDocument.saveNoUI(saveIn)`

**Description**

Saves the non-UI document at the specified path

**Parameters**

| Parameter   | Type   | Description                  |
|-------------|--------|------------------------------|
| `saveIn`    | File   | File to save the document as |

**Returns**

Nothing.

---

### Document.selectObjectsOnActiveArtboard()

`app.activeDocument.selectObjectsOnActiveArtboard()`

**Description**

Selects the objects on the currently active artboard. Returns `true` on success.

**Returns**

Boolean.

---

### Document.setActivePlane()

`app.activeDocument.setActivePlane(gridPlane)`

**Description**

Sets the active plane of the active perspective grid of the document. Returns `true` on success.

**Parameters**

| Parameter   | Type                                                                                                     | Description     |
|-------------|----------------------------------------------------------------------------------------------------------|-----------------|
| `gridPlane` | [PerspectiveGridPlaneType](scripting-constants.md#jsobjref-scripting-constants-perspectivegridplanetype) | Grid plane type |

**Returns**

Boolean.

---

### Document.selectPerspectivePreset()

`app.activeDocument.selectPerspectivePreset(gridType, presetName)`

**Description**

Selects a predefined preset to define grid for the current document. Returns `true` on success.

**Parameters**

| Parameter    | Type                                                                                           | Description           |
|--------------|------------------------------------------------------------------------------------------------|-----------------------|
| `gridType`   | [PerspectiveGridType](scripting-constants.md#jsobjref-scripting-constants-perspectivegridtype) | Grid type             |
| `presetName` | String                                                                                         | Preset name to select |

**Returns**

Boolean.

---

### Document.showPerspectiveGrid()

`app.activeDocument.showPerspectiveGrid()`

**Description**

Shows the current active grid for the document, or if no grid is active, shows the default grid. Returns `true` on success.

**Returns**

Boolean.

---

### Document.windowCapture()

`app.activeDocument.windowCapture(imageFile, windowSize)`

**Description**

Captures the current document window to the target TIFF image file.

**Parameters**

| Parameter    | Type               | Description           |
|--------------|--------------------|-----------------------|
| `imageFile`  | File               | Image file to save as |
| `windowSize` | Array of 2 numbers | Window size           |

**Returns**

Nothing.

---

## Example

### Deselecting all objects in the current document

!!! note
    The frontmost document can be referred to as either `activeDocument` or `documents[0`.

```default
var docRef = activeDocument;
docRef.selection = null;
```

---

### Closing a document

```default
// Closes the active document without saving changes
if ( app.documents.length > 0 ) {
    var aiDocument = app.activeDocument;
    aiDocument.close( SaveOptions.DONOTSAVECHANGES );
    aiDocument = null;
}
```

---

### Creating a document with defaults

```default
// Creates a new document if none exists then sets fill and stroke defaults to true
var doc;
if (app.documents.length == 0) {
    doc = app.documents.add();
} else {
    doc = app.activeDocument;
}

doc.defaultFilled = true;
doc.defaultStroked = true;
```

<a id="jsobjref-document"></a>

# Document

`app.activeDocument`

**Description**

An Illustrator document. Documents are contained in the [Application](Application.md#jsobjref-application) object.

The default document settings—those properties starting with the word “default”—are global settings that affect the current document. Be sure to modify these default properties only when a document is open. Note that if you set default properties to desired values before creating new objects, you can streamline your scripts, eliminating the need to specify specific properties such as `fillColor` and `stroked` that have default properties.

A document’s color space, height, and width can only be set when the document is created. You cannot modify these properties in an existing document. See [Application.open()](Application.md#jsobjref-application-open) for more information on how document color spaces are handled.

---

## Properties

<a id="jsobjref-document-activedataset"></a>

### Document.activeDataset

`app.activeDocument.activeDataset`

**Description**

The currently opened dataset.

**Type**

[Dataset](Dataset.md#jsobjref-dataset)

---

<a id="jsobjref-document-activelayer"></a>

### Document.activeLayer

`app.activeDocument.activeLayer`

**Description**

The active layer in the document.

**Type**

[Layer](Layer.md#jsobjref-layer)

---

<a id="jsobjref-document-activeview"></a>

### Document.activeView

`app.activeDocument.activeView`

**Description**

The document’s current view.

**Type**

[View](View.md#jsobjref-view), read-only.

---

<a id="jsobjref-document-artboards"></a>

### Document.artboards

`app.activeDocument.artboards`

**Description**

All artboards in the document.

**Type**

[Artboards](Artboards.md#jsobjref-artboards), read-only.

---

<a id="jsobjref-document-brushes"></a>

### Document.brushes

`app.activeDocument.brushes`

**Description**

The brushes contained in the document.

**Type**

[Brushes](Brushes.md#jsobjref-brushes), read-only.

---

<a id="jsobjref-document-characterstyles"></a>

### Document.characterStyles

`app.activeDocument.characterStyles`

**Description**

The list of character styles in this document.

**Type**

[CharacterStyles](CharacterStyles.md#jsobjref-characterstyles), read-only.

---

<a id="jsobjref-document-compoundpathitems"></a>

### Document.compoundPathItems

`app.activeDocument.compoundPathItems`

**Description**

The compound path items contained in the document.

**Type**

[CompoundPathItems](CompoundPathItems.md#jsobjref-compoundpathitems), read-only.

---

<a id="jsobjref-document-cropbox"></a>

### Document.cropBox

`app.activeDocument.cropBox`

**Description**

The boundary of the document’s cropping box for output, or `null` if no value has been set.

**Type**

Array of 4 numbers.

---

<a id="jsobjref-document-cropstyle"></a>

### Document.cropStyle

`app.activeDocument.cropStyle`

**Description**

The style of the document’s cropping box.

**Type**

[CropOptions](scripting-constants.md#jsobjref-scripting-constants-cropoptions)

---

<a id="jsobjref-document-datasets"></a>

### Document.dataSets

`app.activeDocument.dataSets`

**Description**

The datasets contained in the document.

**Type**

[Datasets](Datasets.md#jsobjref-datasets), read-only.

---

<a id="jsobjref-document-defaultfillcolor"></a>

### Document.defaultFillColor

`app.activeDocument.defaultFillColor`

**Description**

The color to use to fill new paths if `defaultFilled` is `true`.

**Type**

[Color](Color.md#jsobjref-color)

---

<a id="jsobjref-document-defaultfilled"></a>

### Document.defaultFilled

`app.activeDocument.defaultFilled`

**Description**

If `true`, a new path should be filled.

**Type**

Boolean.

---

<a id="jsobjref-document-defaultfilloverprint"></a>

### Document.defaultFillOverprint

`app.activeDocument.defaultFillOverprint`

**Description**

If `true`, the art beneath a filled object should be overprinted by default.

**Type**

Boolean.

---

<a id="jsobjref-document-defaultstrokecap"></a>

### Document.defaultStrokeCap

`app.activeDocument.defaultStrokeCap`

**Description**

Default type of line capping for paths created.

**Type**

[StrokeCap](scripting-constants.md#jsobjref-scripting-constants-strokecap)

---

<a id="jsobjref-document-defaultstrokecolor"></a>

### Document.defaultStrokeColor

`app.activeDocument.defaultStrokeColor`

**Description**

The stroke color for new paths if default stroked is `true`.

**Type**

[Color](Color.md#jsobjref-color)

---

<a id="jsobjref-document-defaultstroked"></a>

### Document.defaultStroked

`app.activeDocument.defaultStroked`

**Description**

If `true`, a new path should be stroked.

**Type**

Boolean.

---

<a id="jsobjref-document-defaultstrokedashes"></a>

### Document.defaultStrokeDashes

`app.activeDocument.defaultStrokeDashes`

**Description**

Default lengths for dashes and gaps in dashed lines, starting with the first dash length, followed by the first gap length, and so on. Set to an empty object, {}, for solid line.

**Type**

Object.

---

<a id="jsobjref-document-defaultstrokedashoffset"></a>

### Document.defaultStrokeDashOffset

`app.activeDocument.defaultStrokeDashOffset`

**Description**

The default distance into the dash pattern at which the pattern should be started for new paths.

**Type**

Number (double).

---

<a id="jsobjref-document-defaultstrokejoin"></a>

### Document.defaultStrokeJoin

`app.activeDocument.defaultStrokeJoin`

**Description**

Default type of joints in new paths.

**Type**

[StrokeJoin](scripting-constants.md#jsobjref-scripting-constants-strokejoin)

---

<a id="jsobjref-document-defaultstrokemiterlimit"></a>

### Document.defaultStrokeMiterLimit

`app.activeDocument.defaultStrokeMiterLimit`

**Description**

When a default stroke join is set to `mitered`, this property specifies when the join will be converted to beveled (squared-off ) by default. The default miter limit of 4 means that when the length of the point reaches four times the stroke weight, the join switches from a miter join to a bevel join. Range: 1 to 500; a value of 1 specifies a bevel join.

**Type**

Number (double).

---

<a id="jsobjref-document-defaultstrokeoverprint"></a>

### Document.defaultStrokeOverprint

`app.activeDocument.defaultStrokeOverprint`

**Description**

If `true`, the art beneath a stroked object should be overprinted by default.

**Type**

Boolean.

---

<a id="jsobjref-document-defaultstrokewidth"></a>

### Document.defaultStrokeWidth

`app.activeDocument.defaultStrokeWidth`

**Description**

Default width of stroke for new paths.

**Type**

Number (double).

---

<a id="jsobjref-document-documentcolorspace"></a>

### Document.documentColorSpace

`app.activeDocument.documentColorSpace`

**Description**

The color specification system to use for this document’s color space.

**Type**

[DocumentColorSpace](scripting-constants.md#jsobjref-scripting-constants-documentcolorspace)

---

<a id="jsobjref-document-fullname"></a>

### Document.fullName

`app.activeDocument.fullName`

**Description**

The file associated with the document, which includes the complete path to the file.

**Type**

File, read-only.

---

<a id="jsobjref-document-geometricbounds"></a>

### Document.geometricBounds

`app.activeDocument.geometricBounds`

**Description**

The bounds of the illustration excluding the stroke width of any objects in the document.

**Type**

Array of 4 numbers, read-only.

---

<a id="jsobjref-document-gradients"></a>

### Document.gradients

`app.activeDocument.gradients`

**Description**

The gradients contained in the document.

**Type**

[Gradients](Gradients.md#jsobjref-gradients), read-only.

---

<a id="jsobjref-document-graphicstyles"></a>

### Document.graphicStyles

`app.activeDocument.graphicStyles`

**Description**

The graphic styles defined in this document.

**Type**

[GraphicStyles](GraphicStyles.md#jsobjref-graphicstyles), read-only.

---

<a id="jsobjref-document-graphitems"></a>

### Document.graphItems

`app.activeDocument.graphItems`

**Description**

The graph art items in this document.

**Type**

[GraphItems](GraphItems.md#jsobjref-graphitems), read-only.

---

<a id="jsobjref-document-groupitems"></a>

### Document.groupItems

`app.activeDocument.groupItems`

**Description**

The group items contained in the document.

**Type**

[GroupItems](GroupItems.md#jsobjref-groupitems), read-only.

---

<a id="jsobjref-document-height"></a>

### Document.height

`app.activeDocument.height`

**Description**

The height of the document.

**Type**

Number (double), read-only.

---

<a id="jsobjref-document-inklist"></a>

### Document.inkList

`app.activeDocument.inkList`

**Description**

The list of inks in this document.

**Type**

Object, read-only.

---

<a id="jsobjref-document-kinsokuset"></a>

### Document.kinsokuSet

`app.activeDocument.kinsokuSet`

**Description**

The Kinsoku set of characters that cannot begin or end a line of Japanese text.

**Type**

Object, read-only.

---

<a id="jsobjref-document-layers"></a>

### Document.layers

`app.activeDocument.layers`

**Description**

The layers contained in the document.

**Type**

[Layers](Layers.md#jsobjref-layers), read-only.

---

<a id="jsobjref-document-legacytextitems"></a>

### Document.legacyTextItems

`app.activeDocument.legacyTextItems`

**Description**

The legacy text items in the document.

**Type**

[LegacyTextItems](LegacyTextItems.md#jsobjref-legacytextitems), read-only.

---

<a id="jsobjref-document-meshitems"></a>

### Document.meshItems

`app.activeDocument.meshItems`

**Description**

The mesh art items contained in the document.

**Type**

[MeshItems](MeshItems.md#jsobjref-meshitems), read-only.

---

<a id="jsobjref-document-mojikumiset"></a>

### Document.mojikumiSet

`app.activeDocument.mojikumiSet`

**Description**

A list of names of predefined Mojikumi sets which specify the spacing for the layout and composition of Japanese text.

**Type**

Object, read-only.

---

<a id="jsobjref-document-name"></a>

### Document.name

`app.activeDocument.name`

**Description**

The document’s name (not the complete file path to the document).

**Type**

String, read-only.

---

<a id="jsobjref-document-nonnativeitems"></a>

### Document.nonNativeItems

`app.activeDocument.nonNativeItems`

**Description**

The non-native art items in this document.

**Type**

[NonNativeItems](NonNativeItems.md#jsobjref-nonnativeitems), read-only.

---

<a id="jsobjref-document-outputresolution"></a>

### Document.outputResolution

`app.activeDocument.outputResolution`

**Description**

The current output resolution for the document in dots per inch (dpi).

**Type**

Number (double), read-only.

---

<a id="jsobjref-document-pageitems"></a>

### Document.pageItems

`app.activeDocument.pageItems`

**Description**

The page items (all art item classes) contained in the document.

**Type**

[PageItems](PageItems.md#jsobjref-pageitems), read-only.

---

<a id="jsobjref-document-pageorigin"></a>

### Document.pageOrigin

`app.activeDocument.pageOrigin`

**Description**

The zero-point of the page in the document without margins, relative to the overall height and width.

**Type**

Array of 2 numbers.

---

<a id="jsobjref-document-paragraphstyles"></a>

### Document.paragraphStyles

`app.activeDocument.paragraphStyles`

**Description**

The list of paragraph styles in this document.

**Type**

[ParagraphStyles](ParagraphStyles.md#jsobjref-paragraphstyles), read-only.

---

<a id="jsobjref-document-parent"></a>

### Document.parent

`app.activeDocument.parent`

**Description**

The application that contains this document.

**Type**

[Application](Application.md#jsobjref-application), read-only.

---

<a id="jsobjref-document-path"></a>

### Document.path

`app.activeDocument.path`

**Description**

The file associated with the document, which includes the complete path to the file.

**Type**

File, read-only.

---

<a id="jsobjref-document-pathitems"></a>

### Document.pathItems

`app.activeDocument.pathItems`

**Description**

The path items contained in this document.

**Type**

[PathItems](PathItems.md#jsobjref-pathitems), read-only.

---

<a id="jsobjref-document-patterns"></a>

### Document.patterns

`app.activeDocument.patterns`

**Description**

The patterns contained in this document.

**Type**

[Patterns](Patterns.md#jsobjref-patterns), read-only.

---

<a id="jsobjref-document-placeditems"></a>

### Document.placedItems

`app.activeDocument.placedItems`

**Description**

The placed items contained in this document.

**Type**

[PlacedItems](PlacedItems.md#jsobjref-placeditems), read-only.

---

<a id="jsobjref-document-pluginitems"></a>

### Document.pluginItems

`app.activeDocument.pluginItems`

**Description**

The plug-in items contained in this document.

**Type**

[PluginItems](PluginItems.md#jsobjref-pluginitems), read-only.

---

<a id="jsobjref-document-printtiles"></a>

### Document.printTiles

`app.activeDocument.printTiles`

**Description**

If `true`, this document should be printed as tiled output.

**Type**

Boolean, read-only.

---

<a id="jsobjref-document-rastereffectsettings"></a>

### Document.rasterEffectSettings

`app.activeDocument.rasterEffectSettings`

**Description**

The document’s raster effect settings.

**Type**

[RasterEffectOptions](RasterEffectOptions.md#jsobjref-rastereffectoptions), read-only.

---

<a id="jsobjref-document-rasteritems"></a>

### Document.rasterItems

`app.activeDocument.rasterItems`

**Description**

The raster items contained in this document.

**Type**

[RasterItems](RasterItems.md#jsobjref-rasteritems), read-only.

---

<a id="jsobjref-document-rulerorigin"></a>

### Document.rulerOrigin

`app.activeDocument.rulerOrigin`

**Description**

The zero-point of the rulers in the document relative to the bottom left of the document.

**Type**

Array of 2 numbers.

---

<a id="jsobjref-document-rulerunits"></a>

### Document.rulerUnits

`app.activeDocument.rulerUnits`

**Description**

The default measurement units for the rulers in the document.

**Type**

[RulerUnits](scripting-constants.md#jsobjref-scripting-constants-rulerunits), read-only.

---

<a id="jsobjref-document-saved"></a>

### Document.saved

`app.activeDocument.saved`

**Description**

If `true`, the document has not been changed since last time it was saved.

**Type**

Boolean.

---

<a id="jsobjref-document-selection"></a>

### Document.selection

`app.activeDocument.selection`

**Description**

References to the objects in this document’s current selection, or `null` when nothing is selected.

A reference to an insertion point is returned when there is an active insertion point in the contents of a selected text art item. Similarly, a reference to a range of text is returned when characters are selected in the contents of a text art item.

**Type**

Array of objects.

---

<a id="jsobjref-document-showplacedimages"></a>

### Document.showPlacedImages

`app.activeDocument.showPlacedImages`

**Description**

If `true`, placed images should be displayed in the document.

**Type**

Boolean, read-only.

---

<a id="jsobjref-document-splitlongpaths"></a>

### Document.splitLongPaths

`app.activeDocument.splitLongPaths`

**Description**

If `true`, long paths should be split when printing.

**Type**

Boolean, read-only.

---

<a id="jsobjref-document-spots"></a>

### Document.spots

`app.activeDocument.spots`

**Description**

The spot colors contained in this document.

**Type**

[Spots](Spots.md#jsobjref-spots), read-only.

---

<a id="jsobjref-document-stationery"></a>

### Document.stationery

`app.activeDocument.stationery`

**Description**

If `true`, the file is a stationery file.

**Type**

Boolean, read-only.

---

<a id="jsobjref-document-stories"></a>

### Document.stories

`app.activeDocument.stories`

**Description**

The story items in this document.

**Type**

[Stories](Stories.md#jsobjref-stories), read-only.

---

<a id="jsobjref-document-swatches"></a>

### Document.swatches

`app.activeDocument.swatches`

**Description**

The swatches in this document.

**Type**

[Swatches](Swatches.md#jsobjref-swatches), read-only.

---

<a id="jsobjref-document-swatchgroups"></a>

### Document.swatchGroups

`app.activeDocument.swatchGroups`

**Description**

The swatch groups in this document.

**Type**

[SwatchGroups](SwatchGroups.md#jsobjref-swatchgroups), read-only.

---

<a id="jsobjref-document-symbolitems"></a>

### Document.symbolItems

`app.activeDocument.symbolItems`

**Description**

The art items in the document linked to symbols.

**Type**

[SymbolItems](SymbolItems.md#jsobjref-symbolitems), read-only.

---

<a id="jsobjref-document-symbols"></a>

### Document.symbols

`app.activeDocument.symbols`

**Description**

The symbols in this document.

**Type**

[Symbols](Symbols.md#jsobjref-symbols), read-only.

---

<a id="jsobjref-document-tags"></a>

### Document.tags

`app.activeDocument.tags`

**Description**

The tags in this document.

**Type**

[Tags](Tags.md#jsobjref-tags), read-only.

---

<a id="jsobjref-document-textframes"></a>

### Document.textFrames

`app.activeDocument.textFrames`

**Description**

The text frames in this document.

**Type**

[TextFrameItems](TextFrameItems.md#jsobjref-textframeitems), read-only.

---

<a id="jsobjref-document-tilefullpages"></a>

### Document.tileFullPages

`app.activeDocument.tileFullPages`

**Description**

If `true`, full pages should be tiled when printing this document.

**Type**

Boolean, read-only.

---

<a id="jsobjref-document-typename"></a>

### Document.typename

`app.activeDocument.typename`

**Description**

The class name of the referenced object.

**Type**

String, read-only.

---

<a id="jsobjref-document-usedefaultscreen"></a>

### Document.useDefaultScreen

`app.activeDocument.useDefaultScreen`

**Description**

If `true`, the printer’s default screen should be used when printing this document.

**Type**

Boolean, read-only.

---

<a id="jsobjref-document-variables"></a>

### Document.variables

`app.activeDocument.variables`

**Description**

The variables defined in this document.

**Type**

[Variables](Variables.md#jsobjref-variables), read-only.

---

<a id="jsobjref-document-variableslocked"></a>

### Document.variablesLocked

`app.activeDocument.variablesLocked`

**Description**

If true, the variables are locked.

**Type**

Boolean.

---

<a id="jsobjref-document-views"></a>

### Document.views

`app.activeDocument.views`

**Description**

The views contained in this document.

**Type**

[Views](Views.md#jsobjref-views), read-only.

---

<a id="jsobjref-document-visiblebounds"></a>

### Document.visibleBounds

`app.activeDocument.visibleBounds`

**Description**

The visible bounds of the document, including stroke width of any objects in the illustration.

**Type**

Array of 4 numbers, read-only.

---

<a id="jsobjref-document-width"></a>

### Document.width

`app.activeDocument.width`

**Description**

The width of this document.

**Type**

Number (double), read-only.

---

<a id="jsobjref-document-xmpstring"></a>

### Document.XMPString

`app.activeDocument.XMPString`

**Description**

The XMP metadata packet associated with this document.

**Type**

String.

---

## Methods

<a id="jsobjref-document-activate"></a>

### Document.activate()

`app.activeDocument.activate()`

**Description**

Brings the first window associated with the document to the front.

**Returns**

Nothing.

---

<a id="jsobjref-document-arrange"></a>

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

<a id="jsobjref-document-close"></a>

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

<a id="jsobjref-document-closenoui"></a>

### Document.closeNoUI()

`app.activeDocument.closeNoUI()`

**Description**

Closes the specified non-UI document.

**Returns**

Nothing.

---

<a id="jsobjref-document-convertcoordinate"></a>

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

<a id="jsobjref-document-exportfile"></a>

### Document.exportFile()

`app.activeDocument.exportFile(exportFile, exportFormat [,options])`

**Description**

Exports the document to the specified file using one of the predefined export file formats. The appropriate file extension is automatically appended to the file name, except for Photoshop® documents. For these, you must include the file extension (PSD) in the file specification.

**Parameters**

| Parameter      | Type                                                                         | Description        |
|----------------|------------------------------------------------------------------------------|--------------------|
| `exportFile`   | File                                                                         | File to save       |
| `exportFormat` | [ExportType](scripting-constants.md#jsobjref-scripting-constants-exporttype) | Export file format |
| `options`      | [Variable](Variable.md#jsobjref-variable), optional                          | todo               |

**Returns**

Nothing.

---

<a id="jsobjref-document-exportpdfpreset"></a>

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

<a id="jsobjref-document-exportperspectivegridpreset"></a>

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

<a id="jsobjref-document-exportprintpreset"></a>

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

<a id="jsobjref-document-exportvariables"></a>

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

<a id="jsobjref-document-fitartboardtoselectedart"></a>

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

<a id="jsobjref-document-getpageitemfromuuid"></a>

### Document.getPageItemFromUuid()

`app.activeDocument.getPageItemFromUuid(uuid)`

#### NOTE
This functionality was added in Illustrator 24.0. (CC2020)

**Description**

Retrieves the pageitem using Uuid.

**Parameters**

| Parameter   | Type   | Description      |
|-------------|--------|------------------|
| `uuid`      | String | uuid of PageItem |

**Returns**

[PageItem](PageItem.md#jsobjref-pageitem).

---

<a id="jsobjref-document-getperspectiveactiveplane"></a>

### Document.getPerspectiveActivePlane()

`app.activeDocument.getPerspectiveActivePlane()`

**Description**

Retrieves the active plane of the active perspective grid of the document.

**Returns**

[PerspectiveGridPlaneType](scripting-constants.md#jsobjref-scripting-constants-perspectivegridplanetype)

---

<a id="jsobjref-document-hideperspectivegrid"></a>

### Document.hidePerspectiveGrid()

`app.activeDocument.hidePerspectiveGrid()`

**Description**

Hides the current active grid for the document. If no grid is visible, does nothing. Returns `true` if a grid is hidden.

**Returns**

Boolean.

---

<a id="jsobjref-document-imagecapture"></a>

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
| `options`    | [ImageCaptureOptions](ImageCaptureOptions.md#jsobjref-imagecaptureoptions), optional | todo                   |

**Returns**

Nothing.

---

<a id="jsobjref-document-importcharacterstyles"></a>

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

<a id="jsobjref-document-importparagraphstyles"></a>

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

<a id="jsobjref-document-importpdfpreset"></a>

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

<a id="jsobjref-document-importprintpreset"></a>

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

<a id="jsobjref-document-importvariables"></a>

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

<a id="jsobjref-document-print"></a>

### Document.print()

`app.activeDocument.print([options])`

**Description**

Prints the document.

**Parameters**

| Parameter   | Type                                                            | Description   |
|-------------|-----------------------------------------------------------------|---------------|
| `options`   | [PrintOptions](PrintOptions.md#jsobjref-printoptions), optional | todo          |

**Returns**

Nothing.

---

<a id="jsobjref-document-rasterize"></a>

### Document.rasterize()

`app.activeDocument.rasterize(sourceArt [, clipBounds] [, options])`

**Description**

Rasterizes the source art(s) within the specified clip bounds. The source art(s) is disposed of as a result of the rasterization.

**Parameters**

| Parameter    | Type                                                                        | Description             |
|--------------|-----------------------------------------------------------------------------|-------------------------|
| `sourceArt`  | [Variable](Variable.md#jsobjref-variable)                                   | Source art to rasterize |
| `clipBounds` | Rect, optional                                                              | Clipping bounds         |
| `options`    | [RasterizeOptions](RasterizeOptions.md#jsobjref-rasterizeoptions), optional | todo                    |

**Returns**

[RasterItem](RasterItem.md#jsobjref-rasteritem)

---

<a id="jsobjref-document-rearrangearboards"></a>

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

<a id="jsobjref-document-save"></a>

### Document.save()

`app.activeDocument.save()`

**Description**

Saves the document in it current location.

**Returns**

Nothing.

---

<a id="jsobjref-document-saveas"></a>

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

<a id="jsobjref-document-savenoui"></a>

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

<a id="jsobjref-document-selectobjectsonactiveartboard"></a>

### Document.selectObjectsOnActiveArtboard()

`app.activeDocument.selectObjectsOnActiveArtboard()`

**Description**

Selects the objects on the currently active artboard. Returns `true` on success.

**Returns**

Boolean.

---

<a id="jsobjref-document-setactiveplane"></a>

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

<a id="jsobjref-document-selectperspectivepreset"></a>

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

<a id="jsobjref-document-showperspectivegrid"></a>

### Document.showPerspectiveGrid()

`app.activeDocument.showPerspectiveGrid()`

**Description**

Shows the current active grid for the document, or if no grid is active, shows the default grid. Returns `true` on success.

**Returns**

Boolean.

---

<a id="jsobjref-document-windowcapture"></a>

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

#### NOTE
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

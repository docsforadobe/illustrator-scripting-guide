# Application

`app`

**Description**

The Adobe® Illustrator® application object, referenced using the pre-defined global app object, which contains all other Illustrator objects.

---

## Properties

### Application.activeDocument

`app.activeDocument`

**Description**

The active (frontmost) document in Illustrator.

**Type**

[Document](./Document.md)

---

### Application.browserAvailable

`app.browserAvailable`

**Description**

If `true`, a web browser is available.

**Type**

Boolean; read-only.

---

### Application.buildNumber

`app.buildNumber`

**Description**

The application's build number.

**Type**

String; read-only.

---

### Application.colorSettingsList

`app.colorSettingsList`

**Description**

The list of color-settings files currently available for use.

**Type**

Object; read-only.

---

### Application.coordinateSystem

`app.coordinateSystem`

**Description**

The coordinate system currently in use, document or artboard.

**Type**

[CoordinateSystem](scripting-constants.md#jsobjref-scripting-constants-coordinatesystem)

---

### Application.defaultColorSettings

`app.defaultColorSettings`

**Description**

The default color-settings file for the current application locale.

**Type**

File; read-only.

---

### Application.documents

`app.documents`

**Description**

The documents in the application.

**Type**

[Documents](./Documents.md)

---

### Application.flattenerPresetList

`app.flattenerPresetList`

**Description**

The list of flattener style names currently available for use.

**Type**

Object; read-only.

---

### Application.freeMemory

`app.freeMemory`

**Description**

The amount of unused memory (in bytes) within the Illustrator partition.

**Type**

Number (long); read-only.

---

### Application.locale

`app.locale`

**Description**

The application's locale.

**Type**

String; read-only.

---

### Application.name

`app.name`

**Description**

The application's name (not related to the filename of the application file).

**Type**

String; read-only.

---

### Application.pasteRememberLayers

`app.pasteRememberLayers`

**Description**

If `true`, the paste operation maintains the layer structure.

**Type**

Boolean; read-only.

---

### Application.path

`app.path`

**Description**

The file path to the application.

**Type**

File; read-only.

---

### Application.PDFPresetsList

`app.PDFPresetsList`

**Description**

The list of preset PDF-options names available for use.

**Type**

Object; read-only.

---

### Application.PPDFileList

`app.PPDFileList`

**Description**

The list of PPD files currently available for use.

**Type**

Object; read-only.

---

### Application.preferences

`app.preferences`

**Description**

Illustrator's preference settings.

**Type**

[Preferences](./Preferences.md)

---

### Application.printerList

`app.printerList`

**Description**

The list of installed printers.

**Type**

Array of [Printer](./Printer.md)

---

### Application.printPresetsList

`app.printPresetsList`

**Description**

The list of preset printing-options names available for use.

**Type**

Object; read-only.

---

### Application.scriptingVersion

`app.scriptingVersion`

**Description**

The version of the Scripting plug-in.

**Type**

String; read-only.

---

### Application.selection

`app.selection`

**Description**

All currently selected objects in the active (frontmost) document.

**Type**

Array of Objects; read-only.

---

### Application.startupPresetsList

`app.startupPresetsList`

**Description**

The list of presets available for creating a new document.

**Type**

Object; read-only.

---

### Application.textFonts

`app.textFonts`

**Description**

The installed fonts.

**Type**

[TextFonts](./TextFonts.md)

---

### Application.tracingPresetList

`app.tracingPresetList`

**Description**

The list of preset tracing-options names available for use.

**Type**

Array of Strings; read-only.

---

### Application.typename

`app.typename`

**Description**

The class name of the referenced object.

**Type**

String; read-only.

---

### Application.userInteractionLevel

`app.userInteractionLevel`

**Description**

What level of interaction with the user should be allowed when handling script commands.

**Type**

[UserInteractionLevel](scripting-constants.md#jsobjref-scripting-constants-userinteractionlevel)

---

### Application.version

`app.version`

**Description**

The application's version.

**Type**

String; read-only.

---

### Application.visible

`app.visible`

**Description**

If `true`, the application is visible.

**Type**

Boolean; read-only.

---

## Methods

### Application.beep()

`app.beep()`

**Description**

Alerts the user.

**Returns**

Nothing.

---

### Application.concatenateMatrix()

`app.concatenateMatrix(matrix, secondMatrix)`

**Description**

Joins two matrices together.

**Parameters**

| Parameter      | Type                                | Description   |
|----------------|-------------------------------------|---------------|
| `matrix`       | [Matrix](./Matrix.md) | First matrix  |
| `secondMatrix` | [Matrix](./Matrix.md) | Second matrix |

**Returns**

jsobjref/Matrix.

---

### Application.concatenateRotationMatrix()

`app.concatenateRotationMatrix(matrix, angle)`

**Description**

Joins a rotation translation to a transformation matrix.

**Parameters**

| Parameter   | Type            | Description   |
|-------------|-----------------|---------------|
| `matrix`    | Matrix          | Matrix        |
| `angle`     | Number (double) | Angle         |

**Returns**

jsobjref/Matrix.

---

### Application.concatenateScaleMatrix()

`app.concatenateScaleMatrix(matrix[, scaleX][, scaleY])`

**Description**

Concatenates a scale translation to a transformation matrix.

**Parameters**

| Parameter   | Type                      | Description   |
|-------------|---------------------------|---------------|
| `matrix`    | Matrix                    | Matrix        |
| `scaleX`    | Number (double), optional | X Scale       |
| `scaleY`    | Number (dobule), optional | Y Scale       |

**Returns**

[Matrix](./Matrix.md)

---

### Application.concatenateTranslationMatrix()

`app.concatenateTranslationMatrix(matrix[, deltaX][, deltaY])`

**Description**

Joins a translation to a transformation matrix.

**Parameters**

| Parameter   | Type                      | Description   |
|-------------|---------------------------|---------------|
| `matrix`    | Matrix                    | Matrix        |
| `deltaX`    | Number (double), optional | X Delta       |
| `deltaY`    | Number (dobule), optional | Y Delta       |

**Returns**

[Matrix](./Matrix.md)

---

### Application.convertSampleColor()

`app.convertSampleColor(sourceColorSpace, sourceColor, destColorSpace, colorConvertPurpose[, sourceHasAlpha][, destHasAlpha])`

**Description**

Converts a sample-component color from one color space to another.

**Parameters**

| Parameter             | Type                                                                                           | Description                       |
|-----------------------|------------------------------------------------------------------------------------------------|-----------------------------------|
| `sourceColorSpace`    | [ImageColorSpace](scripting-constants.md#jsobjref-scripting-constants-imagecolorspace)         | Color space of source color       |
| `sourceColor`         | ColorComponents                                                                                | Source color to convert           |
| `destColorSpace`      | [ImageColorSpace](scripting-constants.md#jsobjref-scripting-constants-imagecolorspace)         | Destination color space           |
| `colorConvertPurpose` | [ColorConvertPurpose](scripting-constants.md#jsobjref-scripting-constants-colorconvertpurpose) | The purpose of the convert        |
| `sourceHasAlpha`      | Boolean, optional                                                                              | Whether the source has alpha      |
| `destHasAlpha`        | Boolean, optional                                                                              | Whether the destination has alpha |

**Returns**

Array of ColorComponents

---

### Application.copy()

`app.copy()`

**Description**

Copies current selection to the clipboard.

**Returns**

Nothing.

---

### Application.cut()

`app.cut()`

**Description**

Cuts current selection to the clipboard.

**Returns**

Nothing.

---

### Application.deleteWorkspace()

`app.deleteWorkspace(workspaceName)`

**Description**

Deletes an existing workspace.

**Parameters**

| Parameter       | Type   | Description                 |
|-----------------|--------|-----------------------------|
| `workspaceName` | String | Name of workspace to delete |

**Returns**

Boolean

---

### Application.getIdentityMatrix()

`app.getIdentityMatrix()`

**Description**

Returns an identity matrix.

**Returns**

[Matrix](./Matrix.md)

---

### Application.getIsFileOpen()

`app.getIsFileOpen(filePath)`

!!! note
    This functionality was added in Illustrator XX.X (CC2017)

**Description**

Returns whether the specified filePath is open

**Parameters**

| Parameter   | Type   | Description        |
|-------------|--------|--------------------|
| `filePath`  | String | File path to check |

**Returns**

Boolean

---

### Application.getPPDFileInfo()

`app.getPPDFileInfo(name)`

**Description**

Gets detailed file information for specified PPD file.

**Parameters**

| Parameter   | Type   | Description               |
|-------------|--------|---------------------------|
| `name`      | String | File name to get info for |

**Returns**

[PPDFileInfo](./PPDFileInfo.md)

---

### Application.getPresetFileOfType()

`app.getPresetFileOfType(presetType)`

**Description**

Returns the full path to the application's default document profile for the specified preset type.

**Parameters**

| Parameter    | Type                                                                                         | Description                |
|--------------|----------------------------------------------------------------------------------------------|----------------------------|
| `presetType` | [DocumentPresetType](scripting-constants.md#jsobjref-scripting-constants-documentpresettype) | Preset type to get file of |

**Returns**

File

---

### Application.getPresetSettings()

`app.getPresetSettings(preset)`

**Description**

Retrieves the tracing-option settings from the template with a given preset name.

**Parameters**

| Parameter   | Type   | Description                      |
|-------------|--------|----------------------------------|
| `preset`    | String | Preset name to get settings from |

**Returns**

[DocumentPreset](./DocumentPreset.md)

---

### Application.getRotationMatrix()

`app.getRotationMatrix([angle])`

**Description**

Returns a transformation matrix containing a single rotation.

!!! note
    Requires a value in degrees.

For example, `30` rotates the object 30 degrees counterclockwise; `-30` rotates the object 30 degrees clockwise.

**Parameters**

| Parameter   | Type                      | Description            |
|-------------|---------------------------|------------------------|
| `angle`     | Number (double), optional | Angle to get matrix of |

**Returns**

[Matrix](./Matrix.md)

---

### Application.getScaleMatrix()

`app.getScaleMatrix([scaleX][, scaleY])`

**Description**

Returns a transformation matrix containing a single scale.

!!! note
    Requires a value in percentage.

For example, `60` scales the object to 60% of its original size; `200` doubles the object's bounds.

**Parameters**

| Parameter   | Type                      | Description              |
|-------------|---------------------------|--------------------------|
| `scaleX`    | Number (double), optional | X scale to get matrix of |
| `scaleY`    | Number (double), optional | Y scale to get matrix of |

**Returns**

[Matrix](./Matrix.md)

---

### Application.getScriptableHelpGroup()

`app.getScriptableHelpGroup()`

**Description**

Gets the scriptable help group object that represents the search widget in the app bar.

**Returns**

Variant

---

### Application.getTranslationMatrix()

`app.getTranslationMatrix([deltaX][, deltaY])`

**Description**

Returns a transformation matrix containing a single translation.

!!! note
    Requires a value in points.

For example, (100, 200) moves the object 100 pt. to the right and 200 pt. up; a minus before each number moves the object left and down.

**Parameters**

| Parameter   | Type                      | Description   |
|-------------|---------------------------|---------------|
| `deltaX`    | Number (double), optional | X Delta       |
| `deltaY`    | Number (dobule), optional | Y Delta       |

**Returns**

[Matrix](./Matrix.md)

---

### Application.invertMatrix()

`app.invertMatrix(matrix)`

**Description**

Inverts a matrix.

**Parameters**

| Parameter   | Type                                | Description      |
|-------------|-------------------------------------|------------------|
| `matrix`    | [Matrix](./Matrix.md) | Matrix to invert |

**Returns**

[Matrix](./Matrix.md)

---

### Application.isEqualMatrix()

`app.isEqualMatrix(matrix, secondMatrix)`

**Description**

Checks whether the two matrices are equal.

**Parameters**

| Parameter      | Type                                | Description            |
|----------------|-------------------------------------|------------------------|
| `matrix`       | [Matrix](./Matrix.md) | First matrix to check  |
| `secondMatrix` | [Matrix](./Matrix.md) | Second matrix to check |

**Returns**

Boolean

---

### Application.isSingularMatrix()

`app.isSingularMatrix(matrix)`

**Description**

Checks whether a matrix is singular and cannot be inverted.

**Parameters**

| Parameter   | Type                                | Description     |
|-------------|-------------------------------------|-----------------|
| `matrix`    | [Matrix](./Matrix.md) | Matrix to check |

**Returns**

Boolean

---

### Application.loadColorSettings()

`app.loadColorSettings(fileSpec)`

**Description**

Loads color settings from specified file, or, if file is empty, turns color management off.

**Parameters**

| Parameter   | Type   | Description                |
|-------------|--------|----------------------------|
| `fileSpec`  | File   | File to load settings from |

**Returns**

Nothing.

---

### Application.open()

`app.open(file[, documentColorSpace][, options])`

**Description**

Opens the specified document file.

!!! note
    If you open a pre-Illustrator 9 document that contains both RGB and CMYK colors and documentColorSpace is supplied, all colors are converted to the specified color space.

If the parameter is not supplied, Illustrator opens a dialog so the user can choose the color space.

**Parameters**

| Parameter            | Type                                                                                                   | Description             |
|----------------------|--------------------------------------------------------------------------------------------------------|-------------------------|
| `file`               | File                                                                                                   | File to open            |
| `documentColorSpace` | [DocumentColorSpace](scripting-constants.md#jsobjref-scripting-constants-documentcolorspace), optional | Color space of document |
| `options`            | anything                                                                                               | todo                    |

**Returns**

[Document](./Document.md)

---

### Application.paste()

`app.paste()`

**Description**

Pastes current clipboard content into the current document.

**Returns**

Nothing.

---

### Application.quit()

`app.quit()`

**Description**

Quits Illustrator.

!!! note
    If the clipboard contains data, Illustrator may show a dialog prompting the user to save the data for other applications.

**Returns**

Nothing.

---

### Application.redo()

`app.redo()`

**Description**

Redoes the most recently undone transaction.

**Returns**

Nothing.

---

### Application.redraw()

`app.redraw()`

**Description**

Forces Illustrator to redraw all its windows.

**Returns**

Nothing.

---

### Application.resetWorkspace()

`app.resetWorkspace()`

**Description**

Resets the current workspace.

**Returns**

Boolean

---

### Application.saveWorkspace()

`app.saveWorkspace(workspaceName)`

**Description**

Saves a new workspace.

**Parameters**

| Parameter       | Type   | Description                  |
|-----------------|--------|------------------------------|
| `workspaceName` | String | Name of workspace to save as |

**Returns**

Boolean

---

### Application.sendScriptMessage()

`app.sendScriptMessage(pluginName, messageSelector, inputString)`

**Description**

Sends a plug-in-defined command message to a plug-in with given input arguments, and returns the plug-in-defined result string.

**Parameters**

| Parameter         | Type   | Description                       |
|-------------------|--------|-----------------------------------|
| `pluginName`      | String | Name of plugin to send message to |
| `messageSelector` | String | Message to send to the plugin     |
| `inputString`     | String | Data to pass into the command     |

**Returns**

String

---

### Application.showPresets()

`app.showPresets(fileSpec)`

**Description**

Gets presets from the file.

**Parameters**

| Parameter   | Type   | Description              |
|-------------|--------|--------------------------|
| `fileSpec`  | File   | File to get presets from |

**Returns**

PrintPresetList

---

### Application.switchWorkspace()

`app.switchWorkspace(workspaceName)`

**Description**

Switches to the specified workspace.

**Parameters**

| Parameter       | Type   | Description       |
|-----------------|--------|-------------------|
| `workspaceName` | String | Name to switch to |

**Returns**

Boolean

---

### Application.translatePlaceholderText()

`app.translatePlaceholderText(text)`

**Description**

Translates the placeholder text to regular text (a way to enter Unicode points in hex values).

**Parameters**

| Parameter   | Type   | Description         |
|-------------|--------|---------------------|
| `text`      | String | String to translate |

**Returns**

String

---

### Application.undo()

`app.undo()`

**Description**

Undoes the most recent transaction.

**Returns**

Nothing.

---

## Example

### Duplicating the Active Document

```default
// Duplicates any selected items from
// the active document into a new document.

var newItem;
var docSelected = app.activeDocument.selection;

if (docSelected.length > 0) {
  // Create a new document and move the selected items to it.
  var newDoc = app.documents.add();
  if (docSelected.length > 0) {
    for (var i = 0; i < docSelected.length; i++) {
      docSelected[i].selected = false;
      newItem = docSelected[i].duplicate(newDoc, ElementPlacement.PLACEATEND);
    }
  } else {
    docSelected.selected = false;
    newItem = docSelected.parent.duplicate(newDoc, ElementPlacement.PLACEATEND);
  }
} else {
  alert("Please select one or more art objects");
}
```

.. _application:

Application
###########

``app``

**Description**

The Adobe® Illustrator® application object, referenced using the pre-defined
global app object, which contains all other Illustrator objects.

----

==========
Properties
==========

.. _app.activeDocument:

app.activeDocument
********************************************************************************

``app.activeDocument``

**Description**

The active (frontmost) document in Illustrator.

**Type**

`Document <#document>`__

---

.. _app.browserAvailable:

app.browserAvailable
********************************************************************************

``app.browserAvailable``

**Description**

If ``true``, a web browser is available.

**Type**

Boolean; read-only.

---

.. _app.buildNumber:

app.buildNumber
********************************************************************************

``app.buildNumber``

**Description**

The application’s build number.

**Type**

String; read-only.

---

.. _app.colorSettingsList:

app.colorSettingsList
********************************************************************************

``app.colorSettingsList``

**Description**

The list of color-settings files currently
available for use.

**Type**

Object; read-only.

---

.. _app.coordinateSystem:

app.coordinateSystem
********************************************************************************

``app.coordinateSystem``

**Description**

The coordinate system currently in use,
document or artboard.

**Type**

`CoordinateSystem <#coordinatesystem>`__

---

.. _app.defaultColorSettings:

app.defaultColorSettings
********************************************************************************

``app.defaultColorSettings``

**Description**

The default color-settings file for the
current application locale.

**Type**

File; read-only.

---

.. _app.documents:

app.documents
********************************************************************************

``app.documents``

**Description**

The documents in the application.

**Type**

`Documents <#documents>`__

---

.. _app.flattenerPresetList:

app.flattenerPresetList
********************************************************************************

``app.flattenerPresetList``

**Description**

The list of flattener style names
currently available for use.

**Type**

Object; read-only.

---

.. _app.freeMemory:

app.freeMemory
********************************************************************************

``app.freeMemory``

**Description**

The amount of unused memory (in
bytes) within the Illustrator partition.

**Type**

Number (long); read-only.

---

.. _app.locale:

app.locale
********************************************************************************

``app.locale``

**Description**

The application’s locale.

**Type**

String; read-only.

---

.. _app.name:

app.name
********************************************************************************

``app.name``

**Description**

The application’s name (not related to
the filename of the application file).

**Type**

String; read-only.

---

.. _app.pasteRememberLayers:

app.pasteRememberLayers
********************************************************************************

``app.pasteRememberLayers``

**Description**

If ``true``, the paste operation maintains the layer structure.

**Type**

Boolean; read-only.

---

.. _app.path:

app.path
********************************************************************************

``app.path``

**Description**

The file path to the application.

**Type**

File; read-only.

---

.. _app.PDFPresetsList:

app.PDFPresetsList
********************************************************************************

``app.PDFPresetsList``

**Description**

The list of preset PDF-options names
available for use.

**Type**

Object; read-only.

---

.. _app.PPDFileList:

app.PPDFileList
********************************************************************************

``app.PPDFileList``

**Description**

The list of PPD files currently available
for use.

**Type**

Object; read-only.

---

.. _app.preferences:

app.preferences
********************************************************************************

``app.preferences``

**Description**

Illustrator’s preference settings.

**Type**

`Preferences <#preferences>`__

---

.. _app.printerList:

app.printerList
********************************************************************************

``app.printerList``

**Description**

The list of installed printers.

**Type**

Array of `Printer <#printer>`__

---

.. _app.printPresetsList:

app.printPresetsList
********************************************************************************

``app.printPresetsList``

**Description**

The list of preset printing-options names available for use.

**Type**

Object; read-only.

---

.. _app.scriptingVersion:

app.scriptingVersion
********************************************************************************

``app.scriptingVersion``

**Description**

The version of the Scripting plug-in.

**Type**

String; read-only.

---

.. _app.selection:

app.selection
********************************************************************************

``app.selection``

**Description**

All currently selected objects in the active (frontmost) document.

**Type**

Array of Objects; read-only.

---

.. _app.startupPresetsList:

app.startupPresetsList
********************************************************************************

``app.startupPresetsList``

**Description**

The list of presets available for creating a new document.

**Type**

Object; read-only.

---

.. _app.textFonts:

app.textFonts
********************************************************************************

``app.textFonts``

**Description**

The installed fonts.

**Type**

`TextFonts <#textfonts>`__

---

.. _app.tracingPresetList:

app.tracingPresetList
********************************************************************************

``app.tracingPresetList``

**Description**

The list of preset tracing-options
names available for use.

**Type**

Array of Strings; read-only.

---

.. _app.typename:

app.typename
********************************************************************************

``app.typename``

**Description**

The class name of the referenced object.

**Type**

String; read-only.

---

.. _app.userInteractionLevel:

app.userInteractionLevel
********************************************************************************

``app.userInteractionLevel``

**Description**

What level of interaction with the user should be allowed when handling
script commands.

**Type**

`UserInteractionLevel <#userinteractionlevel>`__

---

.. _app.version:

app.version
********************************************************************************

``app.version``

**Description**

The application’s version.

**Type**

String; read-only.

---

.. _app.visible:

app.visible
********************************************************************************

``app.visible``

**Description**

If ``true``, the application is visible.

**Type**

Boolean; read-only.

---

=======
Methods
=======

.. _app.beep:

app.beep()
********************************************************************************

``app.beep()``

**Description**

Alerts the user.

**Returns**

Nothing.

----

.. _app.concatenateMatrix:

app.concatenateMatrix()
********************************************************************************

``app.concatenateMatrix(matrix, secondMatrix)``

**Description**

Joins two matrices together.

**Parameters**

============  ======  =============
matrix        Matrix  First matrix
secondMatrix  Matrix  Second matrix
============  ======  =============

**Returns**

Matrix

----

.. _app.concatenateRotationMatrix:

app.concatenateRotationMatrix()
********************************************************************************

``app.concatenateRotationMatrix(matrix, angle)``

**Description**

Joins a rotation translation to a transformation matrix.

**Parameters**

======  ===============  ===============
matrix  Matrix           Matrix
angle   Number (double)  Angle
======  ===============  ===============

**Returns**

Matrix

----

.. _app.concatenateScaleMatrix:

app.concatenateScaleMatrix()
********************************************************************************

``app.concatenateScaleMatrix(matrix[, scaleX][, scaleY])``

**Description**

Concatenates a scale translation to a transformation matrix.

**Parameters**

========  =========================  =======
matrix    Matrix                     Matrix
[scaleX]  Number (double), optional  X Scale
[scaleY]  Number (dobule), optional  Y Scale
========  =========================  =======

**Returns**

Matrix

----

.. _app.concatenateTranslationMatrix:

app.concatenateTranslationMatrix()
********************************************************************************

``app.concatenateTranslationMatrix(matrix[, deltaX][, deltaY])``

**Description**

Joins a translation to a transformation matrix.

**Parameters**

========  =========================  =======
matrix    Matrix                     Matrix
[deltaX]  Number (double), optional  X Delta
[deltaY]  Number (dobule), optional  Y Delta
========  =========================  =======

**Returns**

Matrix

----

.. _app.convertSampleColor:

app.convertSampleColor()
********************************************************************************

``app.convertSampleColor(sourceColorSpace, sourceColor, destColorSpace, colorConvertPurpose[, sourceHasAlpha][, destHasAlpha])``

**Description**

Converts a sample-component color from one color space to another.

**Parameters**

===================  ==============================================  ====
sourceColorSpace     `ImageColorSpace <#imagecolorspace>`__          todo
sourceColor          ColorComponents                                 todo
destColorSpace       `ImageColorSpace <#imagecolorspace>`__          todo
colorConvertPurpose  `ColorConvertPurpose <#colorconvertpurpose>`__  todo
[sourceHasAlpha]     Boolean, optional                               todo
[destHasAlpha]       Boolean, optional                               todo
===================  ==============================================  ====

**Returns**

Array of ColorComponents

----

.. _app.copy:

app.copy()
********************************************************************************

``app.copy()``

**Description**

Copies current selection to the clipboard.

**Returns**

Nothing.

----

.. _app.cut:

app.cut()
********************************************************************************

``app.cut()``

**Description**

Cuts current selection to the clipboard.

**Returns**

Nothing.


----

.. _app.deleteWorkspace:

app.deleteWorkspace()
********************************************************************************

``app.deleteWorkspace(workspaceName)``

**Description**

Deletes an existing workspace.

**Parameters**

=============  ======  ===========================
workspaceName  String  Name of workspace to delete
=============  ======  ===========================

**Returns**

Boolean

----

.. _app.getIdentityMatrix:

app.getIdentityMatrix()
********************************************************************************

``app.getIdentityMatrix()``

**Description**

Returns an identity matrix.

**Returns**

Matrix

----

.. _app.getIsFileOpen:

app.getIsFileOpen()
********************************************************************************

``app.getIsFileOpen(filePath)``

.. note::
   This functionality was added in Illustrator XX.X (CC2017)

**Description**

Returns whether the specified filePath is open

**Parameters**

========  ======  ===============
filePath  String  todo
========  ======  ===============

**Returns**

Boolean

----

.. _app.getPPDFileInfo:

app.getPPDFileInfo()
********************************************************************************

``app.getPPDFileInfo(name)``

**Description**

Gets detailed file information for specified PPD file.

**Parameters**

====  ======  ===============
name  String  todo
====  ======  ===============

**Returns**

`PPDFileInfo <#ppdfileinfo>`__

----

.. _app.getPresetFileOfType:

app.getPresetFileOfType()
********************************************************************************

``app.getPresetFileOfType(presetType)``

**Description**

Returns the full path to the application’s default document profile for the
specified preset type.

**Parameters**

==========  ============================================  ====
presetType  `DocumentPresetType <#documentpresettype>`__  todo
==========  ============================================  ====

**Returns**

File

----

.. _app.getPresetSettings:

app.getPresetSettings()
********************************************************************************

``app.getPresetSettings(preset)``

**Description**

Retrieves the tracing-option settings from the template with
a given preset name.

**Parameters**

======  ======  ====
preset  String  todo
======  ======  ====

**Returns**

`DocumentPreset <#documentpreset>`__

----

.. _app.getRotationMatrix:

app.getRotationMatrix()
********************************************************************************

``app.getRotationMatrix([angle])``

**Description**

Returns a transformation matrix containing a single rotation.

.. note::
    Requires a value in degrees. For example, 30 rotates the object 30
    degrees counterclockwise;
    -30 rotates the object 30 degrees clockwise.

**Parameters**

=======  =========================  ====
[angle]  Number (double), optional  todo
=======  =========================  ====

**Returns**

Matrix

----

.. _app.getScaleMatrix:

app.getScaleMatrix()
********************************************************************************

``app.getScaleMatrix([scaleX][, scaleY])``

**Description**

Returns a transformation matrix containing a single scale.

.. note::
    Requires a value in percentage.

    For example, `60` scales the object to 60% of its original size;
    `200` doubles the object’s bounds.

**Parameters**

========  =========================  ====
[scaleX]  Number (double), optional  todo
[scaleY]  Number (double), optional  todo
========  =========================  ====

**Returns**

Matrix

----

.. _app.getScriptableHelpGroup:

app.getScriptableHelpGroup()
********************************************************************************

``app.getScriptableHelpGroup()``

**Description**

Gets the scriptable help group object that represents the search widget in
the app bar.

**Returns**

Variant

----

.. _app.getTranslationMatrix:

app.getTranslationMatrix()
********************************************************************************

``app.getTranslationMatrix([deltaX][, deltaY])``

**Description**

Returns a transformation matrix containing a single translation.

.. note::
    Requires a value in points.

    For example, `(100, 200)` moves the object 100 pt. to the right and
    200 pt. up;
    a minus before each number moves the object left and down.

**Parameters**

========  =========================  =======
[deltaX]  Number (double), optional  X Delta
[deltaY]  Number (dobule), optional  Y Delta
========  =========================  =======

**Returns**

Matrix

----

.. _app.invertMatrix:

app.invertMatrix()
********************************************************************************

``app.invertMatrix(matrix)``

**Description**

Inverts a matrix.

**Parameters**

======  ======  ====
matrix  Matrix  todo
======  ======  ====

**Returns**

Matrix

----

.. _app.isEqualMatrix:

app.isEqualMatrix()
********************************************************************************

``app.isEqualMatrix(matrix, secondMatrix)``

**Description**

Checks whether the two matrices are equal.

**Parameters**

============  ======  ====
matrix        Matrix  todo
secondMatrix  Matrix  todo
============  ======  ====

**Returns**

Boolean

----

.. _app.isSingularMatrix:

app.isSingularMatrix()
********************************************************************************

``app.isSingularMatrix(matrix)``

**Description**

Checks whether a matrix is singular and cannot be inverted.

**Parameters**

======  ======  ===============
matrix  Matrix  Matrix to check
======  ======  ===============

**Returns**

Boolean

----

.. _app.loadColorSettings:

app.loadColorSettings()
********************************************************************************

``app.loadColorSettings(fileSpec)``

**Description**

Loads color settings from specified file, or, if file is empty, turns color
management off.

**Parameters**

========  ====  ====
fileSpec  File  todo
========  ====  ====

**Returns**

Nothing.

----

.. _app.open:

app.open()
********************************************************************************

``app.open(file[, documentColorSpace][, options])``

**Description**

Opens the specified document file.

.. note::
    If you open a pre-Illustrator 9 document that contains both RGB and CMYK
    colors and `documentColorSpace` is supplied, all colors are converted to
    the specified color space.

    If the parameter is not supplied, Illustrator opens a dialog so the user
    can choose the color space.

**Parameters**

====================  ============================================  ====
file                  File                                          todo
[documentColorSpace]  `DocumentColorSpace <#documentcolorspace>`__  todo
[options]             anything                                      todo
====================  ============================================  ====

**Returns**

`Document <#document>`__

----

.. _app.paste:

app.paste()
********************************************************************************

``app.paste()``

**Description**

Pastes current clipboard content into the current document.

**Returns**

Nothing.

----

.. _app.quit:

app.quit()
********************************************************************************

``app.quit()``

**Description**

Quits Illustrator.

.. note::
   If the clipboard contains data, Illustrator may show a dialog prompting the user to save the data for other applications.

**Returns**

Nothing.

----

.. _app.redo:

app.redo()
********************************************************************************

``app.redo()``

**Description**

Redoes the most recently undone transaction.

**Returns**

Nothing.

----

.. _app.redraw:

app.redraw()
********************************************************************************

``app.redraw()``

**Description**

Forces Illustrator to redraw all its windows.

**Returns**

Nothing.

----

.. _app.resetWorkspace:

app.resetWorkspace()
********************************************************************************

``app.resetWorkspace()``

**Description**

Resets the current workspace.

**Returns**

Boolean

----

.. _app.saveWorkspace:

app.saveWorkspace()
********************************************************************************

``app.saveWorkspace(workspaceName)``

**Description**

Saves a new workspace.

**Parameters**

=============  ===============  ============================
workspaceName  String           Name of workspace to save as
=============  ===============  ============================

**Returns**

Boolean

----

.. _app.sendScriptMessage:

app.sendScriptMessage()
********************************************************************************

``app.sendScriptMessage(pluginName, messageSelector, inputString)``

**Description**

Sends a plug-in-defined command message to a plug-in with given input
arguments, and returns the plug-in-defined result string.

**Parameters**

===============  ======  ===============
pluginName       String  todo
messageSelector  String  todo
inputString      String  todo
===============  ======  ===============

**Returns**

String

----

.. _app.showPresets:

app.showPresets()
********************************************************************************

``app.showPresets(fileSpec)``

**Description**

Gets presets from the file.

**Parameters**

========  ====  ===============
fileSpec  File  File?
========  ====  ===============

**Returns**

PrintPresetList

----

.. _app.switchWorkspace:

app.switchWorkspace()
********************************************************************************

``app.switchWorkspace(workspaceName)``

**Description**

Switches to the specified workspace.

**Parameters**

=============  ======  =================
workspaceName  String  Name to switch to
=============  ======  =================

**Returns**

Boolean

----

.. _app.translatePlaceholderText:

app.translatePlaceholderText()
********************************************************************************

``app.translatePlaceholderText(text)``

**Description**

Translates the placeholder text to regular text (a way to enter Unicode points
in hex values).

**Parameters**

=============  ===============  ===================
text           String           String to translate
=============  ===============  ===================

**Returns**

String

----

.. _app.undo:

app.undo()
********************************************************************************

``app.undo()``

**Description**

Undoes the most recent transaction.

**Returns**

Nothing.

----

=======
Example
=======

Duplicating the Active Document
*******************************

::

  // Duplicates any selected items from
  // the active document into a new document.
  var newItem;
  var docSelected = app.activeDocument.selection;

  if ( docSelected.length > 0 ) {
    // Create a new document and move the selected items to it.
    var newDoc = app.documents.add()
    if ( docSelected.length > 0 ) {
      for ( i = 0; i < docSelected.length; i++ ) {
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

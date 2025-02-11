<a id="jsobjref-exportoptionsautocad"></a>

# ExportOptionsAutoCAD

`exportOptionsAutoCAD`

**Description**

Options for exporting a document as an AutoCAD file, used with the [Document.exportFile()](Document.md#jsobjref-document-exportfile) method.
All properties are optional.

When you export a document, a file extension is appended automatically. You should not include any file extension in the file specification.

To override the default AutoCAD export format (DWG), use the [ExportOptionsAutoCAD.exportFileFormat](#jsobjref-exportoptionsautocad-exportfileformat) property.

---

## Properties

<a id="jsobjref-exportoptionsautocad-alterpathsforappearance"></a>

### ExportOptionsAutoCAD.alterPathsForAppearance

`exportOptionsAutoCAD.alterPathsForAppearance`

**Description**

If `true`, paths are altered if needed to maintain appearance.

Default: `false`.

**Type**

Boolean.

---

<a id="jsobjref-exportoptionsautocad-colors"></a>

### ExportOptionsAutoCAD.colors

`exportOptionsAutoCAD.colors`

**Description**

The colors exported into the AutoCAD file.

**Type**

[AutoCADColors](scripting-constants.md#jsobjref-scripting-constants-autocadcolors)

---

<a id="jsobjref-exportoptionsautocad-converttexttooutlines"></a>

### ExportOptionsAutoCAD.convertTextToOutlines

`exportOptionsAutoCAD.convertTextToOutlines`

**Description**

If `true`, text is converted to vector paths; preserves the visual appearance of type.

Default: `false`.

**Type**

Boolean.

---

<a id="jsobjref-exportoptionsautocad-exportfileformat"></a>

### ExportOptionsAutoCAD.exportFileFormat

`exportOptionsAutoCAD.exportFileFormat`

**Description**

The format to which the file is exported.

Default: `AutoCADExportFileFormat.DWG`.

**Type**

[AutoCADExportFileFormat](scripting-constants.md#jsobjref-scripting-constants-autocadexportfileformat)

---

<a id="jsobjref-exportoptionsautocad-exportoption"></a>

### ExportOptionsAutoCAD.exportOption

`exportOptionsAutoCAD.exportOption`

**Description**

Specifies whether to preserve appearance or editability during export.

Default: `AutoCADExportOption.MaximizeEditability`.

**Type**

[AutoCADExportOption](scripting-constants.md#jsobjref-scripting-constants-autocadexportoption)

---

<a id="jsobjref-exportoptionsautocad-exportselectedartonly"></a>

### ExportOptionsAutoCAD.exportSelectedArtOnly

`exportOptionsAutoCAD.exportSelectedArtOnly`

**Description**

If `true`, only selected artwork is exported.

Default: `false`.

**Type**

Boolean.

---

<a id="jsobjref-exportoptionsautocad-rasterformat"></a>

### ExportOptionsAutoCAD.rasterFormat

`exportOptionsAutoCAD.rasterFormat`

**Description**

The format in which raster art is exported.

**Type**

[AutoCADRasterFormat](scripting-constants.md#jsobjref-scripting-constants-autocadrasterformat)

---

<a id="jsobjref-exportoptionsautocad-scalelineweights"></a>

### ExportOptionsAutoCAD.scaleLineweights

`exportOptionsAutoCAD.scaleLineweights`

**Description**

If `true`, line weights are scaled by the same scaling factor as the rest of the drawing.

Default: `false`.

**Type**

Boolean.

---

<a id="jsobjref-exportoptionsautocad-typename"></a>

### ExportOptionsAutoCAD.typename

`exportOptionsAutoCAD.typename`

**Description**

The class name of the referenced object.

**Type**

String, read-only.

---

<a id="jsobjref-exportoptionsautocad-unit"></a>

### ExportOptionsAutoCAD.unit

`exportOptionsAutoCAD.unit`

**Description**

The measurement units from which to map.

**Type**

[AutoCADUnit](scripting-constants.md#jsobjref-scripting-constants-autocadunit)

---

<a id="jsobjref-exportoptionsautocad-unitscaleratio"></a>

### ExportOptionsAutoCAD.unitScaleRatio

`exportOptionsAutoCAD.unitScaleRatio`

**Description**

The ratio (as a percentage) by which output is scaled.

Range: 0 to 1000

**Type**

Number (double).

---

<a id="jsobjref-exportoptionsautocad-version"></a>

### ExportOptionsAutoCAD.version

`exportOptionsAutoCAD.version`

**Description**

The release of AutoCAD to which the file is exported.

Default: `AutoCADCompatibility.AutoCADRelease24`.

**Type**

[AutoCADCompatibility](scripting-constants.md#jsobjref-scripting-constants-autocadcompatibility)

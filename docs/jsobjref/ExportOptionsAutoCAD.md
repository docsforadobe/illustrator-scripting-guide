# ExportOptionsAutoCAD

`exportOptionsAutoCAD`

**Description**

Options for exporting a document as an AutoCAD file, used with the [Document.exportFile()](Document.md#jsobjref-document-exportfile) method.
All properties are optional.

When you export a document, a file extension is appended automatically. You should not include any file extension in the file specification.

To override the default AutoCAD export format (DWG), use the [ExportOptionsAutoCAD.exportFileFormat](#jsobjref-exportoptionsautocad-exportfileformat) property.

---

## Properties

### ExportOptionsAutoCAD.alterPathsForAppearance

`exportOptionsAutoCAD.alterPathsForAppearance`

**Description**

If `true`, paths are altered if needed to maintain appearance.

Default: `false`.

**Type**

Boolean.

---

### ExportOptionsAutoCAD.colors

`exportOptionsAutoCAD.colors`

**Description**

The colors exported into the AutoCAD file.

**Type**

[AutoCADColors](scripting-constants.md#jsobjref-scripting-constants-autocadcolors)

---

### ExportOptionsAutoCAD.convertTextToOutlines

`exportOptionsAutoCAD.convertTextToOutlines`

**Description**

If `true`, text is converted to vector paths; preserves the visual appearance of type.

Default: `false`.

**Type**

Boolean.

---

### ExportOptionsAutoCAD.exportFileFormat

`exportOptionsAutoCAD.exportFileFormat`

**Description**

The format to which the file is exported.

Default: `AutoCADExportFileFormat.DWG`.

**Type**

[AutoCADExportFileFormat](scripting-constants.md#jsobjref-scripting-constants-autocadexportfileformat)

---

### ExportOptionsAutoCAD.exportOption

`exportOptionsAutoCAD.exportOption`

**Description**

Specifies whether to preserve appearance or editability during export.

Default: `AutoCADExportOption.MaximizeEditability`.

**Type**

[AutoCADExportOption](scripting-constants.md#jsobjref-scripting-constants-autocadexportoption)

---

### ExportOptionsAutoCAD.exportSelectedArtOnly

`exportOptionsAutoCAD.exportSelectedArtOnly`

**Description**

If `true`, only selected artwork is exported.

Default: `false`.

**Type**

Boolean.

---

### ExportOptionsAutoCAD.rasterFormat

`exportOptionsAutoCAD.rasterFormat`

**Description**

The format in which raster art is exported.

**Type**

[AutoCADRasterFormat](scripting-constants.md#jsobjref-scripting-constants-autocadrasterformat)

---

### ExportOptionsAutoCAD.scaleLineweights

`exportOptionsAutoCAD.scaleLineweights`

**Description**

If `true`, line weights are scaled by the same scaling factor as the rest of the drawing.

Default: `false`.

**Type**

Boolean.

---

### ExportOptionsAutoCAD.typename

`exportOptionsAutoCAD.typename`

**Description**

The class name of the referenced object.

**Type**

String, read-only.

---

### ExportOptionsAutoCAD.unit

`exportOptionsAutoCAD.unit`

**Description**

The measurement units from which to map.

**Type**

[AutoCADUnit](scripting-constants.md#jsobjref-scripting-constants-autocadunit)

---

### ExportOptionsAutoCAD.unitScaleRatio

`exportOptionsAutoCAD.unitScaleRatio`

**Description**

The ratio (as a percentage) by which output is scaled.

Range: 0 to 1000

**Type**

Number (double).

---

### ExportOptionsAutoCAD.version

`exportOptionsAutoCAD.version`

**Description**

The release of AutoCAD to which the file is exported.

Default: `AutoCADCompatibility.AutoCADRelease24`.

**Type**

[AutoCADCompatibility](scripting-constants.md#jsobjref-scripting-constants-autocadcompatibility)

<a id="jsobjref-openoptionsautocad"></a>

# OpenOptionsAutoCAD

`openOptionsAutoCAD`

**Description**

Options for opening an AutoCAD drawing, used with the [Application.open()](Application.md#jsobjref-application-open) method.

---

## Properties

<a id="jsobjref-openoptionsautocad-centerartwork"></a>

### OpenOptionsAutoCAD.centerArtwork

`openOptionsAutoCAD.centerArtwork`

**Description**

If `true`, the artwork is centered on the artboard. Default: `true`.

**Type**

Boolean.

---

<a id="jsobjref-openoptionsautocad-globalscaleoption"></a>

### OpenOptionsAutoCAD.globalScaleOption

`openOptionsAutoCAD.globalScaleOption`

**Description**

How to scale the drawing on import. Default: `AutoCADGlobalScaleOption.FitArtboard`.

**Type**

[AutoCADGlobalScaleOption](scripting-constants.md#jsobjref-scripting-constants-autocadglobalscaleoption)

---

<a id="jsobjref-openoptionsautocad-globalscalepercent"></a>

### OpenOptionsAutoCAD.globalScalePercent

`openOptionsAutoCAD.globalScalePercent`

**Description**

The value when `globalScaleOption` is `AutoCADGlobalScaleOption.ScaleByValue`, expressed as a percentage. Range: 0.0 to 100.0. Default is 100.0.

**Type**

Number (double).

---

<a id="jsobjref-openoptionsautocad-mergelayers"></a>

### OpenOptionsAutoCAD.mergeLayers

`openOptionsAutoCAD.mergeLayers`

**Description**

If `true`, the layers of the artwork are merged. Default: `false`.

**Type**

Boolean.

---

<a id="jsobjref-openoptionsautocad-parent"></a>

### OpenOptionsAutoCAD.parent

`openOptionsAutoCAD.parent`

**Description**

The object’s container.

**Type**

Object, read-only.

---

<a id="jsobjref-openoptionsautocad-scalelineweights"></a>

### OpenOptionsAutoCAD.scaleLineweights

`openOptionsAutoCAD.scaleLineweights`

**Description**

If `true`, line weights are scaled by the same factor as the rest of the drawing. Default: `false`.

**Type**

Boolean.

---

<a id="jsobjref-openoptionsautocad-selectedlayoutname"></a>

### OpenOptionsAutoCAD.selectedLayoutName

`openOptionsAutoCAD.selectedLayoutName`

**Description**

The name of the layout in the drawing to import.

**Type**

String.

---

<a id="jsobjref-openoptionsautocad-typename"></a>

### OpenOptionsAutoCAD.typename

`openOptionsAutoCAD.typename`

**Description**

The class name of the object.

**Type**

String, read-only.

---

<a id="jsobjref-openoptionsautocad-unit"></a>

### OpenOptionsAutoCAD.unit

`openOptionsAutoCAD.unit`

**Description**

The unit to map to. Default: `AutoCADUnit.Millimeters`.

**Type**

[AutoCADUnit](scripting-constants.md#jsobjref-scripting-constants-autocadunit)

---

<a id="jsobjref-openoptionsautocad-unitscaleratio"></a>

### OpenOptionsAutoCAD.unitScaleRatio

`openOptionsAutoCAD.unitScaleRatio`

**Description**

The ratio by which to scale while mapping units. Default: 1.0.

**Type**

Number (double).

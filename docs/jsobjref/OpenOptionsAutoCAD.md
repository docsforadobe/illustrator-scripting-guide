# OpenOptionsAutoCAD

`openOptionsAutoCAD`

#### Description

Options for opening an AutoCAD drawing, used with the [Application.open()](Application.md#jsobjref-application-open) method.

---

## Properties

### OpenOptionsAutoCAD.centerArtwork

`openOptionsAutoCAD.centerArtwork`

#### Description

If `true`, the artwork is centered on the artboard. Default: `true`.

#### Type

Boolean.

---

### OpenOptionsAutoCAD.globalScaleOption

`openOptionsAutoCAD.globalScaleOption`

#### Description

How to scale the drawing on import. Default: `AutoCADGlobalScaleOption.FitArtboard`.

#### Type

[AutoCADGlobalScaleOption](scripting-constants.md#jsobjref-scripting-constants-autocadglobalscaleoption)

---

### OpenOptionsAutoCAD.globalScalePercent

`openOptionsAutoCAD.globalScalePercent`

#### Description

The value when `globalScaleOption` is `AutoCADGlobalScaleOption.ScaleByValue`, expressed as a percentage. Range: 0.0 to 100.0. Default is 100.0.

#### Type

Number (double).

---

### OpenOptionsAutoCAD.mergeLayers

`openOptionsAutoCAD.mergeLayers`

#### Description

If `true`, the layers of the artwork are merged. Default: `false`.

#### Type

Boolean.

---

### OpenOptionsAutoCAD.parent

`openOptionsAutoCAD.parent`

#### Description

The object's container.

#### Type

Object, read-only.

---

### OpenOptionsAutoCAD.scaleLineweights

`openOptionsAutoCAD.scaleLineweights`

#### Description

If `true`, line weights are scaled by the same factor as the rest of the drawing. Default: `false`.

#### Type

Boolean.

---

### OpenOptionsAutoCAD.selectedLayoutName

`openOptionsAutoCAD.selectedLayoutName`

#### Description

The name of the layout in the drawing to import.

#### Type

String.

---

### OpenOptionsAutoCAD.typename

`openOptionsAutoCAD.typename`

#### Description

The class name of the object.

#### Type

String, read-only.

---

### OpenOptionsAutoCAD.unit

`openOptionsAutoCAD.unit`

#### Description

The unit to map to. Default: `AutoCADUnit.Millimeters`.

#### Type

[AutoCADUnit](scripting-constants.md#jsobjref-scripting-constants-autocadunit)

---

### OpenOptionsAutoCAD.unitScaleRatio

`openOptionsAutoCAD.unitScaleRatio`

#### Description

The ratio by which to scale while mapping units. Default: 1.0.

#### Type

Number (double).

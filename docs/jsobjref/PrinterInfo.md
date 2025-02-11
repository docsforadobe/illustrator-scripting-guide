<a id="jsobjref-printerinfo"></a>

# PrinterInfo

`printerInfo`

**Description**

Configuration information about a printer.

---

## Properties

<a id="jsobjref-printerinfo-binaryprintingsupport"></a>

### PrinterInfo.binaryPrintingSupport

`printerInfo.binaryPrintingSupport`

**Description**

If `true`, the printer supports binary printing.

**Type**

Boolean

---

<a id="jsobjref-printerinfo-colorsupport"></a>

### PrinterInfo.colorSupport

`printerInfo.colorSupport`

**Description**

The printer color capability.

**Type**

[PrinterColorMode](scripting-constants.md#jsobjref-scripting-constants-printercolormode)

---

<a id="jsobjref-printerinfo-custompapersupport"></a>

### PrinterInfo.customPaperSupport

`printerInfo.customPaperSupport`

**Description**

If `true`, the printer supports custom paper size.

**Type**

Boolean

---

<a id="jsobjref-printerinfo-custompapertransversesupport"></a>

### PrinterInfo.customPaperTransverseSupport

`printerInfo.customPaperTransverseSupport`

**Description**

If `true`, the printer supports custom paper transverse.

**Type**

Boolean

---

<a id="jsobjref-printerinfo-deviceresolution"></a>

### PrinterInfo.deviceResolution

`printerInfo.deviceResolution`

**Description**

The printer default resolution.

**Type**

Number (double)

---

<a id="jsobjref-printerinfo-inripseparationsupport"></a>

### PrinterInfo.inRIPSeparationSupport

`printerInfo.inRIPSeparationSupport`

**Description**

If `true`, the printer supports InRIP color separation.

**Type**

Boolean

---

<a id="jsobjref-printerinfo-maxdeviceresolution"></a>

### PrinterInfo.maxDeviceResolution

`printerInfo.maxDeviceResolution`

**Description**

The printer maximum device resolution.

**Type**

Number (double)

---

<a id="jsobjref-printerinfo-maxpaperheight"></a>

### PrinterInfo.maxPaperHeight

`printerInfo.maxPaperHeight`

**Description**

Custom paper’s maximum height.

**Type**

Number (double)

---

<a id="jsobjref-printerinfo-maxpaperheightoffset"></a>

### PrinterInfo.maxPaperHeightOffset

`printerInfo.maxPaperHeightOffset`

**Description**

Custom paper’s maximum height offset.

**Type**

Number (double)

---

<a id="jsobjref-printerinfo-maxpaperwidth"></a>

### PrinterInfo.maxPaperWidth

`printerInfo.maxPaperWidth`

**Description**

Custom paper’s maximum width.

**Type**

Number (double)

---

<a id="jsobjref-printerinfo-maxpaperwidthoffset"></a>

### PrinterInfo.maxPaperWidthOffset

`printerInfo.maxPaperWidthOffset`

**Description**

Custom paper’s maximum width offset.

**Type**

Number (double)

---

<a id="jsobjref-printerinfo-minpaperheight"></a>

### PrinterInfo.minPaperHeight

`printerInfo.minPaperHeight`

**Description**

Custom paper’s minimum height.

**Type**

Number (double)

---

<a id="jsobjref-printerinfo-minpaperheightoffset"></a>

### PrinterInfo.minPaperHeightOffset

`printerInfo.minPaperHeightOffset`

**Description**

Custom paper’s minimum height offset.

**Type**

Number (double)

---

<a id="jsobjref-printerinfo-minpaperwidth"></a>

### PrinterInfo.minPaperWidth

`printerInfo.minPaperWidth`

**Description**

Custom paper’s minimum width.

**Type**

Number (double)

---

<a id="jsobjref-printerinfo-minpaperwidthoffset"></a>

### PrinterInfo.minPaperWidthOffset

`printerInfo.minPaperWidthOffset`

**Description**

Custom paper’s minimum width offset.

**Type**

Number (double)

---

<a id="jsobjref-printerinfo-papersizes"></a>

### PrinterInfo.paperSizes

`printerInfo.paperSizes`

**Description**

The list of supported paper sizes.

**Type**

Array of [Paper](Paper.md#jsobjref-paper)

---

<a id="jsobjref-printerinfo-postscriptlevel"></a>

### PrinterInfo.postScriptLevel

`printerInfo.postScriptLevel`

**Description**

The PostScript Language level.

**Type**

[PrinterPostScriptLevelEnum](scripting-constants.md#jsobjref-scripting-constants-printerpostscriptlevelenum)

---

<a id="jsobjref-printerinfo-printertype"></a>

### PrinterInfo.printerType

`printerInfo.printerType`

**Description**

The printer type.

**Type**

[PrinterTypeEnum](scripting-constants.md#jsobjref-scripting-constants-printertypeenum)

---

<a id="jsobjref-printerinfo-typename"></a>

### PrinterInfo.typename

`printerInfo.typename`

**Description**

The class name of the object.

**Type**

String; read-only.

---

## Example

### Finding available printers

```default
// Displays a list of available printers in a new text frame
var docRef = documents.add();
var iCount = printerList.length;

var textRef = docRef.textFrames.add();
textRef.contents += "Printers...\r";

for (var i = 0; i < iCount; i++) {
  textRef.contents += printerList[i].name;
  textRef.contents += "\r\t";
}

textRef.top = 600;
textRef.left = 200;

redraw();
```

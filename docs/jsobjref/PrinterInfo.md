# PrinterInfo

`printerInfo`

**Description**

Configuration information about a printer.

---

## Properties

### PrinterInfo.binaryPrintingSupport

`printerInfo.binaryPrintingSupport`

**Description**

If `true`, the printer supports binary printing.

**Type**

Boolean

---

### PrinterInfo.colorSupport

`printerInfo.colorSupport`

**Description**

The printer color capability.

**Type**

[PrinterColorMode](scripting-constants.md#jsobjref-scripting-constants-printercolormode)

---

### PrinterInfo.customPaperSupport

`printerInfo.customPaperSupport`

**Description**

If `true`, the printer supports custom paper size.

**Type**

Boolean

---

### PrinterInfo.customPaperTransverseSupport

`printerInfo.customPaperTransverseSupport`

**Description**

If `true`, the printer supports custom paper transverse.

**Type**

Boolean

---

### PrinterInfo.deviceResolution

`printerInfo.deviceResolution`

**Description**

The printer default resolution.

**Type**

Number (double)

---

### PrinterInfo.inRIPSeparationSupport

`printerInfo.inRIPSeparationSupport`

**Description**

If `true`, the printer supports InRIP color separation.

**Type**

Boolean

---

### PrinterInfo.maxDeviceResolution

`printerInfo.maxDeviceResolution`

**Description**

The printer maximum device resolution.

**Type**

Number (double)

---

### PrinterInfo.maxPaperHeight

`printerInfo.maxPaperHeight`

**Description**

Custom paper’s maximum height.

**Type**

Number (double)

---

### PrinterInfo.maxPaperHeightOffset

`printerInfo.maxPaperHeightOffset`

**Description**

Custom paper’s maximum height offset.

**Type**

Number (double)

---

### PrinterInfo.maxPaperWidth

`printerInfo.maxPaperWidth`

**Description**

Custom paper’s maximum width.

**Type**

Number (double)

---

### PrinterInfo.maxPaperWidthOffset

`printerInfo.maxPaperWidthOffset`

**Description**

Custom paper’s maximum width offset.

**Type**

Number (double)

---

### PrinterInfo.minPaperHeight

`printerInfo.minPaperHeight`

**Description**

Custom paper’s minimum height.

**Type**

Number (double)

---

### PrinterInfo.minPaperHeightOffset

`printerInfo.minPaperHeightOffset`

**Description**

Custom paper’s minimum height offset.

**Type**

Number (double)

---

### PrinterInfo.minPaperWidth

`printerInfo.minPaperWidth`

**Description**

Custom paper’s minimum width.

**Type**

Number (double)

---

### PrinterInfo.minPaperWidthOffset

`printerInfo.minPaperWidthOffset`

**Description**

Custom paper’s minimum width offset.

**Type**

Number (double)

---

### PrinterInfo.paperSizes

`printerInfo.paperSizes`

**Description**

The list of supported paper sizes.

**Type**

Array of [Paper](Paper.md#jsobjref-paper)

---

### PrinterInfo.postScriptLevel

`printerInfo.postScriptLevel`

**Description**

The PostScript Language level.

**Type**

[PrinterPostScriptLevelEnum](scripting-constants.md#jsobjref-scripting-constants-printerpostscriptlevelenum)

---

### PrinterInfo.printerType

`printerInfo.printerType`

**Description**

The printer type.

**Type**

[PrinterTypeEnum](scripting-constants.md#jsobjref-scripting-constants-printertypeenum)

---

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

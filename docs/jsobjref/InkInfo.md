<a id="jsobjref-inkinfo"></a>

# InkInfo

`app.activeDocument.inkList[index].inkInfo`

**Description**

Ink information for printing a document.

---

## Properties

<a id="jsobjref-inkinfo-angle"></a>

### InkInfo.angle

`app.activeDocument.inkList[index].inkInfo.angle`

**Description**

The ink’s screen angle in degrees. Range: -360 to 360.

**Type**

Number (double).

---

<a id="jsobjref-inkinfo-customcolor"></a>

### InkInfo.customColor

`app.activeDocument.inkList[index].inkInfo.customColor`

**Description**

The color of the custom ink.

**Type**

[Color](Color.md#jsobjref-color)

---

<a id="jsobjref-inkinfo-density"></a>

### InkInfo.density

`app.activeDocument.inkList[index].inkInfo.density`

**Description**

The neutral density. Minimum: 0.0.

**Type**

Number (double).

---

<a id="jsobjref-inkinfo-dotshape"></a>

### InkInfo.dotShape

`app.activeDocument.inkList[index].inkInfo.dotShape`

**Description**

The dot shape name.

**Type**

String.

---

<a id="jsobjref-inkinfo-frequency"></a>

### InkInfo.frequency

`app.activeDocument.inkList[index].inkInfo.frequency`

**Description**

The ink’s frequency. Range: 0.0 to 1000.0.

**Type**

Number (double).

---

<a id="jsobjref-inkinfo-kind"></a>

### InkInfo.kind

`app.activeDocument.inkList[index].inkInfo.kind`

**Description**

The ink type.

**Type**

[InkType](scripting-constants.md#jsobjref-scripting-constants-inktype)

---

<a id="jsobjref-inkinfo-printingstatus"></a>

### InkInfo.printingStatus

`app.activeDocument.inkList[index].inkInfo.printingStatus`

**Description**

The ink printing status.

**Type**

[InkPrintStatus](scripting-constants.md#jsobjref-scripting-constants-inkprintstatus)

---

<a id="jsobjref-inkinfo-trapping"></a>

### InkInfo.trapping

`app.activeDocument.inkList[index].inkInfo.trapping`

**Description**

The trapping type.

**Type**

[TrappingType](scripting-constants.md#jsobjref-scripting-constants-trappingtype)

---

<a id="jsobjref-inkinfo-trappingorder"></a>

### InkInfo.trappingOrder

`app.activeDocument.inkList[index].inkInfo.trappingOrder`

**Description**

The order of trapping for the ink. Range: 1 to 4 for CMYK.

**Type**

Number (long).

---

<a id="jsobjref-inkinfo-typename"></a>

### InkInfo.typename

`app.activeDocument.inkList[index].inkInfo.typename`

**Description**

The class name of the object.

**Type**

String, read-only.

---

## Example

### Getting ink information

```default
// Displays the current documents inks in a text frame

var docRef = documents.add();

// assemble a string of the inks in this document
var sInks = "";
var iLength = activeDocument.inkList.length;
for (var i = 0; i < iLength; i++) {
  sInks += docRef.inkList[i].name;
  sInks += "\r\t";
  sInks += "Frequency = " + docRef.inkList[i].inkInfo.frequency;
  sInks += "\r\t";
  sInks += "Density = " + docRef.inkList[i].inkInfo.density;
  sInks += "\r";
}

var textRef = docRef.textFrames.add();
textRef.contents = sInks;
textRef.top = 600;
textRef.left = 200;

redraw();
```

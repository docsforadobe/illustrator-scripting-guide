<a id="jsobjref-screeninfo"></a>

# ScreenInfo

`PPDFileList[index].PPDInfo.screenList[index].screenInfo`

**Description**

Contains information about the angle and frequency of the color separation screen to be used for printing.

---

## Properties

<a id="jsobjref-screeninfo-angle"></a>

### ScreenInfo.angle

`PPDFileList[index].PPDInfo.screenList[index].screenInfo.angle`

**Description**

The screen’s angle in degrees.

**Type**

Number (double).

---

<a id="jsobjref-screeninfo-defaultscreen"></a>

### ScreenInfo.defaultScreen

`PPDFileList[index].PPDInfo.screenList[index].screenInfo.defaultScreen`

**Description**

If true, it is the default screen.

**Type**

Boolean.

---

<a id="jsobjref-screeninfo-frequency"></a>

### ScreenInfo.frequency

`PPDFileList[index].PPDInfo.screenList[index].screenInfo.frequency`

**Description**

The screen’s frequency.

**Type**

Number (double).

---

<a id="jsobjref-screeninfo-typename"></a>

### ScreenInfo.typename

`PPDFileList[index].PPDInfo.screenList[index].screenInfo.typename`

**Description**

The class name of the referenced object.

**Type**

String; read-only.

---

## Example

### Getting screen information

```default
// Displays in a new text frame, the name, angle and frequency
// of each screen list item
var sInfo = "";
var docRef = documents.add();
if (PPDFileList.length == 0) {
  sInfo = "\r\t\tEmpty PPDFileList";
} else {
  var ppdRef = PPDFileList[0];
  var ppdInfoRef = ppdRef.PPDInfo;
  sInfo += "\r\t\tScreen Objects for 1st PPD File:\r";
  sInfo += "\t\t" + ppdRef.name;

  var iScreens = ppdInfoRef.screenList.length;
  if (iScreens > 0) {
    for (var c = 0; c < iScreens; c++) {

      var screenRef = ppdInfoRef.screenList[c];
      sInfo += "\r\t\t";
      sInfo += screenRef.name;

      var screenInfoRef = screenRef.screenInfo;

      sInfo += ", Angle = ";
      sInfo += screenInfoRef.angle;

      sInfo += ", Frequency = ";
      sInfo += screenInfoRef.frequency;
      sInfo += "\r";
    }
  } else {
    sInfo += "\r\t\tEmpty ScreenList";
  }
}

var textRef = docRef.textFrames.add();
textRef.textRange.characterAttributes.size = 12;
textRef.contents = sInfo;
textRef.top = 600;
textRef.left = 30;

redraw();
```

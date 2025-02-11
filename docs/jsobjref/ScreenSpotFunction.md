# ScreenSpotFunction

`PPDFileList[index].PPDInfo.screenSpotFunctionList[index`

**Description**

Contains information about a color separation screen spot function, including its definition in PostScript language code.

---

## Properties

### ScreenSpotFunction.name

`PPDFileList[index].PPDInfo.screenSpotFunctionList[index].name`

**Description**

The color separation screen spot function name.

**Type**

String

---

### ScreenSpotFunction.spotFunction

`PPDFileList[index].PPDInfo.screenSpotFunctionList[index].spotFunction`

**Description**

The spot function expressed in PostScript commands.

**Type**

String

---

### ScreenSpotFunction.typename

`PPDFileList[index].PPDInfo.screenSpotFunctionList[index].typename`

**Description**

The class name of the referenced object.

**Type**

String; read-only.

---

## Example

### Finding screen spot functions

```default
// Displays in a new text frame, the screen spot functions for the 1st PPD file.
var docRef = documents.add();
var sInfo = "";
if (PPDFileList.length == 0) {
  sInfo = "\r\t\tEmpty PPDFileList"
} else {
  var ppdRef = PPDFileList[0];
  var ppdInfoRef = ppdRef.PPDInfo;

  var sInfo = "\r\t\tScreenSpotFunctions for 1st PPD File:\r";
  sInfo += "\t\t" + ppdRef.name + "\r";

  var iScreenSpots = ppdInfoRef.screenSpotFunctionList.length;
  if (iScreenSpots > 0) {
    for (var n = 0; n < iScreenSpots; n++) {
      var screenSpotRef = ppdInfoRef.screenSpotFunctionList[n];
      sInfo += "\t\t";

      sInfo += screenSpotRef.name;
      sInfo += ", spotFunction: ";

      sInfo += screenSpotRef.spotFunction;
      sInfo += "\r";
    }
  } else {
    sInfo += "\t\tEmpty ScreenSpotFunctionList";
  }
}

var textRef = docRef.textFrames.add();
textRef.textRange.characterAttributes.size = 12;
textRef.contents = sInfo;
textRef.top = 600;
textRef.left = 30;

redraw();
```

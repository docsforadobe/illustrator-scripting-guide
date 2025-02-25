# PPDFileInfo

`app.PPDFileList[index].PPDInfo`

#### Description

Information about a PostScript Printer Description (PPD) file.

---

## Properties

### PPDFileInfo.languageLevel

`app.PPDFileList[index].PPDInfo.languageLevel`

#### Description

The PostScript language level.

#### Type

String

---

### PPDFileInfo.PPDFilePath

`app.PPDFileList[index].PPDInfo.PPDFilePath`

#### Description

Path specification for the PPD file.

#### Type

[File](https://extendscript.docsforadobe.dev/file-system-access/file-object/) object

---

### PPDFileInfo.screenList

`app.PPDFileList[index].PPDInfo.screenList`

#### Description

List of color separation screens.

#### Type

Array of [Screen](./Screen.md)

---

### PPDFileInfo.screenSpotFunctionList

`app.PPDFileList[index].PPDInfo.screenSpotFunctionList`

#### Description

List of color separation screen spot functions.

#### Type

Array of [ScreenSpotFunction](./ScreenSpotFunction.md)

---

## Example

### Displaying PPD file properties

```javascript
// Displays postscript level and path for each PPD file found in a new text frame
var sPPD = "";
var docRef = documents.add();

var x = 30;
var y = (docRef.height - 30);

var iLength = PPDFileList.length;
if (iLength > 20)
    iLength = 20;

for (var i = 0; i < iLength; i++) {
    var ppdRef = PPDFileList[i];
    sPPD = ppdRef.name;
    sPPD += "\r\tPS Level ";

    var ppdInfoRef = ppdRef.PPDInfo;
    sPPD += ppdInfoRef.languageLevel;
    sPPD += "\r\tPath: ";
    sPPD += ppdInfoRef.PPDFilePath;

    var textRef = docRef.textFrames.add();
    textRef.textRange.characterAttributes.size = 8;
    textRef.contents = sPPD;
    textRef.top = (y);
    textRef.left = x;

    redraw();

    if ((y -= (textRef.height)) <= 30) {
        y = (docRef.height - 30);
        x += 150;
    }
}
```

---

### PPDFileInfo and related screen information

```javascript
// Displays in a new text frame, the postscript level, file paths, screens, and
// screen spot information for first 10 PPD files found

var sPPD = "";
var docRef = documents.add();

var x = 30;
var y = (docRef.height - 30);

var iLength = PPDFileList.length;

if (iLength > 10)
    iLength = 10;

for (var i = 0; i < iLength; i++) {
    var ppdRef = PPDFileList[i];
    sPPD = ppdRef.name;
    sPPD += "\r\tPS Level ";

    var ppdInfoRef = ppdRef.PPDInfo;
    sPPD += ppdInfoRef.languageLevel;
    sPPD += "\r\tPath: ";
    sPPD += ppdInfoRef.PPDFilePath;
    sPPD += "\r\tScreens:\r";

    var iScreens = ppdInfoRef.screenList.length;
    for (var c = 0; c < iScreens; c++) {

        var screenRef = ppdInfoRef.screenList[c];
        sPPD += "\t\t";
        sPPD += screenRef.name;

        var screenInfoRef = screenRef.screenInfo;
        sPPD += ", Angle = ";
        sPPD += screenInfoRef.angle;
        sPPD += ", Frequency = ";
        sPPD += screenInfoRef.frequency;
        sPPD += "\r";
    }

    sPPD += "\r\tScreenSpots:\r";

    var iScreenSpots = ppdInfoRef.screenSpotFunctionList.length;
    for (var n = 0; n < iScreenSpots; n++) {
        var screenSpotRef = ppdInfoRef.screenSpotFunctionList[n];
        sPPD += "\t\t";
        sPPD += screenSpotRef.name;
        sPPD += ", spotFunction: ";
        sPPD += screenSpotRef.spotFunction;
        sPPD += "\r";
    }

    var textRef = docRef.textFrames.add();
    textRef.textRange.characterAttributes.size = 8;
    textRef.contents = sPPD;
    textRef.top = (y);
    textRef.left = x;

    redraw();

    y -= (textRef.height);
}
```

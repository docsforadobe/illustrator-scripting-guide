<a id="jsobjref-printfontoptions"></a>

# PrintFontOptions

`new PrintFontOptions()`

**Description**

Contains information about font downloading and substitution for the fonts used for printing the document.

---

## Properties

<a id="jsobjref-printfontoptions-downloadfonts"></a>

### PrintFontOptions.downloadFonts

`printFontOptions.downloadFonts`

**Description**

The font download mode.

Default: `PrintFontDownloadMode.DOWNLOADSUBSET`

**Type**

[PrintFontDownloadMode](scripting-constants.md#jsobjref-scripting-constants-printfontdownloadmode)

---

<a id="jsobjref-printfontoptions-fontsubstitution"></a>

### PrintFontOptions.fontSubstitution

`printFontOptions.fontSubstitution`

**Description**

The font substitution policy.

Default: `FontSubstitutionPolicy.SUBSTITUTEOBLIQUE`

**Type**

[FontSubstitutionPolicy](scripting-constants.md#jsobjref-scripting-constants-fontsubstitutionpolicy)

---

<a id="jsobjref-printfontoptions-typename"></a>

### PrintFontOptions.typename

`printFontOptions.typename`

**Description**

The class name of the object.

**Type**

String, read-only.

---

## Example

### Printing with font options

```default
// Creates a new document, adds text then prints with specified font options.
var docRef = documents.add();

var pathRef = docRef.pathItems.rectangle(500, 300, 400, 400);
var textRef = docRef.textFrames.areaText(pathRef);
textRef.contents = "Text example";

//Create PrintFontOptions object and assign to a PrintOptions object
var fontOpts = new PrintFontOptions();
var printOpts = new PrintOptions();
printOpts.fontOptions = fontOpts;

// Set some font options
fontOpts.downloadFonts = PrintFontDownloadMode.DOWNLOADNONE;
fontOpts.fontSubstitution = FontSubstitutionPolicy.SUBSTITUTEDEVICE;

// print it
activeDocument.print(printOpts);
```

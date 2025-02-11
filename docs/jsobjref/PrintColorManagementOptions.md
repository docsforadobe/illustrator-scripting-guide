# PrintColorManagementOptions

`new PrintColorManagementOptions()`

**Description**

Information used for color management of the document.

---

## Properties

### PrintColorManagementOptions.colorProfileMode

`printColorManagementOptions.colorProfileMode`

**Description**

The color management profile mode. Default: `PrintColorProfile.SOURCEPROFILE`

**Type**

[PrintColorProfile](scripting-constants.md#jsobjref-scripting-constants-printcolorprofile)

---

### PrintColorManagementOptions.intent

`printColorManagementOptions.intent`

**Description**

The color management intent type. Default: `PrintColorIntent.RELATIVECOLORIMETRIC`

**Type**

[PrintColorIntent](scripting-constants.md#jsobjref-scripting-constants-printcolorintent)

---

### PrintColorManagementOptions.name

`printColorManagementOptions.name`

**Description**

The color management profile name.

**Type**

String

---

### PrintColorManagementOptions.typename

`printColorManagementOptions.typename`

**Description**

The class name of the object.

**Type**

String; read-only.

---

## Example

### Managing colors for printing

```default
// Creates a new document, adds symbols, then creates a
// PrintColorManagementOptions object and assigns it
// to a PrintOptions object, then prints with each color intent

// Add some symbol items to a new document
var docRef = documents.add();
var y = docRef.height - 30;

for (var i = 0; i < (docRef.symbols.length); i++) {
  symbolRef = docRef.symbols[i];

  symbolItemRef1 = docRef.symbolItems.add(symbolRef);
  symbolItemRef1.top = y;
  symbolItemRef1.left = 100;

  y -= (symbolItemRef1.height + 10);
}

redraw();

var colorOptions = new PrintColorManagementOptions();
var options = new PrintOptions();
options.colorManagementOptions = colorOptions;
colorOptions.name = "ColorMatch RGB";

// Print the current document once for each color intent.
colorOptions.intent = PrintColorIntent.ABSOLUTECOLORIMETRIC;
docRef.print(options);

colorOptions.intent = PrintColorIntent.PERCEPTUALINTENT;
docRef.print(options);

colorOptions.intent = PrintColorIntent.RELATIVECOLORIMETRIC;
docRef.print(options);

colorOptions.intent = PrintColorIntent.SATURATIONINTENT;
docRef.print(options);
```

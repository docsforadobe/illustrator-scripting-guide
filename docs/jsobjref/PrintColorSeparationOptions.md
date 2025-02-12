# PrintColorSeparationOptions

`new PrintColorSeparationOptions()`

#### Description

Information about the color separations to be used in printing the document.

---

## Properties

### PrintColorSeparationOptions.colorSeparationMode

`printColorSeparationOptions.colorSeparationMode`

#### Description

The color separation type.

Default: `PrintColorSeparationMode.COMPOSITE`

#### Type

[PrintColorSeparationMode](scripting-constants.md#printcolorseparationmode)

---

### PrintColorSeparationOptions.convertSpotColors

`printColorSeparationOptions.convertSpotColors`

#### Description

If `true`, all spot colors should be converted to process colors.

Default: `false`

#### Type

Boolean

---

### PrintColorSeparationOptions.inkList

`printColorSeparationOptions.inkList`

#### Description

The list of inks for color separation.

#### Type

Array of [Ink](./Ink.md)

---

### PrintColorSeparationOptions.overPrintBlack

`printColorSeparationOptions.overPrintBlack`

#### Description

If `true`, overprint in black.

Default: `false`

#### Type

Boolean

---

### PrintColorSeparationOptions.typename

`printColorSeparationOptions.typename`

#### Description

Read-only. The class name of the object.

#### Type

String

---

## Example

### Managing color separations for printing

```javascript
// Creates a new document with symbol items
// and prints document with each separation option

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

// Print with various separation options
var sepOptions = new PrintColorSeparationOptions();
var options = new PrintOptions();
options.colorSeparationOptions = sepOptions;

sepOptions.convertSpotColors = true;
sepOptions.overPrintBlack = true;
sepOptions.colorSeparationMode = PrintColorSeparationMode.COMPOSITE;
docRef.print(options);

sepOptions.colorSeparationMode = PrintColorSeparationMode.INRIPSEPARATION;
docRef.print(options);

sepOptions.convertSpotColors = false;
sepOptions.overPrintBlack = false;
sepOptions.colorSeparationMode = PrintColorSeparationMode.HOSTBASEDSEPARATION;
docRef.print(options);
```

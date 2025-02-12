# CMYKColor

`new cmykColor()`

#### Description

A CMYK color specification, used where a [Color](./Color.md) object is required.

If the color space of a document is `RGB` and you specify the color value for a page item in that document using CMYK, Illustrator will translate the CMYK color specification into an RGB color specification. The same thing happens if the document's color space is CMYK and you specify colors using RGB.

Since this translation can lose information, you should specify colors using the class that matches the document's actual color space.

---

## Properties

### CMYKColor.black

`cmykColor.black`

#### Description

The black color value. Range 0.0-100.0.

Default: 0.0

#### Type

Number (double)

---

### CMYKColor.cyan

`cmykColor.cyan`

#### Description

The cyan color value. Range 0.0-100.0.

Default: 0.0

#### Type

Number (double)

---

### CMYKColor.magenta

`cmykColor.magenta`

#### Description

The magenta color value. Range 0.0-100.0.

Default: 0.0

#### Type

Number (double)

---

### CMYKColor.typename

`cmykColor.typename`

#### Description

The class name of the referenced object.

#### Type

String; read-only.

---

### CMYKColor.yellow

`cmykColor.yellow`

#### Description

The yellow color value. Range 0.0-100.0.

Default: 0.0

#### Type

Number (double)

---

## Example

### Setting a CMYK color

```javascript
// Sets the fill color of the frontmost path item in
// the current document to a light purple CMYK color

if (app.documents.length > 0 && app.activeDocument.pathItems.length > 0) {
    var frontPath = app.activeDocument.pathItems[0];

    // Set color values for the CMYK object
    var newCMYKColor = new cmykColor();
    newCMYKColor.black = 0;
    newCMYKColor.cyan = 30.4;
    newCMYKColor.magenta = 32;
    newCMYKColor.yellow = 0;

    // Use the color object in the path item
    frontPath.filled = true;
    frontPath.fillColor = newCMYKColor;
}
```

<a id="jsobjref-rgbcolor"></a>

# RGBColor

`new RGBColor()`

**Description**

An RGB color specification, used to apply an RGB color to a layer or art item.

If the color space of a document is RGB and you specify the color value for a page item in that document using CMYK, Illustrator will translate the CMYK color specification into an RGB color specification. The same thing happens if the document’s color space is CMYK and you specify colors using RGB. Since this translation can lose information, you should specify colors using the class that matches the document’s actual color space.

---

## Properties

<a id="jsobjref-rgbcolor-blue"></a>

### RGBColor.blue

`rgbColor.blue`

**Description**

The blue color value. Range: 0.0 to 255.0.

**Type**

Number (double).

---

<a id="jsobjref-rgbcolor-green"></a>

### RGBColor.green

`rgbColor.green`

**Description**

The green color value. Range: 0.0 to 255.0.

**Type**

Number (double).

---

<a id="jsobjref-rgbcolor-red"></a>

### RGBColor.red

`rgbColor.red`

**Description**

The red color value. Range: 0.0 to 255.0.

**Type**

Number (double).

---

<a id="jsobjref-rgbcolor-typename"></a>

### RGBColor.typename

`rgbColor.typename`

**Description**

The class name of the referenced object.

**Type**

String, read-only.

---

## Example

### Setting an RGB color

```default
// Sets the default fill color in the current document to yellow.

if (app.documents.length > 0) {
  // Define the new color
  var newRGBColor = new RGBColor();
  newRGBColor.red = 255;
  newRGBColor.green = 255;
  newRGBColor.blue = 0;

  app.activeDocument.defaultFillColor = newRGBColor;
}
```

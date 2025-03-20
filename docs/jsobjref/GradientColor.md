# GradientColor

`gradientColor`

#### Description

A gradient color specification in a Gradient object. A script can create a new gradient color using a reference to an existing gradient in the document. If no existing gradient object is referenced, a default gradient is supplied.

---

## Properties

### GradientColor.angle

`gradientColor.angle`

#### Description

The gradient vector angle in degrees.

Default: 0.0.

!!! warning
    Setting the angle does not work. Apparently this is a [bug since 2008](https://community.adobe.com/t5/illustrator-discussions/unable-to-change-angle-of-gradient/m-p/11759125) that still exists in (at least) 29.3.1.

#### Type

Number (double).

---

### GradientColor.gradient

`gradientColor.gradient`

#### Description

Reference to the object defining the gradient.

#### Type

[Gradient](./Gradient.md)

---

### GradientColor.hiliteAngle

`gradientColor.hiliteAngle`

#### Description

The gradient highlight vector angle in degrees.

#### Type

Number (double).

---

### GradientColor.hiliteLength

`gradientColor.hiliteLength`

#### Description

The gradient highlight vector length.

#### Type

Number (double).

---

### GradientColor.length

`gradientColor.length`

#### Description

The gradient vector length.

#### Type

Number (double).

---

### GradientColor.matrix

`gradientColor.matrix`

#### Description

An additional transformation matrix to manipulate the gradient path.

#### Type

Matrix.

---

### GradientColor.origin

`gradientColor.origin`

#### Description

The gradient vector origin, the center point of the gradient in this color.

#### Type

Array of 2 numbers.

---

### GradientColor.typename

`gradientColor.typename`

#### Description

The class name of the referenced object.

#### Type

String; read-only.

---

## Example

### Changing a gradient stop color

```javascript
// Creates a new RGB document, then changes the color of the first gradient stop of an indexed gradient
app.documents.add(DocumentColorSpace.RGB);

// Get a reference to the gradient that you want to change
var gradientRef = app.activeDocument.gradients[1];

// Create the new color
var startColor = new RGBColor();
startColor.red = 255;
startColor.green = 238;
startColor.blue = 98;

// apply new color to the first gradient stop
gradientRef.gradientStops[0].color = startColor;
```

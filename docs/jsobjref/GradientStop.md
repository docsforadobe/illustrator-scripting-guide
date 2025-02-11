# GradientStop

`app.activeDocument.gradients[index].gradientStops[index`

**Description**

A gradient stop definition that represents a point on a specific gradient defined in the document. Each gradient stop specifies a color change in the containing gradient. See [Changing a gradient stop color](GradientColor.md#jsobjref-gradientcolor-changinggradientstopcolor) for an example.

---

## Properties

### GradientStop.color

`app.activeDocument.gradients[index].gradientStops[index].color`

**Description**

The color linked to this gradient stop.

**Type**

[Color](Color.md#jsobjref-color)

---

### GradientStop.midPoint

`app.activeDocument.gradients[index].gradientStops[index].midPoint`

**Description**

The midpoint key value, specified as a percentage from 13.0 to 87.0.

**Type**

Number (double).

---

### GradientStop.opacity

`app.activeDocument.gradients[index].gradientStops[index].opacity`

**Description**

The opacity value for the gradient stop. Range: 0.0 to 100.0

**Type**

Number (double).

---

### GradientStop.parent

`app.activeDocument.gradients[index].gradientStops[index].parent`

**Description**

The gradient that contains this gradient stop.

**Type**

[Gradient](Gradient.md#jsobjref-gradient), read-only.

---

### GradientStop.rampPoint

`app.activeDocument.gradients[index].gradientStops[index].rampPoint`

**Description**

The location of the color in the blend in a range from 0.0 to 100.0, where 100.0 is 100%.

**Type**

Number (double).

---

### GradientStop.typename

`app.activeDocument.gradients[index].gradientStops[index].typename`

**Description**

The class name of the referenced object.

**Type**

String, read-only.

---

## Methods

### GradientStop.remove()

`app.activeDocument.gradients[index].gradientStops[index].remove()`

**Description**

Deletes this object.

**Returns**

Nothing.

<a id="jsobjref-gradientstop"></a>

# GradientStop

`app.activeDocument.gradients[index].gradientStops[index`

**Description**

A gradient stop definition that represents a point on a specific gradient defined in the document. Each gradient stop specifies a color change in the containing gradient. See [Changing a gradient stop color](GradientColor.md#jsobjref-gradientcolor-changinggradientstopcolor) for an example.

---

## Properties

<a id="jsobjref-gradientstop-color"></a>

### GradientStop.color

`app.activeDocument.gradients[index].gradientStops[index].color`

**Description**

The color linked to this gradient stop.

**Type**

[Color](Color.md#jsobjref-color)

---

<a id="jsobjref-gradientstop-midpoint"></a>

### GradientStop.midPoint

`app.activeDocument.gradients[index].gradientStops[index].midPoint`

**Description**

The midpoint key value, specified as a percentage from 13.0 to 87.0.

**Type**

Number (double).

---

<a id="jsobjref-gradientstop-opacity"></a>

### GradientStop.opacity

`app.activeDocument.gradients[index].gradientStops[index].opacity`

**Description**

The opacity value for the gradient stop. Range: 0.0 to 100.0

**Type**

Number (double).

---

<a id="jsobjref-gradientstop-parent"></a>

### GradientStop.parent

`app.activeDocument.gradients[index].gradientStops[index].parent`

**Description**

The gradient that contains this gradient stop.

**Type**

[Gradient](Gradient.md#jsobjref-gradient), read-only.

---

<a id="jsobjref-gradientstop-ramppoint"></a>

### GradientStop.rampPoint

`app.activeDocument.gradients[index].gradientStops[index].rampPoint`

**Description**

The location of the color in the blend in a range from 0.0 to 100.0, where 100.0 is 100%.

**Type**

Number (double).

---

<a id="jsobjref-gradientstop-typename"></a>

### GradientStop.typename

`app.activeDocument.gradients[index].gradientStops[index].typename`

**Description**

The class name of the referenced object.

**Type**

String, read-only.

---

## Methods

<a id="jsobjref-gradientstop-remove"></a>

### GradientStop.remove()

`app.activeDocument.gradients[index].gradientStops[index].remove()`

**Description**

Deletes this object.

**Returns**

Nothing.

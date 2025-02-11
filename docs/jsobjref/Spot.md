<a id="jsobjref-spot"></a>

# Spot

`app.activeDocument.spots[index`

**Description**

A custom color definition contained in a [SpotColor](SpotColor.md#jsobjref-spotcolor) object.

If no properties are specified when creating a spot, default values are provided.

However, if specifying the color, you must use the same color space as the document, either CMYK or RGB. Otherwise, an error results.

The new spot is added to the end of the swatches list in the Swatches palette.

---

## Properties

<a id="jsobjref-spot-color"></a>

### Spot.color

`app.activeDocument.spots[index].color`

**Description**

The color information for this spot color.

**Type**

[Color](Color.md#jsobjref-color)

---

<a id="jsobjref-spot-colortype"></a>

### Spot.colorType

`app.activeDocument.spots[index].colorType`

**Description**

The color model for this custom color.

**Type**

[ColorModel](scripting-constants.md#jsobjref-scripting-constants-colormodel)

---

<a id="jsobjref-spot-name"></a>

### Spot.name

`app.activeDocument.spots[index].name`

**Description**

The spot color’s name.

**Type**

String

---

<a id="jsobjref-spot-parent"></a>

### Spot.parent

`app.activeDocument.spots[index].parent`

**Description**

The document that contains this spot color.

**Type**

[Document](Document.md#jsobjref-document); read-only.

---

<a id="jsobjref-spot-spotkind"></a>

### Spot.spotKind

`app.activeDocument.spots[index].spotKind`

**Description**

The kind of spot color (RGB, CMYK or LAB). This is the name of the color kind contained in the spot object.

**Type**

[SpotColorKind](scripting-constants.md#jsobjref-scripting-constants-spotcolorkind); read-only.

---

<a id="jsobjref-spot-typename"></a>

### Spot.typename

`app.activeDocument.spots[index].typename`

**Description**

The class name of the referenced object.

**Type**

String; read-only.

---

## Methods

<a id="jsobjref-spot-getinternalcolor"></a>

### Spot.getInternalColor()

`app.activeDocument.spots[index].getInternalColor()`

**Description**

Gets the internal color of a spot.

**Returns**

Color components.

---

<a id="jsobjref-spot-remove"></a>

### Spot.remove()

`app.activeDocument.spots[index].remove()`

**Description**

Deletes this object.

**Returns**

Nothing.

---

## Example

### Creating a new spot color

```default
// Creates a new spot color in the current document, then applies an 80% tint to the color
if ( app.documents.length > 0 ) {
  var doc = app.activeDocument;

  // Create the new spot
  var newSpot = doc.spots.add();

  // Define the new color value
  var newColor = new CMYKColor();
  newColor.cyan = 35;
  newColor.magenta = 0;
  newColor.yellow = 50;
  newColor.black = 0;

  // Define a new SpotColor with an 80% tint
  // of the new Spot's color. The spot color can then
  // be applied to an art item like any other color.
  newSpot.name = "Pea-Green";
  newSpot.colorType = ColorModel.SPOT;
  newSpot.color = newColor;

  var newSpotColor = new SpotColor();
  newSpotColor.spot = newSpot;
  newSpotColor.tint = 80;
}
```

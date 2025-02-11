# Spots

`app.activeDocument.spots`

**Description**

A collection of [SpotColor](./SpotColor.md) objects in a document.

---

## Properties

### Spots.length

`app.activeDocument.spots.length`

**Description**

Number of elements in the collection.

**Type**

Number, read-only.

---

### Spots.parent

`app.activeDocument.spots.parent`

**Description**

The object's container.

**Type**

Object, read-only.

---

### Spots.typename

`app.activeDocument.spots.typename`

**Description**

The class name of the object.

**Type**

String, read-only.

---

## Methods

### Spots.add()

`app.activeDocument.spots.add()`

**Description**

Creates a new object.

**Returns**

[Spot](./Spot.md)

---

### Spots.getByName()

`app.activeDocument.spots.getByName(name)`

**Description**

Get the first element in the collection with the provided name.

**Parameters**

| Parameter   | Type   | Description            |
|-------------|--------|------------------------|
| `name`      | String | Name of element to get |

**Returns**

[Spot](./Spot.md)

---

### Spots.index()

`app.activeDocument.spots.index(itemKey)`

**Description**

Gets an element from the collection.

**Parameters**

| Parameter   | Type           | Description           |
|-------------|----------------|-----------------------|
| `itemKey`   | String, Number | Key of element to get |

**Returns**

[Spot](./Spot.md)

---

### Spots.removeAll()

`app.activeDocument.spots.removeAll()`

**Description**

Deletes all elements in the collection.

**Returns**

Nothing.

---

## Example

### Removing spot colors

```default
// Deletes all spots colors from the current document
if ( app.documents.length > 0 ) {
    var spotCount = app.activeDocument.spots.length;

    if (spotCount > 0) {
        app.activeDocument.spots.removeAll();
    }
}
```

---

### Creating and applying spot colors

```default
// Defines and applies a new spot color in the current document,
// then applies the color to the first path item
if (app.documents.length > 0 && app.activeDocument.pathItems.length > 0) {
    // Define the new color value
    var newRGBColor = new RGBColor();
    newRGBColor.red = 255;
    newRGBColor.green = 0;
    newRGBColor.blue = 0;

    // Create the new spot
    var newSpot = app.activeDocument.spots.add();

    // Define the new SpotColor as 80% of the RGB color
    newSpot.name = "Scripted Red spot";
    newSpot.tint = 80;
    newSpot.color = newRGBColor;

    // Apply a 50% tint of the new spot color to the frontmost path item.
    // Create a spotcolor object, set the tint value,
    var newSpotColor = new SpotColor();
    newSpotColor.spot = newSpot;
    newSpotColor.tint = 50;

    // Use the spot color to set the fill color
    var frontPath = app.activeDocument.pathItems[0];
    frontPath.filled = true;
    frontPath.fillColor = newSpotColor;
}
```

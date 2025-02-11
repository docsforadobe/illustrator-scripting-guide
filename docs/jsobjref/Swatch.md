<a id="jsobjref-swatch"></a>

# Swatch

`app.activeDocument.swatches[index`

**Description**

A color swatch definition contained in a document. The swatches correspond to the swatch palette in the Illustrator user interface.

A script can create a new swatch.

The swatch can hold all types of color data, such as pattern, gradient, CMYK, RGB, gray, and spot.

---

## Properties

<a id="jsobjref-swatch-color"></a>

### Swatch.color

`app.activeDocument.swatches[index].color`

**Description**

The color information for this swatch.

**Type**

[Color](Color.md#jsobjref-color)

---

<a id="jsobjref-swatch-name"></a>

### Swatch.name

`app.activeDocument.swatches[index].name`

**Description**

The swatch’s name.

**Type**

String.

---

<a id="jsobjref-swatch-parent"></a>

### Swatch.parent

`app.activeDocument.swatches[index].parent`

**Description**

The object that contains this swatch.

**Type**

[Document](Document.md#jsobjref-document), read-only.

---

<a id="jsobjref-swatch-typename"></a>

### Swatch.typename

`app.activeDocument.swatches[index].typename`

**Description**

The class name of the object.

**Type**

String, read-only.

---

## Methods

<a id="jsobjref-swatch-remove"></a>

### Swatch.remove()

`app.activeDocument.swatches[index].remove()`

**Description**

Deletes this object.

**Returns**

Nothing.

---

## Example

### Modifying a swatch

```default
// Changes the name of the last swatch
if ( app.documents.length > 0 && app.activeDocument.swatches.length > 0 ) {
  var lastIndex = app.activeDocument.swatches.length - 1;
  var lastSwatch = app.activeDocument.swatches[lastIndex];
  lastSwatch.name = "TheLastSwatch";
}
```

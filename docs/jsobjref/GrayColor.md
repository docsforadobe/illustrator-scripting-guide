# GrayColor

`new GrayColor()`

#### Description

A grayscale color specification, used where a `color` object is required.

---

## Properties

### GrayColor.gray

`grayColor.gray`

#### Description

The tint of the gray. Range: 0.0 to 100.0, where 0.0 is black and 100.0 is white.

#### Type

Number (double).

---

### GrayColor.typename

`grayColor.typename`

#### Description

The class name of the referenced object.

#### Type

String, read-only.

---

## Example

### Changing a color to gray

```javascript
// Sets the color of the first word in the active document to a shade of gray

if (app.documents.length > 0 && app.activeDocument.textFrames.length > 0) {
    var text = app.activeDocument.textFrames[0].textRange;
    var firstWord = text.words[0];

    // Create the new color
    var textColor = new GrayColor();
    textColor.gray = 45;

    firstWord.filled = true;
    firstWord.fillColor = textColor;
}
```

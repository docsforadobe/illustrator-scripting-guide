<a id="jsobjref-textfont"></a>

# TextFont

`app.textFonts[index`

**Description**

Information about a font in the document, found in a [CharacterAttributes](CharacterAttributes.md#jsobjref-characterattributes) object.

---

## Properties

<a id="jsobjref-textfont-family"></a>

### TextFont.family

`app.textFonts[index].family`

**Description**

The font’s family name.

**Type**

String, read-only.

---

<a id="jsobjref-textfont-name"></a>

### TextFont.name

`app.textFonts[index].name`

**Description**

The font’s full name.

**Type**

String, read-only.

---

<a id="jsobjref-textfont-parent"></a>

### TextFont.parent

`app.textFonts[index].parent`

**Description**

The object’s container.

**Type**

Object, read-only.

---

<a id="jsobjref-textfont-style"></a>

### TextFont.style

`app.textFonts[index].style`

**Description**

The font’s style name.

**Type**

String, read-only.

---

<a id="jsobjref-textfont-typename"></a>

### TextFont.typename

`app.textFonts[index].typename`

**Description**

The class name of the object.

**Type**

String, read-only.

---

## Example

### Setting the font of text

```default
// Sets the font of all the text in the document to the first font
if ( app.documents.length > 0 ) {

// Iterate through all text art and apply font 0
  for ( i = 0; i< app.activeDocument.textFrames.length; i++) {
    textArtRange = app.activeDocument.textFrames[i].textRange;
    textArtRange.characterAttributes.textFont = app.textFonts[0];
  }
}
```

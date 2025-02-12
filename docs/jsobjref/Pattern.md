# Pattern

`app.activeDocument.patterns[index`

#### Description

An Illustrator pattern definition contained in a document.

Patterns are shown in the Swatches palette.

Each pattern is referenced by a [PatternColor](./PatternColor.md) object, which defines the pattern's appearance.

---

## Properties

### Pattern.name

`app.activeDocument.patterns[index].name`

#### Description

The pattern name.

#### Type

String

---

### Pattern.parent

`app.activeDocument.patterns[index].parent`

#### Description

The document that contains this pattern.

#### Type

[Document](./Document.md); read-only.

---

### Pattern.typename

`app.activeDocument.patterns[index].typename`

#### Description

The class name of the object.

#### Type

String; read-only.

---

## Methods

### Pattern.remove()

`app.activeDocument.patterns[index].remove()`

#### Description

Removes the referenced pattern from the document.

#### Returns

Nothing.

---

### Pattern.toString()

`app.activeDocument.patterns[index].toString()`

#### Description

Returns the object type of a referenced object. If the object has a name, also returns the name.

#### Returns

String

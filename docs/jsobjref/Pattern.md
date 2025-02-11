<a id="jsobjref-pattern"></a>

# Pattern

`app.activeDocument.patterns[index`

**Description**

An Illustrator pattern definition contained in a document.

Patterns are shown in the Swatches palette.

Each pattern is referenced by a [PatternColor](PatternColor.md#jsobjref-patterncolor) object, which defines the pattern’s appearance.

---

## Properties

<a id="jsobjref-pattern-name"></a>

### Pattern.name

`app.activeDocument.patterns[index].name`

**Description**

The pattern name.

**Type**

String

---

<a id="jsobjref-pattern-parent"></a>

### Pattern.parent

`app.activeDocument.patterns[index].parent`

**Description**

The document that contains this pattern.

**Type**

[Document](Document.md#jsobjref-document), read-only.

---

<a id="jsobjref-pattern-typename"></a>

### Pattern.typename

`app.activeDocument.patterns[index].typename`

**Description**

The class name of the object.

**Type**

String, read-only.

---

## Methods

<a id="jsobjref-pattern-remove"></a>

### Pattern.remove()

`app.activeDocument.patterns[index].remove()`

**Description**

Removes the referenced pattern from the document.

**Returns**

Nothing.

---

<a id="jsobjref-pattern-tostring"></a>

### Pattern.toString()

`app.activeDocument.patterns[index].toString()`

**Description**

Returns the object type of a referenced object. If the object has a name, also returns the name.

**Returns**

String

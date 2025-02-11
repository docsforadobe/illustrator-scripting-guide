<a id="jsobjref-symbol"></a>

# Symbol

`app.activeDocument.symbols[index`

**Description**

An art item that is stored in the Symbols palette, and can be reused one or more times in the document without duplicating the art data. Symbols are contained in documents.

Instances of `Symbol` in a document are associated with [SymbolItem](SymbolItem.md#jsobjref-symbolitem) objects, which store the art object properties.

---

## Properties

<a id="jsobjref-symbol-name"></a>

### Symbol.name

`app.activeDocument.symbols[index].name`

**Description**

The symbol’s name

**Type**

String.

---

<a id="jsobjref-symbol-parent"></a>

### Symbol.parent

`app.activeDocument.symbols[index].parent`

**Description**

The object that contains the symbol object.

**Type**

Object, read-only.

---

<a id="jsobjref-symbol-typename"></a>

### Symbol.typename

`app.activeDocument.symbols[index].typename`

**Description**

The class name of the object.

**Type**

String, read-only.

---

## Methods

<a id="jsobjref-symbol-duplicate"></a>

### Symbol.duplicate()

`app.activeDocument.symbols[index].duplicate()`

**Description**

Creates a duplicate of this object.

**Returns**

[Symbol](#jsobjref-symbol)

---

<a id="jsobjref-symbol-remove"></a>

### Symbol.remove()

`app.activeDocument.symbols[index].remove()`

**Description**

Deletes this object.

**Returns**

Nothing.

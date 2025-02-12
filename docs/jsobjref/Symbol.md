# Symbol

`app.activeDocument.symbols[index`

#### Description

An art item that is stored in the Symbols palette, and can be reused one or more times in the document without duplicating the art data. Symbols are contained in documents.

Instances of `Symbol` in a document are associated with [SymbolItem](./SymbolItem.md) objects, which store the art object properties.

---

## Properties

### Symbol.name

`app.activeDocument.symbols[index].name`

#### Description

The symbol's name

#### Type

String.

---

### Symbol.parent

`app.activeDocument.symbols[index].parent`

#### Description

The object that contains the symbol object.

#### Type

Object; read-only.

---

### Symbol.typename

`app.activeDocument.symbols[index].typename`

#### Description

The class name of the object.

#### Type

String; read-only.

---

## Methods

### Symbol.duplicate()

`app.activeDocument.symbols[index].duplicate()`

#### Description

Creates a duplicate of this object.

#### Returns

[Symbol](#jsobjref-symbol)

---

### Symbol.remove()

`app.activeDocument.symbols[index].remove()`

#### Description

Deletes this object.

#### Returns

Nothing.

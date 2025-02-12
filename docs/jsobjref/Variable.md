# Variable

`app.activeDocument.variables[index`

#### Description

A document-level variable that can be imported or exported.

A variable is a dynamic object used to create data-driven graphics.

For an example, see [Dataset](./Dataset.md).

Variables are accessed in Illustrator through the Variables palette.

---

## Properties

### Variable.kind

`app.activeDocument.variables[index].kind`

#### Description

The variable's type.

#### Type

[VariableKind](scripting-constants.md#jsobjref-scripting-constants-variablekind)

---

### Variable.name

`app.activeDocument.variables[index].name`

#### Description

The name of the variable.

#### Type

string

---

### Variable.pageItems

`app.activeDocument.variables[index].pageItems`

#### Description

All of the artwork in the variable.

#### Type

[PageItems](./PageItems.md), read-only

---

### Variable.parent

`app.activeDocument.variables[index].parent`

#### Description

Read-only. The object that contains the variable.

#### Type

Object

---

### Variable.typename

`app.activeDocument.variables[index].typename`

#### Description

The class name of the referenced object.

#### Type

String, read-only

---

## Methods

### Variable.remove()

`app.activeDocument.variables[index].remove()`

#### Description

Removes the variable from the collection of variables.

#### Returns

Nothing.

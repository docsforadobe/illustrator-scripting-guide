<a id="jsobjref-variable"></a>

# Variable

`app.activeDocument.variables[index`

**Description**

A document-level variable that can be imported or exported.

A variable is a dynamic object used to create data-driven graphics.

For an example, see [Dataset](Dataset.md#jsobjref-dataset).

Variables are accessed in Illustrator through the Variables palette.

---

## Properties

<a id="jsobjref-variable-kind"></a>

### Variable.kind

`app.activeDocument.variables[index].kind`

**Description**

The variable’s type.

**Type**

[VariableKind](scripting-constants.md#jsobjref-scripting-constants-variablekind)

---

<a id="jsobjref-variable-name"></a>

### Variable.name

`app.activeDocument.variables[index].name`

**Description**

The name of the variable.

**Type**

string

---

<a id="jsobjref-variable-pageitems"></a>

### Variable.pageItems

`app.activeDocument.variables[index].pageItems`

**Description**

All of the artwork in the variable.

**Type**

[PageItems](PageItems.md#jsobjref-pageitems), read-only

---

<a id="jsobjref-variable-parent"></a>

### Variable.parent

`app.activeDocument.variables[index].parent`

**Description**

Read-only. The object that contains the variable.

**Type**

Object

---

<a id="jsobjref-variable-typename"></a>

### Variable.typename

`app.activeDocument.variables[index].typename`

**Description**

The class name of the referenced object.

**Type**

String, read-only

---

## Methods

<a id="jsobjref-variable-remove"></a>

### Variable.remove()

`app.activeDocument.variables[index].remove()`

**Description**

Removes the variable from the collection of variables.

**Returns**

Nothing.

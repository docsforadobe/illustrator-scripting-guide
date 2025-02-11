# ParagraphStyle

`app.activeDocument.paragraphStyles[index`

**Description**

Associates character and paragraph attributes with a style name. The style object can be used to apply those attributes to the text in a TextFrame object. See [Creating and applying a paragraph style](ParagraphStyles.md#jsobjref-paragraphstyles-creatingandapplyingparagraphstyle) example.

---

## Properties

### ParagraphStyle.characterAttributes

`app.activeDocument.paragraphStyles[index.characterAttributes`

**Description**

The character properties for the text range.

**Type**

[CharacterAttributes](./CharacterAttributes.md), read-only.

---

### ParagraphStyle.name

`app.activeDocument.paragraphStyles[index.name`

**Description**

The paragraph style's name.

**Type**

String.

---

### ParagraphStyle.paragraphAttributes

`app.activeDocument.paragraphStyles[index.paragraphAttributes`

**Description**

The paragraph properties for the text range.

**Type**

[CharacterAttributes](./CharacterAttributes.md), read-only.

---

### ParagraphStyle.parent

`app.activeDocument.paragraphStyles[index.parent`

**Description**

The object's container.

**Type**

Object, read-only.

---

### ParagraphStyle.typename

`app.activeDocument.paragraphStyles[index.typename`

**Description**

The class name of the object.

**Type**

String, read-only.

---

## Methods

### ParagraphStyle.applyTo()

`app.activeDocument.paragraphStyles[index.applyTo(textItem [,clearingOverrides])`

**Description**

Applies this paragraph style to the specified text item.

**Parameters**

| Parameter           | Type              | Description                      |
|---------------------|-------------------|----------------------------------|
| `textItem`          | Object            | Paragraph item to apply style to |
| `clearingOverrides` | Boolean, optional | Whether to clear overrides       |

**Returns**

Nothing.

---

### ParagraphStyle.remove()

`app.activeDocument.paragraphStyles[index.remove()`

**Description**

Deletes the object.

**Returns**

Nothing.

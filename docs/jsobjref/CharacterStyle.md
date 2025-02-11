# CharacterStyle

`characterStyle`

**Description**

Associates character attributes with characters. For an example, see [CharacterStyles](CharacterStyles.md#jsobjref-characterstyles).

---

## Properties

### CharacterStyle.characterAttributes

`characterStyle.characterAttributes`

**Description**

The character properties for the style.

**Type**

[CharacterAttributes](CharacterAttributes.md#jsobjref-characterattributes), read-only.

---

### CharacterStyle.name

`characterStyle.name`

**Description**

The character style’s name.

**Type**

String

---

### CharacterStyle.parent

`characterStyle.parent`

**Description**

The object’s container.

**Type**

Object, read-only.

---

### CharacterStyle.typename

`characterStyle.typename`

**Description**

The class name of the object.

**Type**

String, read-only.

---

## Methods

### CharacterStyle.applyTo()

`characterStyle.applyTo(textItem [,clearingOverrides])`

**Description**

Applies the character style to the text object or objects.

**Paramaters**

| Parameter           | Type              | Description                 |
|---------------------|-------------------|-----------------------------|
| `textItem`          | Object            | Text item to apply style to |
| `clearingOverrides` | Boolean, optional | Whether to clear overrides  |

**Returns**

Nothing

---

### CharacterStyle.remove()

`characterStyle.remove()`

**Description**

Deletes the object.

**Returns**

Nothing.

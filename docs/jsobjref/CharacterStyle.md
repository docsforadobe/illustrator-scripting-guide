<a id="jsobjref-characterstyle"></a>

# CharacterStyle

`characterStyle`

**Description**

Associates character attributes with characters. For an example, see [CharacterStyles](CharacterStyles.md#jsobjref-characterstyles).

---

## Properties

<a id="jsobjref-characterstyle-characterattributes"></a>

### CharacterStyle.characterAttributes

`characterStyle.characterAttributes`

**Description**

The character properties for the style.

**Type**

[CharacterAttributes](CharacterAttributes.md#jsobjref-characterattributes), read-only.

---

<a id="jsobjref-characterstyle-name"></a>

### CharacterStyle.name

`characterStyle.name`

**Description**

The character style’s name.

**Type**

String

---

<a id="jsobjref-characterstyle-parent"></a>

### CharacterStyle.parent

`characterStyle.parent`

**Description**

The object’s container.

**Type**

Object, read-only.

---

<a id="jsobjref-characterstyle-typename"></a>

### CharacterStyle.typename

`characterStyle.typename`

**Description**

The class name of the object.

**Type**

String, read-only.

---

## Methods

<a id="jsobjref-characterstyle-applyto"></a>

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

<a id="jsobjref-characterstyle-remove"></a>

### CharacterStyle.remove()

`characterStyle.remove()`

**Description**

Deletes the object.

**Returns**

Nothing.

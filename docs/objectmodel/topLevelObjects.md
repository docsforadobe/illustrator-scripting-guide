# Top-Level (containing) Objects

Use these objects to access global information about the Illustrator application or an individual document.

---

## Application

The properties of the `application` object give your script access to global values, such as:

- User `preferences`, which a user sets interactively in the Illustrator application by using the Preferences dialog (Edit > Preferences).
- System information like installed fonts (the `text fonts` property) and printers (the `printer list` property).

Also, there are properties that provide application-specific information and higher-level information about any open documents:

- Application information like the installation `path`, `version`, and whether Illustrator is `visible`.
- The `current active` document; that is, the art canvas that is displayed and accepting user input.
- All open `documents`.

The `application` object's methods or commands allow your script to perform application-wide actions; for example:

- `Open` files
- `Undo` and `redo` transactions
- `Quit` Illustrator

---

## Document

The `document` object, which your scripts can create or access through the `application` object, represents an art canvas or loaded Illustrator file.

The `document` object's properties give you access to the document's content; for example:

- The current `selection`, or art objects that the user selected in the document
- All contained art objects, called `page items`, that make up the artwork tree
- Art objects of particular types, like `symbols` and `text frames`
- All `layers` and the currently `active layer`

Document properties also tell you about the state of the document itself; for example:

- User settings for the document, such as `ruler units`
- Whether the document was `saved` since the last alteration of content
- The `path` of the associated file

The document object's methods allow your scripts to act on the document; for example:

- `Save` to an Illustrator file or `save as` the various supported file formats
- `Activate` or `close` a document
- `Print` the document. Your scripts can select a printer by referencing a `print options` object, or they can reference available printers through the application object's `printer list` property.

---

## Layer

The `layer` object provides access to the contents, or artwork tree, of a specific layer.

You access the `layer` object through the `document` object.

The `layer` object properties provide access to, or information about, the layer, such as:

- Whether the layer is `visible` or `locked`.
- The layer's `opacity` (overall transparency) and `z order position` (position in the stacking order).
- Art-creation preferences for the layer, like `artwork knockout` and `blending mode.`

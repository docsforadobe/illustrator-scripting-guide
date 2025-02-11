# Object references

In AppleScript, Illustrator returns object references by index position or name. For example, this is a reference to the first path in layer 2

```applescript
path item 1 of layer 2 of document 1
```

An object's index position may change when other objects are created or deleted. For example, when a new path item is created on `layer 2`, the new path item becomes `path item 1 of layer 2 of document 1`.

This new object displaces the original path item, forcing the original to index position 2; therefore, any references made to `path item 1 of layer 2 of document 1` refer to the new object. This method of applying index numbers assures that lowest index number refers to the object that was worked on most recently.

Consider the following sample script:

```applescript
-- Make 2 new objects and try to select both
tell application "Adobe Illustrator"
    set newDocument to make new document
    set rectPath to make new rectangle in newDocument
    set starPath to make new star in newDocument
    set selection of newDocument to {rectPath, starPath}
end tell
```

This script does not select both the rectangle and the star, as intended; instead, it selects only the star. Try running the script with the Event Log window open, to observe the references returned from Illustrator for each consecutive `make` command. (Choose Event Log at the bottom of the Script Editor window.) Notice that both commands return the same object reference: `path item 1 of layer 1 of document 1`; therefore, the last line resolves to

```applescript
set selection of document 1 to {path item 1 of layer 1 of document 1,
    path item 1 of layer 1 of document 1}
```

A better approach is to reference the objects by name:

```applescript
tell application "Adobe Illustrator"
    set newDocument to make new document
    make new rectangle in newDocument with properties {name:"rectangle"}
    make new star in newDocument with properties {name:"star"}
    set selection of newDocument to
    {path item "rectangle" of newDocument,
    path item "star" of newDocument}
end tell
```

This example illustrates the need to uniquely identify objects in AppleScript scripts. We recommend that you assign names or variables to objects you need to access at a later time, as there is no guarantee you are accessing the objects you expect when accessing them by index.

---

## Obtaining objects from documents and layers

This script references an object as part of a document:

```applescript
-- Get reference for first page item of document 1
tell application "Adobe Illustrator"
    set pageItemRef to page item 1 of document 1
end tell
```

In the following script, the pageItemRef variable does not necessarily refer to the same object as in the previous script, because this script includes a reference to a layer:

```applescript
-- Get reference for first page item of layer 1 of document 1
tell application "Adobe Illustrator"
    set pageItemRef to page item 1 of layer 1 of document 1
end tell
```

---

## Creating new objects

To create a new object in AppleScript, use the `make` command.

---

## Working with selections

When the user makes a selection in a document, the selected objects are stored in the document's selection property. To access all selected objects in the active document:

```applescript
tell application "Adobe Illustrator"
    set myDoc to current document
    set selectedObjects to selection of myDoc
end tell
```

Depending on what is selected, the `selection` property value can be an array of any type of art objects. To get or manipulate the properties of the selected art items, you must retrieve the individual items in the array. To find out an object's type, use the `class` property.

The following sample gets the first object in the array, then displays the object's type:

```applescript
tell application "Adobe Illustrator"
    set myDoc to current document
    set selectedObjects to selection of myDoc
    set topObject to item 1 of selectedObjects
    display dialog (class of topObject)
end tell
```

The first object in a selection array is the selected object that was last added to the page, not the last object selected.

### Working with selections

To select an art object, the object's `selected` property.

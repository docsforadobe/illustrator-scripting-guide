<a id="scriptingvbscript-objectreferences"></a>

# Accessing and referencing objects

When you write a script, you must first decide which file, or `Document`, the script should act on. Through the `Application` object, the script can create a new document, open an existing document, or act on a document that is already open.

The script can create new objects in the document, operate on objects that the user selected, or operate on objects in one of the object collections. The following sections illustrate techniques for accessing,
referencing, and manipulating Illustrator objects

---

## Obtaining objects from collections

Generally, to obtain a reference to a specific object, you can navigate the containment hierarchy. For example, to use the `myPath` variable to store a reference to the first `PathItem` in the second layer of the active document

```basic
Set myPath = appRef.ActiveDocument.Layers(2).PathItems(1)
```

The following scripts demonstrate how to reference an object as part of a document:

```basic
Set documentRef = appRef.ActiveDocument

Set pageItemRef = documentRef.PageItems(1)
```

In the script below, the variable `pageItemRef` will not necessarily refer to the same object as the above script, since this script includes a reference to a layer:

```basic
Set documentRef = appRef.ActiveDocument
Set pageItemRef = documentRef.Layers(1).PageItems(1)
```

VBScript indexes start at 1 for object collections; however, VBScript allows you to specify whether array indexes start at 1 or 0. For information on specifying the index start number for arrays, see any VBScript textbook or tutorial.

---

## Creating new objects

You can use a script to create new objects. To create objects that are available from collection objects, use the collection object’s `Add` method:

```basic
Set myDoc = appRef.Documents.Add()

Set myLayer = myDoc.Layers.Add()
```

Some collection objects do not have an `Add` method. To create an object of this type, define a variable and use the `CreateObject` method. For example, the following code creates a new `CMYKColor` object using the variable name `newColor`

```basic
Set newColor = CreateObject ("Illustrator.CMYKColor")
```

---

## Working with selections

When the user makes a selection in a document, the selected objects are stored in the document’s `selection` property. To access all selected objects in the active document

```basic
Set appRef = CreateObject ("Illustrator.Application")
Set documentRef = appRef.ActiveDocument
selectedObjects = documentRef.Selection
```

Depending on what is selected, the selection property value can be an array of any type of art objects. To get or manipulate the properties of the selected art items, you must retrieve the individual items in the array. To find out an object’s type, use the `typename` property.

The following sample gets the first object in the array, then displays the object’s type

```basic
Set appRef = CreateObject ("Illustrator.Application")
Set documentRef = appRef.ActiveDocument
selectedObjects = documentRef.Selection
Set topObject = selectedObjects(0)
MsgBox(topObject.Typename)
```

The `MsgBox` method does not display a dialog when the script is run from the Illustrator Scripts menu (File > Scripts).

The first object in a selection array is the selected object that was last added to the page, not the last object selected.

### Working with selections

To select an art object, the object’s `Selected` property.

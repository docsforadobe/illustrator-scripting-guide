.. _scriptingJavascript/objectReferences:

Accessing and referencing objects
################################################################################

When you write a script, you must first decide which file, or ``document``, the script should act on. Through the ``application`` object, the script can create a new document, open an existing document, or act on a document that is already open.

The script can create new objects in the document, operate on objects that the user selected, or operate on objects in one of the object collections. The following sections illustrate various techniques for accessing, referencing, and manipulating Illustrator objects.

----

Referencing the application object
================================================================================

To obtain a reference to a specific object, you need to navigate the containment hierarchy. Because all JavaScript scripts are executed from within the Illustrator application, however, a specific reference to the application object is not required. For example, to assign the active document in Illustrator to the variable ``frontMostDocument``, you could reference the ``activeDocument`` property of the ``application`` object, as follows

::

  var frontMostDocument = activeDocument;

It is permissible to use the ``application`` object in a reference. To reference the ``application`` object, use the app global variable. The following two statements appear identical to the JavaScript engine::

  var frontMostDocument = activeDocument;

  var frontMostDocument = app.activeDocument;

----

Accessing objects in collections
================================================================================

All open documents, as well as the objects in a document, are collected into collection objects for the object type. A collection object contains an array of the objects that you can access by index or name. The collection object takes the plural form of the object name. For example, the collection object for the ``document`` object is ``documents``.

The following script sample gets all ``graphic style`` objects in the ``graphic styles`` collection; that is, it gets all graphic styles available to the active document

::

  var myStyles = app.activeDocument.graphicStyles;

All numeric collection references in JavaScript are zero-based: the first object in the collection has the index [0].

As a rule, JavaScript index numbers do not shift when you add an object to a collection. There is one exception: ``documents[0`` is always the active or frontmost document.

To access the first style in a ``graphic styles`` collection, you can use the variable declared in the previous script sample, or you can use the containment hierarchy to refer to the collection:

- Using the myStyles variable

::

    var firstStyle = myStyles[0];

- Using the containment hierarchy::

    var firstStyle = app.activeDocument.graphicStyles[0];

The following statements assign the name of the first graphic style in the collection to a variable. You can use these statements interchangeably.

::

    var styleName = myStyles[0].name

    var styleName = firstStyle.name

    var styleName = app.activeDocument.graphicStyles[0].name

To get the total number of objects in a collection, use the ``length`` property::

  alert ( myStyles.length );

The index of the last graphic style in the collection is ``myStyles.length - 1`` (-1 because the collection starts the index count at 0 and the length property counts from 1)::

  var lastStyle = myStyles[ myStyles.length - 1 ];

Note that an expression representing the index value is enclosed in square brackets ( [] ) as well as quotes.

If you know the name of an object, you can access the object in the collections using the name surrounded by square brackets; for example::

  var getStyle = myStyles["Ice Type"];

Each element in the collection is an object of the desired type, and you can access its properties through the collection. For example, to get an object’s name, use the ``name`` property::

  var styleName = app.activeDocument.graphicStyles[0].name;

To apply ``lastStyle`` to the first ``pageItem`` in the document, use its ``applyTo()`` method::

  lastStyle.applyTo( app.activeDocument.pageItems[0] );

----

Creating new objects
================================================================================

You can use a script to create new objects. To create objects that are available from collection objects, or containers, use the container object’s ``add()`` method

::

  var myDoc = app.documents.add()
  var myLayer = myDoc.layers.add()

Some object types are not available from containers. To create an object of this type, define a variable, then use the ``new`` operator with an object constructor to assign an object as the value. For example, to create a new ``CMYKColor`` object using the variable name ``myColor``::

  var myColor = new CMYKColor()

----

Working with selections
================================================================================

When the user makes a selection in a document, the selected objects are stored in the document’s ``selection`` property. To access all selected objects in the active document::

  var selectedObjects = app.activeDocument.selection;

The ``selection`` property value can be an array of any type of art objects, depending on what types of objects are selected. To get or manipulate the properties of the selected art items, you must retrieve the individual items in the array. To find out an object’s type, use the ``typename`` property.

The following sample gets the first object in the array, then displays the object’s type

::

  var topObject = app.activeDocument.selection[0];
  alert(topObject.typename)

The first object in a selection array is the selected object that was last added to the page, not the last object selected.

Selecting artwork objects
********************************************************************************

To select an art object, the object’s ``selected`` property.

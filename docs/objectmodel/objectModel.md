<a id="objectmodel-objectmodel"></a>

# The Illustrator Scripting Object Model

A good understanding of the Illustrator object model will improve your scripting abilities. The following figure shows the containment hierarchy of the object model, starting with the application object.

Note that the layer and group item classes can contain nested objects of the same class which can, in turn, contain additional nested objects.

![Illustrator Scripting Object Model](_static/objectmodel.png)

In addition to this application-specific object model, JavaScript provides certain utility objects, such as the File and Folder objects, which give you operating-system-independent access to the file system.

For details, see [JavaScript Tools Guide](http://estk.aenhancers.com).

# Scripting language support in Adobe Illustrator CC

Illustrator scripting supports VBScript and JavaScript scripts for Windows, and AppleScript and JavaScript scripts for Mac OS.

---

## Script file extensions

For a file to be recognized by Adobe Illustrator CC 2017 as a valid script file, the file must have the correct file name extension:

| Script Type                | File type (extension)                              | Platforms      |
|----------------------------|----------------------------------------------------|----------------|
| AppleScript                | compiled script ( .scpt ) OSAS file (no extension) | Mac OS         |
| JavaScript or ExtendScript | text ( .js or .jsx)                                | Windows Mac OS |
| VBScript                   | text ( .vbs )                                      | Windows        |

---

## JavaScript development options

You can use the ExtendScript Toolkit to create JavaScript scripts explicitly for Illustrator, or you can use Adobe Extension Builder and the Creative Cloud SDK to develop extensions in ActionScript.

Extensions are Flash-based (SWF) and can potentially work in a variety of Creative Cloud applications.

### Developing a CC extension using ActionScript

Creative Cloud applications have an extensibility infrastructure that allows developers to extend the capabilities of the applications; the infrastructure is based on Flash/Flex technology, and each extension is delivered as compiled Flash (SWF) file.

Creative Cloud includes the Extension Manager to enable installation of extensions.

An example of an extension that ships with the point products is Adobe Kuler. Kuler has a consistent user interface across the different suite applications, but has different logic in each, adapted to the host application.

The user interface for an extension is written in ActionScript, using the Flex framework. An extension is typically accessed through its own menu item in the application’s Extensions menu.

Adobe Extension Builder allows you to design the user interface interactively using the Design view of Flash Builder. The Creative Cloud SDK also allows you to develop all of the application logic for your extension in ActionScript; you can develop and debug your extension in the familiar Flash Builder environment.

To develop your application logic, we recommend using the ActionScript Wrapper Library ( CSAWLib ), which exposes the scripting DOM of each host application as an ActionScript library. This is tightly integrated with the Adobe Extension Builder environment, which includes wizards to help you build your extension’s basic structure, and run and debug your code against suite applications such as Adobe InDesign, Photoshop and Illustrator.

The methods, properties, and behavior of the scripting DOM is as described in the JavaScript Scripting Reference for the host application.

For details of how to use Adobe Extension Builder and the wrapper libraries, see the Creative Cloud SDK documentation, which is accessible from within Adobe Extension Builder.

### Scripting plug-ins

The CC JavaScript scripting interface allows for limited scripting for plug-ins. A plug-in can define a command, with an event and notifier, and a handler that performs some action. A JavaScript script can then use the `app.sendScriptMessage()` method to send parameters to that plug-in-defined command, and receive a plug-in-defined response.

For example, the Adobe Custom Workspace plug-in defines a command “Switch Workspace”. A script can invoke this command with the following code

```default
result = app.sendScriptMessage (
  "Adobe Custom Workspace",
  "Switch Workspace",
  '<workspace="Essentials" >'
);
```

In this case, the value that the plug-in returns is the string

```default
"<error= errNo>".
```

### ExtendScript features

If you write Illustrator-specific scripts that use the Illustrator JavaScript DOM directly, you will create ExtendScript files, which are distinguished by the .jsx extension.

Giving your JavaScript files a .jsx extension (rather than the standard .js extension for a JavaScript file) allows you to take advantage of ExtendScript features and tools.

ExtendScript offers all standard JavaScript features, plus a development and debugging environment, the ExtendScript Toolkit (ESTK).

The ESTK is installed with all scriptable Adobe applications, and is the default editor for JSX files. The ESTK includes an Object Model Viewer that contains complete documentation of the methods and properties of JavaScript objects. For information on accessing the ESTK and the Object Model Viewer see [Viewing the object model](viewingTheObjectModel.md#introduction-viewingtheobjectmodel).

ExtendScript also provides various tools and utilities, including the following:

- A localization utility
- Tools that allow you to combine scripts and direct them to particular applications
- Platform-independent file and folder representation
- Tools for building user interfaces to your scripts
- A messaging framework that allows you to send and receive scripts and data among scripting-enabled Adobe applications

All of these features are available whether you use the DOM directly with a JSX file, or indirectly through the ActionScript wrapper library and Adobe Extension Builder. For details of these and other features, see [JavaScript Tools Guide](http://estk.aenhancers.com).

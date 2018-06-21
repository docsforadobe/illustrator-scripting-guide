.. _introduction/viewingTheObjectModel:

Viewing the object model
################################################################################

Each of the supported scripting languages provides a facility for viewing the
scripting objects defined by Illustrator, with reference details.

----

.. _introduction/viewingTheObjectModel/javascript:

Viewing the JavaScript object model
================================================================================

To view the JavaScript object model for Illustrator, follow these steps:

In a default Adobe installation, the ESTK is in the following location:
=======  ===================================================================================
Windows  ``\system drive\Program Files\Adobe\Adobe Utilities CC\ExtendScript Toolkit CC``
Mac OS   ``\system drive\Applications\Utilities\Adobe Utilities CC\ExtendScript Toolkit CC``
=======  ===================================================================================

1. Start the ESTK.
2. In the ESTK, choose Help > Object Model Viewer.
3. In the Object Model Viewer window, select Adobe lllustrator CC Type Library from the Browser drop-down list.

Several extended sample scripts are in the ``/Scripting/Sample Scripts/``
folder in your Illustrator CC installation directory.

You also can view script samples and information about individual classes,
objects, properties, methods, and parameters in
**Adobe lllustrator CC Scripting Reference: JavaScript**, which you can
download from http://www.adobe.com/devnet/illustrator/scripting/.

----

.. _introduction/viewingTheObjectModel/applescript:

Viewing the AppleScript object model
================================================================================

Apple provides a Script Editor with all Mac OS systems. You can use
Script Editor to view the AppleScript dictionary that describes Illustrator
objects and commands.

For details of how to use Script Editor, see Script Editor Help.

.. note::
  In a default Mac OS installation, Script Editor is in
  ``Applications/AppleScript/Script Editor``

  If you cannot find the Script Editor application, you must reinstall it from
  your Mac OS system CD.

1. Start Script Editor.
2. Choose File > Open Dictionary. Script Editor displays an Open Dictionary dialog.
3. In the Open Dictionary dialog, find and select Adobe lllustrator CC, and click Open.

Script Editor displays a list of the Illustrator objects and commands, which
include the properties and elements associated with each object and the
parameters for each command.

Several extended sample scripts are in the ``/Scripting/Sample Scripts/``
folder in your Illustrator CC installation directory.

You also can view script samples and information about individual classes,
objects, properties, methods, and parameters in
**Adobe lllustrator CC Scripting Reference: AppleScript**, which you can
download from http://www.adobe.com/devnet/illustrator/scripting/.

----

.. _introduction/viewingTheObjectModel/vbscript:

Viewing the VBScript object model
================================================================================

VBScript provides a type library you can use to view Illustrator object
properties and methods. This procedure explains how to view the type library
through any Microsoft Office program. Your VBScript editor probably provides
access to the library. For information see your editor’s Help.

1. In any Microsoft Office application, choose Tools > Macro > Visual Basic Editor.
2. In the Visual Basic Editor, choose Tools > References.
3. In the dialog that appears, select the check box for Adobe lllustrator CC Type Library, and click OK.
4. Choose View > Object Browser, to display the Object Browser window.
5. Choose “Illustrator” from the list of open libraries in the top-left pull-down menu of the Object Browser window.

Several extended sample scripts are in the ``/Scripting/Sample Scripts/``
folder in your lllustrator CC installation directory.

You also can view script samples and information about individual classes,
objects, properties, methods, and parameters in
**Adobe lllustrator CC Scripting Reference: VBScript**, which you can
download from http://www.adobe.com/devnet/illustrator/scripting/.

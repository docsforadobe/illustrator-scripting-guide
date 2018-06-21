.. _introduction/executingScripts:

Executing Scripts
################################################################################

The Illustrator interface includes a Scripts menu (File > Scripts) that
provides quick and easy access to your scripts.

Scripts can be listed directly as menu items that run when you select them.
See :ref:`introduction/executingScripts/installing`

You can navigate from the menu to any script in your file system and then run
the script.
See :ref:`introduction/executingScripts/executing`

You also can have JavaScript scripts with a .jsx extension start automatically
when you launch the application. For information, see :ref:`introduction/executingScripts/startup`

----

.. _introduction/executingScripts/installing:

Installing scripts in the Scripts menu
================================================================================

To include a script in the Scripts menu (File > Scripts), save the script in
the Scripts folder, located in the ``/lllustrator CC/Presets`` folder in your
lllustrator CC installation directory.

The script’s filename, minus the file extension, appears in the Scripts menu.

Scripts that you add to the Scripts folder while Illustrator is running do not
appear in the Scripts menu until the next time you launch Illustrator.

Any number of scripts can be installed in the Scripts menu. If you have many
scripts, use subfolders in the Scripts folder to help organize the scripts in
the Scripts menu.

Each subfolder is displayed as a separate submenu containing the scripts
in that subfolder.

----

.. _introduction/executingScripts/executing:

Executing scripts from the Other Scripts menu item
================================================================================

The Other Scripts item at the end of the Scripts menu
``(File > Scripts > Other Scripts)`` allows you to execute scripts that are not
installed in the Scripts folder.

Selecting Other Scripts displays a Browse dialog, which you use to navigate to
a script file. When you select the file, the script is executed.

Only files that are of one of the supported file types are displayed in the
browse dialog. For details, see :ref:`introduction/scriptingLanguageSupport`

----

.. _introduction/executingScripts/startup:

Startup scripts (.jsx scripts only)
================================================================================

JavaScript scripts with a .jsx file extension can be installed in one of two
folders, so the scripts run automatically when you launch Illustrator and each
time you run a script.

The folders are:

- An application-specific startup scripts folder, which contains scripts
  for IllustratorCC
- A general startup scripts folder, which contains scripts that run
  automatically when you start any Creative Cloud application

Application-specific startup scripts folder
********************************************************************************

You must place application-specific startup scripts in a folder named
**Startup Scripts**, which you create in the Illustrator installation
directory.

For example, when IllustratorCC is installed to its default location, you
would create the Startup Scripts folder at the following location:

=======  ===============================================================
Windows  ``C:\Program Files\Adobe\Adobe lllustratorCC\Startup Scripts\``
Mac OS   ``/Applications/Adobe lllustrator CC/Startup Scripts/``
=======  ===============================================================

JavaScript scripts with a .jsx extension placed in the Startup Scripts folder
run automatically when:

- The application is launched.
- Any JavaScript file is selected from the Scripts menu (File > Scripts).

General startup scripts folder
********************************************************************************

The general startup scripts folder contains scripts that run automatically when
you start any Creative Cloud application.

You create the folder in the following location:

=======  =====================================================================
Windows  ``/Program Files/Common Files/Adobe/Startup Scripts CC/Illustrator``
Mac OS   ``/Library/Application Support/Adobe/Startup Scripts CC/Illustrator``
=======  =====================================================================

If a script in the general startup folder is meant to be executed only by
Illustrator, the script must include the ExtendScript #target directive
( ``#target illustrator`` ) or code like the following::

  if (BridgeTalk.appName == "illustrator") {
    //continue executing script
  }

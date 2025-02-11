.. _scripting/launching:

Launching and quitting Illustrator from a script
################################################################################

Your scripts can control the activation and termination of Illustrator.

----

Launching and activating Illustrator
================================================================================

AppleScript
********************************************************************************

In AppleScript, you use a tell statement to target Illustrator.

The activate command activates Illustrator if it is not already active

::

  tell application "Adobe Illustrator"
  activate
  end tell

JavaScript
********************************************************************************

Typically, you run JavaScript scripts from the application’s Scripts menu (File > Scripts) or start-up folder, so there is no need to launch Illustrator from your script.

Information on launching Illustrator in JavaScript is beyond the scope of this guide.

For details, search for `Interapplication Communication <https://javascript-tools-guide.readthedocs.io/1%20-%20Introduction/extendscript-overview.html#interapplication-communication-and-messaging>`__ or `Javascript Messaging Framework <https://javascript-tools-guide.readthedocs.io/5%20-%20Interapplication%20Communication%20with%20Scripts/communications-overview.html#messaging-framework>`__ in `JavaScript Tools Guide <http://estk.aenhancers.com>`__.


VBScript
********************************************************************************

In VBScript, there are several ways to create an instance of Illustrator:

- ``CreateObject`` launches Illustrator as an invisible application if it is not already running. If Illustrator is launched as an invisible application you must manually activate the application to make it visible:

.. code-block:: basic

  Set appRef = CreateObject("Illustrator.Application")

If you have multiple versions of Illustrator installed on the same machine and use the CreateObject method to obtain an application reference, using "Illustrator.Application" creates a reference to the latest Illustrator version. To specifically target an earlier version, use a version identifier at the end of the string:

===================  ================================
Illustrator 10       "Illustrator.Application.1"
Illustrator CS       "Illustrator.Application.2"
Illustrator CS2      "Illustrator.Application.3"
Illustrator CS3      "Illustrator.Application.4"
Illustrator CS4      "Illustrator.Application.CS4"
Illustrator CS5      "Illustrator.Application.CS5"
Illustrator CS6      "Illustrator.Application.CS6"
Illustrator CC       "Illustrator.Application.CC"
Illustrator CC 2014  "Illustrator.Application.CC2014"
Illustrator CC 2015  "Illustrator.Application.CC2015"
Illustrator CC 2017  "Illustrator.Application.CC2017"
===================  ================================

- Use the ``New`` operator if you added a reference to the Illustrator type library to the project. For example, the following line creates a new reference to the Application object:

.. code-block:: basic

  Set appRef = New Illustrator.Application

----

Quitting Illustrator
================================================================================

AppleScript
********************************************************************************

Use the quit command::

  tell application "Adobe Illustrator"
  quit
  end tell

JavaScript
********************************************************************************

Use the app.quit() method::

  app.quit();

VBScript
********************************************************************************

Use the Application object’s Quit method::

  Set appRef = CreateObject("Illustrator.Application")
  appRef.Quit

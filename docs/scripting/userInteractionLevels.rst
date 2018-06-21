.. _scripting/userInteractionLevels:

User-interaction levels
################################################################################

When user feedback is required, an application typically presents a dialog. This is called user interaction. It
is useful and expected when you are directly interacting with the application; however, when a script is
interacting with an application, a dialog brings the execution of the script to a halt until the dialog is
dismissed. This can be a serious problem in an automation environment, where there is no one present to
deal with dialogs.

The ``application`` object contains a ``user interaction level`` property that allows you to control the level
of interaction allowed during script execution. You can suppress interaction in an automation
environment or allow some interaction where scripts are being used in a more interactive fashion.

----

AppleScript
================================================================================

Using AppleScript, it is possible to send commands from one machine to another, so additional types of
interaction are possible. In AppleScript:, there are four possible values for the ``user interaction`` level
property:

+-------------------------+-----------------------------------------------------------------------------+
|     Property Value      |                                   Result                                    |
+=========================+=============================================================================+
| ``never interact``      | No interaction is allowed.                                                  |
+-------------------------+-----------------------------------------------------------------------------+
| ``interact with self``  | Interact only with scripts executed from the Scripts menu (File > Scripts). |
+-------------------------+-----------------------------------------------------------------------------+
| ``interact with local`` | Interact with scripts executed on the local machine (including self ).      |
+-------------------------+-----------------------------------------------------------------------------+
| ``interact with all``   | Interact with all scripts.                                                  |
+-------------------------+-----------------------------------------------------------------------------+


The four values allow you to control interaction based on the source of the script commands. For example,
if the application is acting as a server for remote users, it would be difficult for a remote user to dismiss a
dialog, but it would be no problem for someone sitting in front of the machine. In this case, an interaction
level of interact with local would prevent dialogs from halting remote scripts but would allow dialogs to be
presented for local scripts.

----

JavaScript
================================================================================

In JavaScript, there are two possible values for the ``app.userInteractionLevel`` property:

+-----------------------+----------------------------+
|    Property Value     |           Result           |
+=======================+============================+
| ``DISPLAYALERTS``     | Interaction is allowed.    |
+-----------------------+----------------------------+
| ``DONTDISPLAYALERTS`` | No interaction is allowed. |
+-----------------------+----------------------------+

----

VBScript
================================================================================

In VBScript, there are two possible values for the ``UserInteractionLevel`` property of the ``Application`` object:

+-------------------------+----------------------------+
|     Property Value      |           Result           |
+=========================+============================+
| ``aiDisplayAlerts``     | Interaction is allowed.    |
+-------------------------+----------------------------+
| ``aiDontDisplayAlerts`` | No interaction is allowed. |
+-------------------------+----------------------------+
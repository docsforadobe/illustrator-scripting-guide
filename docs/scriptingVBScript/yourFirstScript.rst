.. highlight:: basic

.. _scriptingVBScript/yourFirstScript:

Your first Illustrator script
################################################################################

The traditional first project in any programming language is displaying the message “Hello World!” In this
example, you create a new Illustrator document, then add a text frame containing this message. Follow
these steps:

1. Start any text editor (for example, Notepad).
2. Type the following code::

    Rem Hello World
    Set appRef = CreateObject("Illustrator.Application")
    Rem Create a new document and assign it to a variable
    Set documentRef = appRef.Documents.Add
    Rem Create a new text frame item and assign it to a variable
    Set sampleText = documentRef.TextFrames.Add
    Rem Set the contents and position of the TextFrame
    sampleText.Position = Array(200, 200)
    sampleText.Contents = "Hello World!"

3. Save the file as text-only in a folder of your choice, using the file extension ``.vbs``.
4. To test the script, do one of the following:

- Double-click the file.
- Start Illustrator, choose File > Scripts > Other Scripts, and navigate to and run your script file.

.. tip::
  To add the script to the Illustrator Scripts menu (File > Scripts), save the script in the Scripts folder. The script will appear on the menu the next time you start Illustrator. For details, see “Installing scripts in the Scripts menu” on page 10.

  In general, when you launch a VBScript script from the Scripts menu, any ``msgBox`` dialogs will not display correctly.

----

Adding features to “Hello World”
================================================================================

Next, we create a new script that makes changes to the Illustrator document you created with your first
script. Our second script demonstrates how to:

- Get the active document.
- Get the width of the active document.
- Resize the text frame to match the document’s width.

If you already closed the Illustrator document, run your first script again to create a new document.

Follow these steps:

1. Copy the following script into your text editor, and save the file::

    Set appRef = CreateObject("Illustrator.Application")
    'Get the active document
    Set documentRef = appRef.ActiveDocument
    Set sampleText = documentRef.TextFrames(1)
    ' Resize the TextFrame item to match the document width
    sampleText.Width = documentRef.Width
    sampleText.Left = 0

2. Run the script.

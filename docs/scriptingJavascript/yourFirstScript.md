<a id="scriptingjavascript-yourfirstscript"></a>

# Your first Illustrator script

The traditional first project in any programming language is displaying the message “Hello World!” In this example, you create a new Illustrator document, then add a text frame containing this message. Follow
these steps:

For information on locating the ExtendScript Toolkit, see [Viewing the JavaScript object model](../introduction/viewingTheObjectModel.md#introduction-viewingtheobjectmodel-javascript).

1. Using any text editor (including Adobe^ InDesign® or the ESTK), enter the following text:
   ```default
   //Hello World!
   var myDocument = app.documents.add();
   //Create a new text frame and assign it to the variable "myTextFrame"
   var myTextFrame = myDocument.textFrames.add();
   // Set the contents and position of the text frame
   myTextFrame.position = [200,200];
   myTextFrame.contents = "Hello World!"
   ```
2. To test the script, do either of the following:

> - If you are using the ESTK, select Adobe lllustrator CC 2017 from the drop-down list in the upper-left corner, select Yes to start Illustrator, then choose Debug > Run in the ESTK to run the script.
> - If you are using a different text editor than the ESTK, save the file as text-only in a folder of your choice, using the file extension .jsx , then start Illustrator. In Illustrator, choose File > Scripts > Other Scripts, and navigate to and run your script file.

---

## Adding features to “Hello World”

Next, we create a new script that makes changes to the Illustrator document you created with your first script. Our second script demonstrates how to:

- Get the active document.
- Get the width of the active document.
- Resize the text frame to match the document’s width.

If you already closed the Illustrator document, run your first script again to create a new document.

Follow these steps:

1. In Script Editor, choose File > New to create a new script.
2. Enter the following code:
   ```default
   var docRef = app.activeDocument;
   var docWidth = docRef.width
   var frameRef = docRef.textFrames[0]
   frameRef.width = docWidth
   ```
3. Run the script.

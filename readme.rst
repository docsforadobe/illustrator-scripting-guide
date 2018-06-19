**Description**

Repo hosting the Illustrator Scripting Guide RST docs, linked into a http://readthedocs.io system hosted at http://ai.aenhancers.com

This came from the Adobe Illustrator CC Scripting Guide (https://www.adobe.com/devnet/illustrator/scripting.html).

----

This is still VERY wip! Still to do:

**To-do**

Scripting Guide Section:
========================

- Find/replace "on page x" with links to sections
- Find/replace ``keyword`` with link to section
- Find/replace "JS Tools Guide" with link to estk.aenhancers.com

Code Reference:
===============

- Finish JS obj ref
	- Keep adding things
	- Organize into folders / sections based on root object
	-
- Add Applescript obj ref
- Add VBScript obj ref
- Changelog

----

**Contribution**

Contributors are welcome and encouraged to suggest fixes, adjustments, notes/warnings, and anything else that may help the project.

----

**Admonitions Usage**

Currently, the following `admonitions <http://docutils.sourceforge.net/docs/ref/rst/directives.html#admonitions>`_ are in use in this project. Try to keep one piece of data per note, for easier parsing.

	.. note::
		Notes detail version added, and/or relevant pieces of information.

	.. tip::
		Tips supply helpful suggestions on usage or behaviours.

	.. warning::
		Warnings convey negative behaviours, or when something won't work the way you'd expect.

----

**Build HTML Locally**

You may want to build the HTML locally before pushing, in order to ensure that the result is what you'd expect. These files aren't included in the git repo, nor are they used online; this is solely to create a local, offline version of the online docs.

- Install ``Python 2.7``
- Install ``pip``
- Navigate to the project directory and use the command ``pip install -r requirements.txt``
- Build the docs using ``make html``

----

**Licensing & Ownership**

This project exists for educational purposes only.

All content is copyright Adobe Systems Incorporated.

.. _printingDocuments:

Printing Illustrator documents
################################################################################

Using the ``print options`` scripting feature, you can capture and automate parts of your print workflow.
Scripting exposes the full capabilities of Illustrator printing, some of which may not be accessible through
the application’s user interface.

Illustrator supports at most one print session at a time, because of limits in the current printing
architecture.

The ``document`` object’s print command or method takes one optional parameter, which allows you to
specify a ``print options`` object.

The print options object allows you to define print settings like PPD, PostScript options, paper options,
and color-management options. The ``print options`` object also has a ``print preset`` property, which
allows you to specify a preset to define your print job.

When defining the properties of a ``print options`` object, you can find out which printers, PPDs, print
presets, and other items are available by using the ``application`` object’s read-only “list” properties, such
as the ``printer list``, ``PPD file list``, and ``print presets list`` properties.

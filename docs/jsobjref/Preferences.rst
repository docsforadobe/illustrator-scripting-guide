.. _jsobjref/Preferences:

Preferences
################################################################################

``app.Preferences``

**Description**

Specifies the preferred options for AutoCAD, FreeHand, PDF, and Photoshop files.

----

==========
Properties
==========

.. _jsobjref/Preferences.AutoCADFileOptions:

Preferences.AutoCADFileOptions
********************************************************************************

``app.preferences.AutoCADFileOptions``

**Description**

Options to use when opening or placing an AutoCAD file.

**Type**

:ref:`jsobjref/OpenOptionsAutoCAD`; read-only.

----

.. _jsobjref/Preferences.FreeHandFileOptions:

Preferences.FreeHandFileOptions
********************************************************************************

``app.preferences.FreeHandFileOptions``

**Description**

Options to use when opening or placing a FreeHand file.

**Type**

:ref:`jsobjref/OpenOptionsFreeHand`; read-only.

----

.. _jsobjref/Preferences.parent:

Preferences.parent
********************************************************************************

``app.preferences.parent``

**Description**

The parent of this object.

**Type**

object; read-only.

----

.. _jsobjref/Preferences.PDFFileOptions:

Preferences.PDFFileOptions
********************************************************************************

``app.preferences.PDFFileOptions``

**Description**

Options to use when opening or placing a PDF file.

**Type**

:ref:`jsobjref/PDFFileOptions`; read-only.

----

.. _jsobjref/Preferences.PhotoshopFileOptions:

Preferences.PhotoshopFileOptions
********************************************************************************

``app.preferences.PhotoshopFileOptions``

**Description**

Options to use when opening or placing a Photoshop file.

**Type**

:ref:`jsobjref/PhotoshopFileOptions`; read-only.

----

.. _jsobjref/Preferences.typename:

Preferences.typename
********************************************************************************

``app.preferences.typename``

**Description**

The class name of the referenced object.

**Type**

string; read-only.

----

=======
Methods
=======

.. _jsobjref/Preferences.getBooleanPreference:

Preferences.getBooleanPreference
********************************************************************************

``app.preferences.getBooleanPreference(key)``

**Description**

Gets the boolean value of a given application preference.

**Parameters**

+-----------+--------+--------------------------+
| Parameter |  Type  |       Description        |
+===========+========+==========================+
| ``key``   | String | Pref key of value to get |
+-----------+--------+--------------------------+

**Returns**

Boolean

----

.. _jsobjref/Preferences.getIntegerPreference:

Preferences.getIntegerPreference
********************************************************************************

``app.preferences.getIntegerPreference(key)``

**Description**

Gets the integer value of a given application preference.

**Parameters**

+-----------+--------+--------------------------+
| Parameter |  Type  |       Description        |
+===========+========+==========================+
| ``key``   | String | Pref key of value to get |
+-----------+--------+--------------------------+

**Returns**

Integer

----

.. _jsobjref/Preferences.getRealPreference:

Preferences.getRealPreference
********************************************************************************

``app.preferences.getRealPreference(key)``

**Description**

Gets the real-number value of a given application preference.

**Parameters**

+-----------+--------+--------------------------+
| Parameter |  Type  |       Description        |
+===========+========+==========================+
| ``key``   | String | Pref key of value to get |
+-----------+--------+--------------------------+

**Returns**

Real

----

.. _jsobjref/Preferences.getStringPreference:

Preferences.getStringPreference
********************************************************************************

``app.preferences.getStringPreference(key)``

**Description**

Gets the string value of a given application preference.

**Parameters**

+-----------+--------+--------------------------+
| Parameter |  Type  |       Description        |
+===========+========+==========================+
| ``key``   | String | Pref key of value to get |
+-----------+--------+--------------------------+

**Returns**

String

----

.. _jsobjref/Preferences.removePreference:

Preferences.removePreference
********************************************************************************

``app.preferences.removePreference(key)``

**Description**

Deletes a given application preference.

**Parameters**

+-----------+--------+--------------------------+
| Parameter |  Type  |       Description        |
+===========+========+==========================+
| ``key``   | String | Pref key of value to get |
+-----------+--------+--------------------------+

**Returns**

Nothing.

----

.. _jsobjref/Preferences.setBooleanPreference:

Preferences.setBooleanPreference
********************************************************************************

``app.preferences.setBooleanPreference(key, value)``

**Description**

Sets the boolean value of a given application preference.

**Parameters**

+-----------+---------+--------------------------+
| Parameter |  Type   |       Description        |
+===========+=========+==========================+
| ``key``   | String  | Pref key of value to get |
+-----------+---------+--------------------------+
| ``value`` | Boolean | Value to set             |
+-----------+---------+--------------------------+

**Returns**

Nothing.

----

.. _jsobjref/Preferences.setIntegerPreference:

Preferences.setIntegerPreference
********************************************************************************

``app.preferences.setIntegerPreference(key, value)``

**Description**

Sets the integer value of a given application preference.

**Parameters**

+-----------+---------+--------------------------+
| Parameter |  Type   |       Description        |
+===========+=========+==========================+
| ``key``   | String  | Pref key of value to get |
+-----------+---------+--------------------------+
| ``value`` | Integer | Value to set             |
+-----------+---------+--------------------------+

**Returns**

Nothing.

----

.. _jsobjref/Preferences.setRealPreference:

Preferences.setRealPreference
********************************************************************************

``app.preferences.setRealPreference(key, value)``

**Description**

Sets the real-number value of a given application preference.

**Parameters**

+-----------+--------+--------------------------+
| Parameter |  Type  |       Description        |
+===========+========+==========================+
| ``key``   | String | Pref key of value to get |
+-----------+--------+--------------------------+
| ``value`` | Double | Value to set             |
+-----------+--------+--------------------------+

**Returns**

Nothing.

----

.. _jsobjref/Preferences.setStringPreference:

Preferences.setStringPreference
********************************************************************************

``app.preferences.setStringPreference(key, value)``

**Description**

Sets the string value of a given application preference.

**Parameters**

+-----------+--------+--------------------------+
| Parameter |  Type  |       Description        |
+===========+========+==========================+
| ``key``   | String | Pref key of value to get |
+-----------+--------+--------------------------+
| ``value`` | String | Value to set             |
+-----------+--------+--------------------------+

**Returns**

Nothing.

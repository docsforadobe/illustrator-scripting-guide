# Working with the perspective grid

!!! note
    This functionality was added in Illustrator CC 2017

The Perspective Grid is a feature that enables you to create and manipulate art in a spatial environment using established laws of perspective. Enable Perspective Grid using the View > Perspective Grid menu or the perspective tools in the toolbar.

The SDK provides an API for working with the perspective grid programmatically, and your scripts have some access to this API. A script can:

- Set a the default grid parameters using preset values.
- Show or hide the grid.
- Set the active plane.
- Draw an object in perspective on the active plane.
- Bring an object into perspective.

---

## Use perspective presets

Illustrator provides default grid-parameter presets for one-point, two-point, and three-point perspectives. The presets are named `"[1P-NormalView]"`, `"[2P-NormalView]"`, and `"[3P-NormalView]"`.

The script shows how to select the two-point perspective preset programmatically:

```applescript
tell application "Adobe Illustrator"
    --Create a new document
    set docRef to make new document
    tell docRef
        --Select the default two-point perspective preset
        select perspective preset perspective preset "[2P-Normal View]"
    end tell
end tell
```

You can create new perspective presets, export presets to files, and import presets from files. These scripts shows how to export and import presets:

```applescript
tell application "Adobe Illustrator"
    set docRef to make new document
    set filePath to "Macintosh HD:scripting:PGPresetsExported"
    export perspective grid preset of docRef to file filePath
end tell

tell application "Adobe Illustrator"
    set docRef to make new document
    set filePath to "Macintosh HD:scripting:PGPresets"
    import perspective grid preset of docRef from file filePath
end tell
```

---

## Show or hide the grid

This script shows or hides the Perspective Grid programmatically:

```applescript
tell application "Adobe Illustrator"
    --Create a new document
    set docRef to make new document
    tell docRef
        --Display the perspective grid defined in the document
        show perspective grid
        --Hide the perspective grid defined in the document
        hide perspective grid
    end tell
end tell
```

---

## Set the active plane

The perspective grid plane types are:

|     Plane     |                Type                 |
| ------------- | ----------------------------------- |
| Left plane    | `perspective grid plane leftplane`  |
| Right plane   | `perspective grid plane rightplane` |
| Floor plane   | `perspective grid plane floorplane` |
| Invalid plane | `perspective grid plane noplane`    |

For a one-point perspective grid, only the left and floor plane are valid.

This script sets the active perspective plane to the left plane:

```applescript
tell application "Adobe Illustrator"
    --Create a new document
    set docRef to make new document
    tell docRef
        --Set the active plane to the left plane
        set perspective active plane perspective grid plane leftplane
    end tell
end tell
```

---

## Draw on a perspective grid

When the Perspective Grid is on, drawing methods allow you to draw or operate on objects in perspective. This script creates a new document, shows a two-point perspective grid, and draws art objects on the left
plane

```applescript
tell application "Adobe Illustrator"
    --Create a new document
    set docRef to make new document
    tell docRef
        --Select the default two-point perspective preset
        select perspective preset perspective preset "[2P-Normal View]"

        --Display the perspective grid defined in the document
        show perspective grid

        --Check if active plane is set to left, otherwise set it to left
        if (get perspective active plane) is not leftplane then
            set perspective active plane perspective grid plane leftplane
        end if

        --Draw rectangle in perspective, then resize to 200% and move
        set rectRef to make new rectangle with properties {bounds:{0, 0, 30, 30}, reversed:false}
        scale rectRef horizontal scale 200 vertical scale 200 about top left with transforming objects
        translate rectRef delta x -420 delta y 480

        --Draw ellipse in perspective
        set ellipseRef to make new ellipse with properties {bounds:{60, -60, 90, -30}, reversed:false, inscribed:true}

        --Draw rounded rectangle in perspective
        set rrectRef to make new rounded rectangle with properties {bounds:{90, -90, 30, 30}, horizontal radius:10, vertical radius:10, reversed:false}

        --Draw polygon in perspective
        set polyRef to make new polygon with properties {center point:{105, 105}, radius:15, sides:7, reversed:false}

        --Draw star in perspective
        set starRef to make new star with properties {center point:{135, 135}, radius:15, inner radius:10, point count:6, reversed:false}

        --Draw path in perspective
        set newPath to make new path item with properties {entire path:{{anchor:{0, 0}}, {anchor:{60, 0}}, {anchor:{30, 45}}, {anchor:{90, 110}}}}
    end tell
end tell
```

---

## Bring objects into perspective

If an art object is not in perspective, use the `bringInPerspective()` method to bring it into perspective and place it on a plane.

This script creates a new document, draws an art object, and brings it into perspective on a three-point perspective grid:

```applescript
tell application "Adobe Illustrator"
    --Create a new document
    set docRef to make new document
    tell docRef
        --Draw star
        set starRef to make new star with properties {center point:{135, 135}, radius:15, inner radius:10, point count:6, reversed:false}

        --Select the default three-point perspective preset
        select perspective preset perspective preset "[3P-Normal View]"

        --Display the perspective grid defined in the document
        show perspective grid

        --Check if active plane is set to left, otherwise set it to left
        if (get perspective active plane) is not leftplane then
            set perspective active plane perspective grid plane leftplane
        end if

        --Bring star to floor plane
        bring in perspective starRef position x 100 position y 100 perspective grid plane floorplane
    end tell
end tell
```

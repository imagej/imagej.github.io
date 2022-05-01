---
title: Keyboard Shortcuts
section: Learn:ImageJ Basics
nav-links: true
---

ImageJ has a lot of keyboard shortcuts.

## Listing all keyboard shortcuts

For a verbose list of keyboard shortcuts, call
{% include bc path='Plugins | Shortcuts | List Shortcuts' %}.

## The search bar

Use {% include key key='ctrlcmd|L' %} to jump to the
[search bar](/learn#the-search-bar),
to call menu entries by name.

## Recent commands

To open a list of some recent commands, and a list of the most frequently
called commands, press {% include key key='ctlcmd|9' %}.

## Open

To open new images, press {% include key keys='ctlcmd|O' %}.

## Creating your own keyboard shortcuts

You can also
[assign your own keyboard shortcuts](https://imagej.nih.gov/ij/docs/guide/146-31.html#toc-Subsection-31.2)!

## Assign a shortcut to a macro

There are 3 options to assign a keyboard shortcut to a macro:

### Option 1: Edit the StartupMacros file

Either put the code of the macro in the file `macros/StartupMacros.ijm`
(or `StartupMacros.fiji.ijm` in Fiji) to have it installed automatically at
startup.

The code of the macro must declare a keyboard shortcut in square brackets:

```javascript
macro "Macro 1 [1]" {
    print("The user pressed '1' on the top row of the keyboard");
}

macro "Macro 1.2 [n1]" {
    print("The user pressed '1' on the numerical keypad");
}

macro Macro 1.3 [&1]{
    print("The user pressed '1' either on the numerical keyboard or on the top row of the keyboard. This is new since ImageJ v1.53a, thanks to Norbert Vischer.")
}

macro "Macro 2 [h]" {
    print ("the user pressed 'h'");
}

macro "Macro 3 [H]"{
    print ("the user pressed 'shift + h'");
}
```

The key defined in square bracket is case sensitive ! If a capital letter is used then the shortcut is {% include key keys="shift | &lt;key&gt;" %}.

### Option 2: Save the macro(s) as a toolset

The shortcut should be defined in square bracket like for option 1, but instead
of editing the existing StartupMacros file, the macros(s) can be saved as a
separate MyShortcut.ijm or .txt file in the ImageJ/Fiji subfolder
`macros/toolsets`.

Then restart ImageJ/Fiji and click the {% include bc path='&gt;&gt;' %} at the
rightmost side of the fiji toolbar and click the entry MyShortcut. This will
install your macros and thus activate the associated shortcuts.

This option is more convenient to distribute macros with keyboard shortcuts to
colleagues or via an update site.

### Option 3: Associate shortcut to a plugin menu entry

The third possibility consists of saving the macro code as a small script file
into the `./Fiji.app/scripts/Plugins/` folder, so that it appears in the menu
upon restart.

Then you can register a shortcut using
{% include bc path='Plugins|Shortcuts|Add Shortcut...' %}.

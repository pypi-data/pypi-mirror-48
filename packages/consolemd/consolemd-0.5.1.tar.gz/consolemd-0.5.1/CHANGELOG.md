# Changelog

Here's what we all hope is an accurate list of things that have changed
between versions.

## v0.5.1

* fixes wrapping (and extra spaces) when width specified on command line
* thematic break now uses unicode wide dash and obeys width

## v0.5.0

* adding --width flag to command line
* added some more tests

## v0.4.5

* attempting to freeze with pyinstaller
* attempting to create release build with travisci

## v0.4.4

* fix deprecated CommonMark to commonmark

## v0.4.3

* fixed `--version` option which always ran

## v0.4.2

* adding `--version` option to command line

## v0.4.1

* using list comprehension instead of list() function
* hopefully doing a proper deploy to pypi

## v0.4.0

* consolemd is now a python3 app, thanks to tek and kseistrup
* added a few sanity tests

## v0.3.2

* fixed several errors with unicode decoding
* fixed bug where headers get continously darker

## v0.3.1

* mainly doc updates, bug fixes and some refactoring
* exit with error if chosen style doesn't exist
* minor tweaks to README.md, show README.md as example image
* added section on OSX italics to README.md

## v0.3.0

* show image/link text and show their urls as footnotes at end of document

## v0.2.1

* can now load and render a utf-8 encoded file

## v0.2.0

* inserting vertical whitespace is much simpler and much more effective
* added --soft-wrap option to break at source line endings

## v0.1.0

First release. Appears to work even if the styling code is pretty ugly.

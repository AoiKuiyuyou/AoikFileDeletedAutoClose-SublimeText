[:var_set('', """
# Compile command
aoikdyndocdsl -s README.src.md -n aoikdyndocdsl.ext.all::nto -g README.md
""")
]\
[:HDLR('heading', 'heading')]\
# AoikFileDeletedAutoClose
A Sublime Text plugin to automatically close the focused view if the viewed
 file has been deleted.

Tested working with:
- Sublime Text 2
- Sublime Text 3

## Table of Contents
[:toc(beg='next', indent=-1)]

## Setup

### Setup via git
Clone this repository to Sublime Text's **Packages** directory (Preferences - Browse Packages...):
```
git clone https://github.com/AoiKuiyuyou/AoikFileDeletedAutoClose-SublimeText AoikFileDeletedAutoClose
```

Make sure the repository directory is renamed to **AoikFileDeletedAutoClose**
(without the "-SublimeText" postfix), otherwise it may not work well.

## Usage
Open a file in Sublime Text, delete the file, then when this file's view in
 Sublime Text gets focus it will be closed automatically.

Views with a file path under Sublime Text's "Packages" directory will not be
closed, because many plugins (including this one) open settings views with
non-existent file path under the "Packages" directory, which will otherwise be
considered "deleted" by this plugin.

Views with unsaved changes will not be closed by default. This can be adjusted
in settings.

Settings can be adjusted at
"Preferences - Package Settings - AoikFileDeletedAutoClose".

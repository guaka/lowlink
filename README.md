
**lowlink.py** is a Python script to recursively create lowercase
symbolic links to files with capitals. This can be useful when
migrating from a case insensitive system to a case sensitive system,
e.g.  when converting a website from ASP on Windows to Drupal on LAMP.

This script was developed by [Kasper Souren](http://guaka.org/) for
migrating [B'Tselem's website](http://www.btselem.org/) to Drupal.

You might want to do something like this in Apache's virtual host
configuration, note that this doesn't work in `.htaccess`.

        RewriteEngine on
        RewriteMap lc int:tolower
        RewriteCond %{REQUEST_URI} [A-Z]
        RewriteRule (.*) ${lc:$1} [R=301,L]


See also [the accompanying blog post](http://guaka.org/recursively-create-lowercase-symlinks-filenames-uppercase-letters-python)
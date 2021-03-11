
**lowlink.py** is a Python script to recursively create lowercase
symbolic links to files with capitals. This can be useful when
migrating from a case insensitive system to a case sensitive system,
e.g.  when converting a website from ASP on Windows to Drupal on LAMP.

You might want to do something like this in Apache's virtual host
configuration, note that this doesn't work in `.htaccess`.

        RewriteEngine on
        RewriteMap lc int:tolower
        RewriteCond %{REQUEST_URI} [A-Z]
        RewriteRule (.*) ${lc:$1} [R=301,L]


See also [the accompanying blog post](https://guaka.org/recursively-create-lowercase-symlinks-filenames-uppercase-letters-python)

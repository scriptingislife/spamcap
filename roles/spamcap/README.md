Role Name
=========

Install's Postfix then configures it to use the spamcap hook. Script can be found in `files/`.

Requirements
------------

Only tested on Ubuntu 16.04.

Role Variables
--------------

* `hostname` is the hostname used by postfix. Doesn't affect system hostname.
* `root_dir` is the place that the hook script and other files will be placed.
* `hook_file` is the filename of the hook script.

Example Playbook
----------------

    - hosts: servers
      roles:
         - spamcap

License
-------

BSD
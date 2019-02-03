Role Name
=========

Install's Postfix and PHP packages then configures Postfix to use the PHP hook. Script can be found in `files/`.

Requirements
------------

Currently only worked on Debian systems with apt.

Role Variables
--------------

* `hostname` is the hostname used by postfix. Doesn't affect system hostname.

Example Playbook
----------------

    - hosts: servers
      roles:
         - { role: spamcap, hostname: 'spamcap.test'}

License
-------

BSD
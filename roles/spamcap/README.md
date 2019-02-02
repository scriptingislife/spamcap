Role Name
=========

Install's Postfix and PHP packages then configures Postfix to use the PHP hook.

Requirements
------------

Currently only uses apt.

Role Variables
--------------

None currently.

Example Playbook
----------------

    - hosts: servers
      roles:
         - { role: spamcap }

License
-------

BSD
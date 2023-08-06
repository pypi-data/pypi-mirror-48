=========================================================
FBUPKEEP - Firebird server & database maintenance utility
=========================================================

FBUPKEEP is basically a task executor engine. Its primary purpose is to run maintenance
tasks for `Firebird`_ ® servers and databases, but could be easily extended to run other
tasks of various type.

Built-in tasks:

* Logical (gbak) database backup and restore.
* Database sweep.
* Collection of database statistics (gstat).
* Update index statistics in database.
* Rebuild of user indices in database.
* Removal of old files.

FBUPKEEP is designed to run on Python 3.5+, and uses FDB_ Firebird driver.

.. _Firebird: http://www.firebirdsql.org
.. _FDB: https://github.com/FirebirdSQL/fdb

Trunk Based Development
=======================

`Trunk Based Development <https://trunkbaseddevelopment.com>`_ recommends
short-lived topic branches that are merged into a single ``main`` branch.
:abbr:`TBD (Trunk Based Development)` leads to an easily managed linear
progression.

Trunk Based Development is a perfect fit for one-person projects.
Branches are not necessary, but using a version control system 
pays off quickly even for a single developer.

In smaller development teams, each pair-programming duo preferably transfers
small commits directly to the trunk (or ``main`` branch), although the build
must first be successfully executed before integration.

Trunk based development on a large scale is best done with short-lived feature
branches, where one person develops over a few days at most, and the changes are
then integrated into the trunk (or ``main``) with pull or merge requests, code
review and build automation.

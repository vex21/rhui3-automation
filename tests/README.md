About
---------------
Setup of RHUI3 test framework

Requirements
---------------
* Ansible version 1.9.2 and higher. (It's possible that you will get older version using standard distro repositories. Try using "pip install -U ansible" instead. You might need to install easy_install first.)
* RHUI3 set up.

Usage
--------
  To include testing stage in RHUI3 deployment see [RHUI deployment Readme](https://github.com/RedHatQE/rhui3-automation/blob/master/deploy/README.md).
  
  Tests can be run any time after RHUI3 deployment. 
  * Update/create your hosts.cfg file with addresse of RHUA machine in [TESTS] section.
  * Be in deploy/ directory and run:
  
  `ansible-playbook -i ~/pathto/hosts.cfg site.yml --tags tests`
  
  


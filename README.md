webhook-listener
=========
[![Build Status](https://travis-ci.org/joshuacherry/ansible-role-webhook-listener.svg?branch=master)](https://travis-ci.org/joshuacherry/ansible-role-webhook-listener)  

Installs [webhook-listener](https://github.com/joshuacherry/Git-Auto-Deploy).

Requirements
------------
None.

Role Variables
--------------

**url:** The URL to the repository.  
**branch:** The branch which will be checked out.  
**remote:** The name of the remote to use.  
**path:** Path to clone the repository to. If omitted, the repository won't be cloned, only the deploy scripts will be executed.  
**deploy:** A command to be executed. If path is set, the command is executed after a successfull pull.  
**filters:** Filters to apply to the web hook events so that only the desired events result in executing the deploy actions. See section Filters for more details.  
**secret-token:** The secret token set for your webhook (currently only implemented for GitHub and GitLab)

Dependencies
------------
none

Example Playbook
----------------

```
- hosts: servers
  roles:
    - role: webhook-listener
  vars:
    webhook_listener_name: "webhook-listener"
    webhook_listener_daemon_user: "root"
    webhook_listener_daemon_group: "root"
    webhook_listener_repo: "https://github.com/joshuacherry/Git-Auto-Deploy.git"
    webhook_listener_destination: "/opt/{{ webhook_listener_name }}"
    webhook_listener_version: "master"
    webhook_listener_remote: "origin"
    webhook_listener_pip_requirements: "{{ webhook_listener_destination }}/requirements.txt"

    # Config File Variables
    webhook_listener_conf_pidfilepath: "/var/run/webhook-listener.pid"
    webhook_listener_conf_logfilepath: "/var/log/webhook-listener.log"
    webhook_listener_conf_host: "0.0.0.0"
    webhook_listener_conf_port: "8001"

    webhook_listener_conf_repositories:
      - url: "https://github.com/joshuacherry/Git-Auto-Deploy.git"
        branch: "master"
        remote: "origin"
        path: "{{ webhook_listener_destination }}"
        deploy: "echo deploying"
        filters:
          - object_kind: 'push'
          - ref: 'refs/heads/master'
        secret-token: ""
      - url: "https://github.com/username/test.git"
        branch: "master"
        remote: "origin"
        path: "/repos/test"
        deploy: "echo deploying"
        filters:
          - object_kind: 'push'
          - ref: 'refs/heads/master'
        secret-token: "12345"
```

License
-------

MIT

Author Information
------------------

An optional section for the role authors to include contact information, or a website (HTML is not allowed).

# webhook-listener

[![Build Status](https://travis-ci.org/joshuacherry/ansible-role-webhook-listener.svg?branch=master)](https://travis-ci.org/joshuacherry/ansible-role-webhook-listener)  

Installs [webhook-listener](https://github.com/joshuacherry/Git-Auto-Deploy) which consists of a small HTTP server that listens for Web hook requests sent from GitHub, GitLab or Bitbucket servers. This application allows you to continuously and automatically deploy you projects each time you push new commits to your repository.

## Requirements
- none

## Install
`ansible-galaxy install joshuacherry.webhook-listener`

## Supported Operating Systems
| OS            |
| :------------ |
| Debian 8      | ✓             |
| Ubuntu 16.04  | ✓             |
| Centos 7      | ✓             |

## Role Variables

**url:** The URL to the repository.  
**branch:** The branch which will be checked out.  
**remote:** The name of the remote to use.  
**path:** Path to clone the repository to. If omitted, the repository won't be cloned, only the deploy scripts will be executed.  
**deploy:** A command to be executed. If path is set, the command is executed after a successfull pull.  
**filters:** Filters to apply to the web hook events so that only the desired events result in executing the deploy actions. See section Filters for more details.  
**secret-token:** The secret token set for your webhook (currently only implemented for GitHub and GitLab)

## Example Playbook

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
        header_filter:
          - X-GitHub-Event: 'push'
        secret-token: "12345"
```

## Testing
Local testing can be done using Vagrant.
1. Bring up the Vagrant VM with `vagrant up`
2. SSH into the VM with `vagrant ssh` or `ssh 127.0.0.1:2222` or `ssh 10.1.15.10`
3. Change directories into /vagrant `cd /vagrant`
4. You can test the role against each Dockerfile with:  
`make centos7 test`  
`make jessie64 test`  
`make xenial64 test`  


## License

The MIT License (MIT)

Copyright (c) 2017 Joshua Cherry

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

# Deploy full stack flask application by Ansible 
In this project I used flask application with mariaDB database.
I used galera cluster for Databases to let the application can use three nodes of mariaDB
I used proxysql as a loadbalancer to achieve high availability to accessing databases nodes.

## To run my Ansible project
``` sh 
    $ ansible-playbook -i hosts.txt fullyprojectplay.yml --vault-password-file ~/.passwords/vault-pass 
```
## Accessing flask application with GUI
![Page 1](./imgs/page1.png)



# Deploy full stack flask application by Ansible 
In this project I used flask application with mariaDB database and Nginx webserver.
I used galera cluster for Databases to let the application can use three nodes of mariaDB
I used proxysql as a loadbalancer to achieve high availability to accessing databases nodes.

## To run my Ansible project
``` sh 
    $ ansible-playbook -i hosts.txt fullyprojectplay.yml --vault-password-file ~/.passwords/vault-pass 
```
## Accessing flask application with browser
![Page 1](./imgs/page1.png)

## DataBase on three db servers 
![Db](./imgs/db.png)

## Load Balancer 
![Lb](./imgs/lb.png)

## Connection to data base by load balancer (proxysql)
![Db_connection](./imgs/db_connection.png)

## New item has been added from browser 
![New_item](./imgs/new_item.png)

## Two database servers down and 2 items have been removed from database 
![Db_servers_down](./imgs/db_servers_down.png)

## Restart the db servers to be online and check if it read the change in the items
![db_restarted](./imgs/db_restarted.png)

## Ownership
![Radwan Maazon](images/Radwan1.jpg)|
|:-----------------:|
|[Radwan Maazon](https://github.com/redwan2050)|

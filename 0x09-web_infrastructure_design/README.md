### THE PROJECT DIAGRAMS WILL TRY TO ILLUSRATE:

## FILE  "0-simple_web_stack":
<li>   What is a server
    What is the role of the domain name
    What type of DNS record www is in www.foobar.com
    What is the role of the web server
    What is the role of the application server
    What is the role of the database
    What is the server using to communicate with the computer of the user requesting the website </li>
 

## FILE "1-distributed_web_infrastructure":
<li>    What distribution algorithm your load balancer is configured with and how it works
    Is your load-balancer enabling an Active-Active or Active-Passive setup, explain the difference between both
    How a database Primary-Replica (Master-Slave) cluster works
    What is the difference between the Primary node and the Replica node in regard to the application</li>


## FILE "2-secured_and_monitored_web_infrastructure":
<li>    What are firewalls for
    Why is the traffic served over HTTPS
    What monitoring is used for
    How the monitoring tool is collecting data
    Explain what to do if you want to monitor your web server QPS

    Why terminating SSL at the load balancer level is an issue
    Why having only one MySQL server capable of accepting writes is an issue
    Why having servers with all the same components (database, web server and application server) might be a problem
</li>
# Airflow_Template
Running Airflow in Docker 
follow this Link : https://airflow.apache.org/docs/apache-airflow/stable/howto/docker-compose/index.html
Documentation : https://airflow.apache.org/docs/apache-airflow/1.10.10/start.html

image required
- apache/airflow : https://airflow.apache.org/docs/docker-stack/index.html
- postgres : https://hub.docker.com/_/postgres
- redis : https://hub.docker.com/_/redis

Deployment
1. git pull this repository to server
2. run docker "docker stack deploy"
3. if there is an update code , commit last ver. code to github and git pull on server
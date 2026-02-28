#AI Security Automation  with Wazuh

##Overview 
This project demonstrates an AI-driven security automation architecture integrated with Wazuh SIEM.

The system simulates:
- AI-based alert analysis
- Severity classification
- Automated remediation actions
- Containerized microservice deplyment using Docker

-----
 ## Architecture

Wazuh -> AI Engine -> Remediation Engine 

1. Wazuh detects suspicious activity
2. AI Engine classifies alert severity.
3. Remediation Engine performs automated response.

----

## Technologies used

- Wazuh SIEM
- Docker
- Docker Compose 
- Python 3.10
- Ubuntu Linux

----

## Project Structure 

ai-security-stack/
|
|__docker-compose.yml
|__README.md
|__.gitignore
|__app/
   |__ ai_engine.py
   |__ remediation.py


----

##How to Run

cd ai-security-stack
sudo docker compose up -d

Verify:
sudo docker ps

View logs:
sudo docker logs ai_engine
sudo docker logs remediation_engine

----

## Features
- Containerized AI microservices
- Continuous alert monitoring
- Automated remediation simulation
- Docker network isolation

----



## Authore
Devapriya Shyam

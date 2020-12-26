## -- Origin Image
FROM python:alpine

## -- Install Dependencies
RUN apk add --no-cache ansible

## -- Define Work-Directory
WORKDIR /usr/local/ansible

## -- Copy Playbook and Ansible Config
COPY ../ansible.cfg .
COPY ../playbook.yml .

## -- Playbook Entrypoint
CMD ["ansible-playbook", "./playbook.yml"]

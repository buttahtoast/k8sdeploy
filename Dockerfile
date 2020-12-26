## -- Origin Image
FROM python:alpine

## -- Environment
ENV HELM_VERSION "3.0.0"

## -- Install Dependencies
RUN apk add --no-cache curl jq bash ansible kubectl \
  && curl -s -L -o /usr/local/bin/ejson "https://github.com/Shopify/ejson/releases/download/$(curl --silent "https://api.github.com/repos/Shopify/ejson/releases/latest" | jq -r .tag_name)/linux-amd64" \
  && curl -s -L -o /usr/local/bin/spruce "https://github.com/geofffranks/spruce/releases/download/$(curl --silent "https://api.github.com/repos/geofffranks/spruce/releases/latest" | jq -r .tag_name)/spruce-linux-amd64" \
  && curl -s -L -o /usr/local/bin/reckoner "https://github.com/FairwindsOps/reckoner/releases/download/$(curl --silent "https://api.github.com/repos/FairwindsOps/reckoner/releases/latest" | jq -r .tag_name)/reckoner-linux-amd64" \
  && curl -s "https://get.helm.sh/helm-${HELM_VERSION}-amd64.tar.gz" | tar zx && mv linux-amd64/helm "/usr/local/bin/helm" \
  && chmod +x "/usr/local/bin/*"


## -- Define Work-Directory
WORKDIR /usr/local/ansible

## -- Copy Playbook and Ansible Config
COPY ansible.cfg .
COPY playbook.yml .
COPY example .

## -- Playbook Entrypoint
ENTRYPOINT ["ansible-playbook", "./playbook.yml"]

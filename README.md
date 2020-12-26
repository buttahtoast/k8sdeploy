# K8s-Deployment

**NOT UNDER DEVELOPMENT! WAS JUST AN EXPERIMENT** :D

With this Ansible Playbook you can deploy multiple Charts across multiple Clusters over different Stages. Ansible was Mainly used for it's merging functionality to merge accross different Stages. For the actual Deployment of the Charts we choose [Reckoner](https://github.com/FairwindsOps/reckoner). This Playbook acts as bridge between merging the Values and creating a valid Reckoner Deployment. See below how it works.

# Run the Playbook

All tasks are made locally. So that means there's just a playbook for the current stage, you want to deploy required. Sample Inventory for a stage called `dev`:

```
[dev]
localhost              ansible_connection=local
```

Then run the playbook with this inventory and limit the execution to the given stage:

```

```



```
ansible-playbook playbook.yml -i inventory.py -e "sub_dir=example" -e "ejson_privkey=b9f24a02dabd1f05c327c51a88f99390dab0835f0e56d4766885648cda2a51d6"

```

# Structure a Deployment

Pleases follow the following

## Basic Structure



## Merging & Secrets


### Working with EJSON


## Configuration


### Remote Variables

It's supported, that you use remote variables. By this we mean, that you can reference public files/repositories, which can be merged to the data structure of the Directory you are deploying in. The source can be formatted in JSON or YAML, it doesn't matter. Currently you can't reference EJSON Secrets in remote files.

#### Public Files


#### Git Repositories



#### Example

Let's say we have repositories, which are all the same for our Application Deployments.

**all.yml**
```
---
deploy:
  ## -- Create remote Reference
  remote:

    # -- Example: Define a file which can be downloaded through the get_url module (public available)
    - name: "repositories"
      url: "https://somewhereintheinternet/repositories.yml"
```

Now on the Development Stage we just want to reference one of the repositories from the remote file:

**group_vars/dev.yml**
```
deploy:
  reckoner:
    charts:
      someChart:
        ...
        repository: "stable"
```

The content of the remote file looks like this:

**https://somewhereintheinternet/repositories.yml**
```
---
REPOSITORIES:
  stable:
    url: https://kubernetes-charts.storage.googleapis.com
  incubator:
    url: https://kubernetes-charts-incubator.storage.googleapis.com
```


### Clusters













###







## Requirements

The following binaries are required for this playbook to run properly:

  * [EJSON Merger](https://gitlab.com/kubernetli/scripts/ejson-merger)
    * [Spruce](https://github.com/geofffranks/spruce)
    * [Ejson](https://github.com/Shopify/ejson)
    * [JQ](https://stedolan.github.io/jq/)
  * [Helm](https://helm.sh/docs/intro/install/)
  * [Kubectl](https://kubernetes.io/de/docs/reference/kubectl/)

Make sure before you run that playbook, that these are installed.

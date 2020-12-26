# Clusters

A list of clusters is required for a Deployment to work properly.


## Basic Structure

The basic structure looks like the following example. On the top level of your yaml structure is a key <code>clusters</code> required, which is a yaml array containing atleast one element (one cluster definition):

<pre><code>clusters:

  - name: "kubernetes-admin@kubernetli"
    type: "local"
    # decrypt: "secret"
    options:
      path: "kubeconfigs/kubeconfig.enc"

  - name: "my-custom-cluster"
    type: "local"
    # context: "kubernetes-admin@k8s-dev-cluster"
    decrypt:
      enabled: true
      key: "secret"
      type: "openssl"
    options:
      path: "kubeconfigs/kubeconfig.enc"


  ## -- Remote Kubeconfig Reference
  # Note: The name of the object has to match the name
  # in the reference kubectl Konfiguration
  #- name: "kubernetes-admin@kubernetli"
  #  kubeconfig:
  #    type: "url"
  #    decrypt: "test"
  #    options:
  #      url: "https://minio.kubernetli.ch/kubernetes/test-kubernetli/master/kubeconfig.tar.7z"
  #      ## --- Authentication for get_url (Optional)
  #      auth:
  #        user: "test"
  #        password: "test"



## Supported Keys

The following options are currently supported to declare a cluster:

| **key**  | **Description**  | **Default** | **Required** |
|:---|:---|:---|:---|
| `name` | Defines a unique name for the cluster. It's recommended to use the cluster-context as name. | `{}` | yes |
| `decrypt` | It's expected for | |
| `context` | Declare a specific kubernetes-context for the referenced kubeconfig. If this field is not declared, the name of the element will be used as context. | `{}` | no |
| `type` | Defines how to kubeconfig is stored. See each type below for further configuration possibilities | `{}` | `no` |

The named keys look like this as example for one cluster element:

<pre><code>clusters:

- name: "my-custom-cluster"
  type: "local"
  context: "kubernetes-admin@k8s-dev-cluster"
  options:
    path: "kubeconfigs/kubeconfig.enc"</code></pre>

### Options

As seen in the above example there are more options available under the options key.

| **key**  | **Description**  | **Default** | **Required** |
|:---|:---|:---|:---|
| `options.decrypt.disabled` | By default it's expected, that your kubeconfig is encrypted with openssl (Since we like security). If you wish to skip decryption process, since the referenced kubeconfig is in plaintext, you can set this option to `true`. | `{}` | no |
| `options.decrypt.key` | It's expected for | |
| `type` | Defines how to kubeconfig is stored. See each type below for further configuration possibilities | `{}` | `no` |














### Type 'local'

When a cluster is declared as type <code>local</code> it is expected to get a path to a local encrypted kubeconfig file.



#### Options





### Type 'url'


## Kubeconfig


### Openssl En-/Decryption

# kvs3

kvs3 is a tool for managing environment configuration values. It is intended for use with aws environments and uses an s3  
bucket as a general key/value store.  

## Installing

```bash
$ pip install kvs3
```

## Authenticating

`kvs3` assumes running in an environment with an authenticated AWS user which has the appropriate permission to read/write  
values to an s3 bucket used as the key/value store. Uses boto3 authentication method hierarchy in attempting aws access.   

## Setting up s3

Any s3 bucket can be used, but recommend configuring a bucket with versioning and server-side encryption. Kvs3 will use  
the following sources (in order) to determine the s3 bucket name:  

* `--bucket` flag included in parameters
* shell Environment var `KVS3_BUCKET`
* Run `$ kvs3 init` and provide bucket name. Written to .kvs3 file used by `kvs3` to find bucket

## Usage

### Writing Keys

```bash
$ kvs3 write <service> <key> <value|->
``` 

This command will write a value to a key in s3 under the service path.  

Example:  
```bash
$ kvs3 --bucket my-key-value-store write my-app-env min-nodes 3
```

Will create an object in the s3 bucket named `my-key-value-store` with the name `my-app-env/min-nodes` and the contents `3`.  

### Listing Keys

```bash
$ kvs3 list <service>
KEY           SIZE  MODIFIED
min-nodes     3     2019-06-27 23:37:48
max-nodes     10    2019-06-30 23:28:52
```

`list` will show the key names for a given service, along with other the size in bytes of the value and the date when  
the key was last modified.  

### Reading Keys

```bash
$ kvs3 read <service> <key>
```
<value>  
`read` outputs the value of a single configuration key.  

### Setting shell environment with multiple key values

The setenv command is used as part of a deployment pipeline to setup runtime environment variables for use in a  
deployment pipeline. Create a `keyfile` with a simple list of key values, such as:

```bash
$ cat <<EOF > env.vars
MIN_NODES
MAX_NODES
DOCKER_REGISTRY
```

Now, use setenv to create the output used by `bash source` to define Environment variables.  

```bash
$ kvs3 setenv my-app-env env.vars > local.env
```
Results in local.env containing the following example contents:

```bash
# source my-app-env environment config  
export MIN_NODES=3
export MAX_NODES=5
export DOCKER_REGISTRY=quay.io
```

This file can be used `$source local.env` in a linux environment to create the environment configuration values used  
by a deployment pipeline.  

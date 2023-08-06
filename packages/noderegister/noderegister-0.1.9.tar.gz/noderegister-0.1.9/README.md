![PyPI](https://img.shields.io/pypi/v/noderegiste:r.svg?color=blue&label=pypi%20release)

[![Build Status](https://travis-ci.org/avattathil/noderegister.svg?branch=master)](https://travis-ci.org/avattathil/noderegister)

### noderegister
A Simple tool that registers ec2 host information to a DynamoDB Table

### DDB Content Example

|HOSTNAME                                     | NODE_TYPE  | NODE_STATE | PRIVATE_IP    | TIME_STAMP               |                    
|-------------------------------------------- | ---------- | ---------- | ------------  | ------------------------ |                    
|ip-172-31-36-196.us-west-2.compute.internal  |seednode    | Running    | 172.31.36.196 | Tue Jul  2 20:09:11 2019 |
|ip-172-31-36-197.us-west-2.compute.internal  |seednode    | Running    | 172.31.36.197 | Tue Jul  2 20:10:11 2019 |
|ip-172-33-36-190.us-west-2.compute.internal  |clusternode | Running    | 172.33.36.190 | Tue Jul  2 20:11:11 2019 |
|ip-172-33-36-191.us-west-2.compute.internal  |clusternode | Running    | 172.33.36.191 | Tue Jul  2 20:12:11 2019 | 
|ip-172-33-36-192.us-west-2.compute.internal  |clusternode | Running    | 172.33.36.192 | Tue Jul  2 20:13:11 2019 |

 ![PyPI - Python Version](https://img.shields.io/pypi/pyversions/noderegister.svg?label=Supported%20Python%20Versions&style=for-the-badge)

### Useage

# noderegister
```
usage: noderegister [-h] [-c] [-a ASSIGN | -s SET_STATE | -r | -l]
                    [-D DYNAMODB_TABLE]

optional arguments:
  -h, --help            show this help message and exit
  -c, --create_ddb      Create a new DynamoDB table

actions:
  -a ASSIGN, --assign ASSIGN
                        Set the node type of an existing node
  -s SET_STATE, --set_state SET_STATE
                        Set the node state of an existing node
                        (running|terminated)
  -r, --register_node   Add a new node to the DynamoDB table
  -l, --list            List Registered Node in given DynamoDB Table

required:
  for (assign|state|list|register_node) actions

  -D DYNAMODB_TABLE, --dynamodb_table DYNAMODB_TABLE
                        Name of Existing DynamoDB

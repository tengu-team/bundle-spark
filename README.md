# Spark Bundle

### Overview
![schema](https://github.com/Qrama/spark-bundle/blob/master/schema.png?raw=true)

This repository contains the necessary jobs and Notebook to deploy a spark bundle.
The bundle contains the following services:

#### Spark

- Spark is running with 2 spark jobs
  - ![getdata](https://github.com/Qrama/spark-bundle/blob/master/jobs/writedata.py)
  - ![validatedata](https://github.com/Qrama/spark-bundle/blob/master/jobs/transformdata.py)
- => SparkUI can be accessed on `http://url:4040`

#### Hadoop
- Hadoop is running and has a relationship with Zeppelin. In this way Zeppelin can use HDFS to store data.
- The hadoop service consists of:
    - Hadoop namenode
    - Hadoop resourcemanager
    - 1 hadoop slave
    
#### Zeppelin
- Zeppelin Notebook has a relation with spark and Hadoop. There is 1 Notebook available that will retrieve data from your hdfs and makes it possible to query the data. The notebook is called `Tengu-notebook`
- => Zeppelin can be accessed on `http://url:9080`

### usage
- this bundle can be deployed in your juju environment by cloning this repo and clone the required charms that are not avilable on the juju charm store. to deploy this bundle use:

```
juju deploy /path/to/bundle.yaml
```

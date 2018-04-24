## Workspace Components

![schema](https://github.com/Qrama/spark-bundle/blob/master/schema.png?raw=true)

This repository contains the necessary jobs and Notebook to deploy a spark bundle.
The bundle contains the following services:

### Spark
Apache Spark is a fast and general purpose engine for large-scale data processing. Learn more at spark.apache.org

- Spark is running with 2 spark jobs
  - ![getdata](https://github.com/Qrama/spark-bundle/blob/master/jobs/writedata.py)
  - ![validatedata](https://github.com/Qrama/spark-bundle/blob/master/jobs/transformdata.py)
- => SparkUI can be accessed on `http://url:4040`

### Hadoop
The Apache Hadoop software library is a framework that allows for the distributed processing of large data sets across clusters of computers using simple programming models. It is designed to scale up from single servers to thousands of machines, each offering local computation and storage. Rather than rely on hardware to deliver high-availability, the library itself is designed to detect and handle failures at the application layer, so delivering a highly-available service on top of a cluster of computers, each of which may be prone to failures.

- Hadoop is running and has a relationship with Zeppelin. In this way Zeppelin can use HDFS to store data.
- The hadoop service consists of:
    - Hadoop namenode
    - Hadoop resourcemanager
    - 1 hadoop slave
    
### Zeppelin
Apache Zeppelin is a web-based notebook that enables interactive data analytics. You can make beautiful data-driven, interactive, and collaborative documents with SQL, Scala and more

- Zeppelin Notebook has a relation with spark and Hadoop. There is 1 Notebook available that will retrieve data from your hdfs and makes it possible to query the data. The notebook is called `Tengu-notebook`
- => Zeppelin can be accessed on `http://url:9080`

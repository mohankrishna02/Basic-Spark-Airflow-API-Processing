# Basic Spark Airflow API Processing :-

### Overview :- 
This project demonstrates a basic data pipeline that reads data from an API, processes it using Apache Spark, and stores the processed data into a local file system. The entire workflow is orchestrated using Apache Airflow.
!["visualization"](https://github.com/mohankrishna02/Basic-Spark-Airflow-API-Processing/blob/main/images/api%20airflow.png "Optional Title")


### Technologies Used :- 
* Python
* Apache Spark
* Apache Airflow

### Files :-
* Spark Script :- [Click Here](https://github.com/mohankrishna02/Basic-Spark-Airflow-API-Processing/blob/main/api_processing.py) <br>
* DAG :- [Click Here](https://github.com/mohankrishna02/Basic-Spark-Airflow-API-Processing/blob/main/api_processing_dag.py)

### Setup :-
* Install the Apache Airflow make sure that you have Python & Pyspark in your environment.
* Clone this repository
  ```
  git clone https://github.com/mohankrishna02/Basic-Spark-Airflow-API-Processing.git
  ```
* Place the Pyspark file in any folder and place the DAG file in the Airflow DAG home directory, you will find that directory path in `airflow.cfg` file.

### Running the Pipeline :-
* Start the Airflow
  ```
  airflow webserver -p 8080
  airflow scheduler
  ```
* Trigger the DAG via Airflow UI or CLI

!["visualization"](https://github.com/mohankrishna02/Basic-Spark-Airflow-API-Processing/blob/main/images/DAG-RUNNING.png "Optional Title")

!["visualization"](https://github.com/mohankrishna02/Basic-Spark-Airflow-API-Processing/blob/main/images/DAG-SUCCESS.png "Optional Title")

### Documentation :-
* Python :- [Click Here](https://docs.python.org/3.12/tutorial/index.html) <br>
* Pyspark :- [Click Here](https://spark.apache.org/docs/latest/api/python/index.html) <br>
* Apache Airflow :- [Click Here](https://airflow.apache.org/docs/apache-airflow/stable/tutorial/fundamentals.html)

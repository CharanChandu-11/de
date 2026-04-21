hive
CREATE DATABASE company;
USE company;

CREATE TABLE emp (
    id INT,
    name STRING,
    salary FLOAT
)
ROW FORMAT DELIMITED
FIELDS TERMINATED BY ',';

LOAD DATA LOCAL INPATH '/user/hive/empdata.txt' INTO TABLE emp;   

SELECT * FROM emp;

DESCRIBE emp;


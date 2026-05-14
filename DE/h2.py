hdfs dfs -cat /lab1/input/file.txt

hdfs dfs -cp /lab1/input/file.txt /lab1/input/file_copy.txt

hdfs dfs -ls /lab1/input/

hdfs dfs -cat /lab1/input/file_copy.txt

########

hdfs dfs -mkdir /input
nano input.txt (enter file content)
hdfs dfs -put input.txt /input
hadoop jar /usr/lib/hadoop-mapreduce/hadoop-mapreduce-examples.jar wordcount /input /output
hdfs dfs -ls output   
hdfs dfs -cat /output/part-r-00000
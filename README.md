# Hadoop data analysis
*Use Map-Reduce with streaming API to process data file (in csv format) on a hadoop cluster*

### To run the map-reduce job:
- Clone repo
- Execute: ```$ hadoop jar /usr/hdp/current/hadoop-mapreduce-client/hadoop-streaming.jar -file <path to mapper.py> -mapper <path to mapper.py> -file <path to reducer.py> -reducer <path to reducer.py> -input /user/tatavag/nyc.data -output /tmp/outputmehravr```
- View output file generated for statistics summary

### Description

- **Mapper**: From each line in data file, extracts upto five vehicle types (if present), through means of a regex
- **Reducer**: Sums count of all similar vehicle types and prints output to file

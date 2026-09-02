# Lab 2 - URL Count Solution

## Solution

I implemented the URL counter using Python and the Hadoop Streaming API.

The mapper, `URLMapper.py`, reads the input one line at a time and uses the regular expression:

`href="([^"]*)"`

to extract all URLs from each line. Since a line can contain multiple URLs, `findall()` is used to capture every match. For each URL found, the mapper outputs the URL as the key and `1` as the value.

The reducer, `URLReducer.py`, receives the URL records after Hadoop sorts and groups them by key. It sums the counts for each URL and only outputs URLs whose total count is greater than 5.

## Software / Environment

- Python 3
- Hadoop 3.3.6
- Hadoop Streaming
- HDFS
- Google Cloud Dataproc
- CSEL programming environment
- Git and GitHub

The solution was first developed and tested on CSEL. It was then executed on a multi-node Google Cloud Dataproc cluster using Hadoop Streaming.

## CSEL Testing

The mapper and reducer were first tested locally using:

`cat input/file01 input/file02 | python3 URLMapper.py | sort | python3 URLReducer.py`

The same program was then executed using Hadoop Streaming on CSEL. The local Python output and Hadoop Streaming output were compared and matched.

## Dataproc Execution Times

### 1 Master + 2 Workers

Execution time:

`real 1m43.784s`

The resulting output contained 10 URLs with counts greater than 5.

### 1 Master + 4 Workers

Execution time:

`real 1m21.735s`

The resulting output also contained the same 10 URLs with counts greater than 5.

## Timing Comparison

The 4-worker cluster completed the job faster than the 2-worker cluster.

However, doubling the number of workers did not cut the execution time in half. The input for this lab is relatively small, so fixed Hadoop overhead such as job initialization, YARN scheduling, mapper/reducer startup, shuffle setup, and task coordination represents a significant portion of the total execution time.

With a much larger dataset, the additional workers would have more useful work to execute in parallel and the performance improvement could be more significant.

Dataproc generated multiple `part-*` reducer output files. Concatenating all of the part files produced the same 10 result lines as the CSEL implementation.

## Resources

Resources used while completing this lab:

- CSCI 5253 Lab 2 README and supplied WordCount example
- Apache Hadoop / Hadoop Streaming documentation
- Google Cloud Dataproc documentation
- ChatGPT for step-by-step setup guidance and troubleshooting

I completed the implementation myself and did not work with another student on the code.

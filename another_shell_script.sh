#!/bin/bash
for i in {1..100}
do
   echo "Welcome $i times"
   curl -X GET   https://jsonplaceholder.typicode.com/posts/$i -H 'cache-control: no-cache'   -H 'content-type: application/json'
done

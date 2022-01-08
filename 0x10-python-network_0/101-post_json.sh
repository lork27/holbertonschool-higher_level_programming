#!/bin/bash
#display body of the get response
curl -s -H 'Content-Type: application/json' -d $2 $1

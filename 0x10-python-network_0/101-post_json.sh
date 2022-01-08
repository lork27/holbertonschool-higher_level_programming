#!/bin/bash
#display body of the get response
curl -s -X POST $2 -H 'Content-Type: application/json' -d $1

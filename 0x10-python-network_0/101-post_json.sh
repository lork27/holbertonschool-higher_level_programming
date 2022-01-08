#!/bin/bash
#display body of the get response
curl -s -X POST $1 -H 'Content-Type: application/json' -d "$2"

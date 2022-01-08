#!/bin/bash
#display body of the get response
curl -o /dev/null -s -w "%{http_code}" $1

#!/bin/bash
#display body of the get response
curl -0 /dev/null -s -w "%{http_codew}" $1

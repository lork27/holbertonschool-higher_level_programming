#!/bin/bash
#display body of the get response
curl -s "$1" -i | grep "Allow" | cut -d ' ' -f 2-

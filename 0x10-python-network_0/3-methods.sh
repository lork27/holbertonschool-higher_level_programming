#!/bin/bash
#display body of the get response
curl -s -X OPTION "$1" -i | grep "Allow" | cut -d ' ' -f 2-

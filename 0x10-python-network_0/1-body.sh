#!/usr/bin/bash
#display body of the get response
curl -s -w "\n%{http_code}" '$1'

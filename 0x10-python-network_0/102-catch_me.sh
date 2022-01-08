#!/bin/bash
#display body of the get response
curl -sL 0.0.0.0:5000/catch_me -X PUT -d "user_id=98" -H "Origin: HolbertonSchool"

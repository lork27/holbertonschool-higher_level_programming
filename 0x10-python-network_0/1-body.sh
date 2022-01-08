#!/usr/bin/bash
#display body of the get response
curl -s -w "\n%{http_code}" 'https://swapi.co/api/people/1/?format=json' | {
    read body
    read code
    echo $code
    jq .name <<< "$body"
}

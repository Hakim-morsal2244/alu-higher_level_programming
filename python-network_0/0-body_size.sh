#!/bin/bash
# Script to get the size of the body of the response from a URL
curl -s "$1" | wc -c

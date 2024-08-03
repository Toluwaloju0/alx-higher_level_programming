#!/bin/bash
# A script that show the methods a url allows
curl -s --request OPTIONS "$1"

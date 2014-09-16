#! /bin/env bash

echo $1
gulp dist
git add .
git commit -m "$1"
git push heroku master

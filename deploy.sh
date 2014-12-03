#! /bin/env bash

if [ "$#" -ne 2 ]; then
    echo "Usage: <production|staging> <commit message> [--no-dist]"
    exit 1
fi

echo ">>>> Env: $1"
echo ">>>> Message: $2"

if echo $* | grep -e "--no-dist" -q
then
  echo ">>>> Skipping Dist step"
else
  gulp dist
  git add .
  git commit -m "$1: $2"
fi

if [ "$1" -eq "production" ]
then
    git push heroku production:master
    APP=magnovite
else
    git push staging staging:master
    APP=magnovite-staging
fi

echo ">>>> Migrationg heroku app $APP"
heroku run ./manage.py migrate --app="$APP"

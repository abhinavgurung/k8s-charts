#!/bin/sh

environment=$PORTAL_ENV
env=$(echo $environment | cut -d'-' -f1)
channel=$(echo $environment | cut -d'-' -f2)

if [[ "$channel" = "release" ]] ;
then
  echo "Deploying to release channel..." ;
  if [[ "$env" = "Development" ]] ;
  then
    cp -a /app-dev-release/. /usr/share/nginx/html ;
    echo "Copied DEVELOPMENT (release channel) environment app files to nginx folder." ;
  elif [[ "$env" = "Test" ]] ;
    then
    cp -a /app-test-release/. /usr/share/nginx/html ;
    echo "Copied TEST (release channel) environment app files to nginx folder." ;
  elif [[ "$env" = "Production" ]] ;
    then
    cp -a /app-prod-release/. /usr/share/nginx/html ;
    echo "Copied PRODUCTION (release channel) environment app files nginx folder." ;
  else
    cp -a /app-dev-release/. /usr/share/nginx/html ;
    echo "Copied DEVELOPMENT (release channel) environment app files (default - no PORTAL_ENV provided) files to nginx folder." ;
  fi
else
  echo "Deploying to development channel..." ;
  if [[ "$env" = "Development" ]] ;
  then
    cp -a /app-dev/. /usr/share/nginx/html ;
    echo "Copied DEVELOPMENT environment app files to nginx folder." ;
  elif [[ "$env" = "Test" ]] ;
    then
    cp -a /app-test/. /usr/share/nginx/html ;
    echo "Copied TEST environment app files to nginx folder." ;
  elif [[ "$env" = "Production" ]] ;
    then
    cp -a /app-prod/. /usr/share/nginx/html ;
    echo "Copied PRODUCTION environment app files nginx folder." ;
  else
    cp -a /app-dev/. /usr/share/nginx/html ;
    echo "Copied DEVELOPMENT environment app files (default - no PORTAL_ENV provided) files to nginx folder." ;
  fi
fi

nginx -g 'daemon off;'

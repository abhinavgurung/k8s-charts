#!/bin/sh

environment=$PORTAL_ENV
env=$(echo $environment | cut -d'-' -f1)
channel=$(echo $environment | cut -d'-' -f2)

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

nginx -g 'daemon off;'

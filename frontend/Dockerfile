FROM node:16.15.0-alpine3.15

# Set the working directory
WORKDIR /app

# Copy the project files to the container
COPY . /app

# Update OS package index and update packages to latest versions.
RUN apk update && apk upgrade

# Update NPM
RUN npm install -g npm@8.19.4

# Install node dependencies
RUN npm install

# start app
CMD ["npm" , "start"]

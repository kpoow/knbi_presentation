FROM node:16

WORKDIR /app

# install app dependencies
COPY package.json ./
COPY package-lock.json ./

# add app
COPY ./ ./

# start app
RUN npm i
CMD ["npm", "run", "start"]
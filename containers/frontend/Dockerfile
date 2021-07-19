FROM node:14.17.3 AS build

WORKDIR /app

ENV PATH /app/node_modules/.bin:$PATH

COPY package.json ./
COPY package-lock.json ./

RUN npm ci
RUN npm install react-scripts@3.4.0 -g

COPY . ./

RUN npm run build
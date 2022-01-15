FROM node:current-alpine
WORKDIR /data/frontend
COPY ["package.json", "package-lock.json*", "./"]
COPY . .
RUN npm install --NODE_ENV
RUN npm install -g @angular/cli

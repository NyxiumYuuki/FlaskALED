FROM node:current-slim
WORKDIR /data/frontend
COPY ["package.json", "package-lock.json*", "./"]
RUN npm install --NODE_ENV
RUN npm install -g @angular/cli
COPY . .

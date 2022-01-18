FROM node:current-slim
WORKDIR /data/frontend
COPY ["package.json", "package-lock.json*", "./"]
RUN npm install -g npm@8.3.1
RUN npm install --NODE_ENV
RUN npm install -g @angular/cli
COPY . .

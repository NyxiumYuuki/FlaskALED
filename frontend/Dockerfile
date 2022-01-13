FROM node:current-alpine
WORKDIR /data/frontend
COPY ["package.json", "package-lock.json*", "./"]
COPY . .
RUN apk add --no-cache gettext
#RUN envsubst < environments/environment.ts > environments/environment.ts
RUN npm install --NODE_ENV
RUN npm install -g @angular/cli

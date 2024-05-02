# build environment
FROM node:slim as build
WORKDIR /app
COPY package.json .
COPY package-lock.json .
RUN npm install
COPY . .
EXPOSE 3000
CMD ["npm", "start"]

# RUN npm install serve -g
# RUN npm run build
# CMD ["serve", "-s","build"]
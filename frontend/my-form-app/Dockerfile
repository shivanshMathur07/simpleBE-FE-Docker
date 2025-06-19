FROM node:alpine3.22
WORKDIR /app
COPY ./ /app
RUN npm install
ENTRYPOINT ["npm", "run"]
CMD ["dev"]
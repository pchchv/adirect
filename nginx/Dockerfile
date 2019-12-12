FROM nginx
#COPY nginx.conf /etc/nginx/nginx.conf
#RUN rm /etc/nginx/conf.d/default.conf
WORKDIR /app

ADD . /app

EXPOSE 80:80

CMD ["nginx", "-g", "daemon off;"]

#FROM nginx

#RUN rm /etc/nginx/conf.d/default.conf

#COPY nginx.conf /etc/nginx/cinf.d/

FROM nginx:stable-alpine
COPY ./nginx.conf /etc/nginx/nginx.conf
COPY ./sites-enabled /etc/nginx/sites-enabled
COPY ./proxy_params /etc/nginx/proxy_params
EXPOSE 80

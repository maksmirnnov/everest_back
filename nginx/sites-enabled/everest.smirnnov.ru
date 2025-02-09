upstream gunicorn_server {
    server everest_back:8000 fail_timeout=0;
}

server {
    listen 80 default_server;
    listen [::]:80 default_server ipv6only=on;

    server_name localhost;
    
    keepalive_timeout 5;

    location / {
        proxy_pass      http://gunicorn_server/;
        include         proxy_params;
        # proxy_redirect  off;
    }

    location /static {
        alias           /etc/nginx/static;
    }

    location /assets {
        alias           /etc/nginx/static;
    }
}

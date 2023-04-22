server {
    listen 81;
    server_name www.admin.trustcenterholding.com 95.216.165.58 admin.trustcenterholding.com localhost;

    location /static {
        alias /vol/static;
    }

    location / {
        uwsgi_pass              ${APP_HOST}:${APP_PORT};
        include                 /etc/nginx/uwsgi_params;
        client_max_body_size    10M;
    }
}


# Dockerfile for nginx
FROM nginx

# Override the default nginx configuration file
RUN rm /etc/nginx/conf.d/default.conf

COPY nginx.conf /etc/nginx/conf.d/default.conf
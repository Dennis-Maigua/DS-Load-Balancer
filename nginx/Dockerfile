# Dockerfile for nginx
FROM nginx

# Remove the default nginx config
RUN rm /etc/nginx/conf.d/default.conf

# Copy the new config file to the nginx directory
COPY nginx.conf /etc/nginx/conf.d/default.conf
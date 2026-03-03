# We use the official image - it already has all extensions (gd, mysqli, etc.) installed
FROM wordpress:php8.3-apache

# All we need to do is add your custom 1GB limits
COPY uploads.ini /usr/local/etc/php/conf.d/uploads.ini

# health check for kamal proxy
COPY up.php /var/www/html/up.php

# The official image already handles EXPOSE 80 and the CMD to start Apache
# We don't even need to copy the WordPress files; they are already in /var/www/html

#!/bin/bash

# Define MySQL user and password
MYSQL_USER="root"  # Use 'root' or another admin user
MYSQL_PASSWORD="your_mysql_root_password"

# List privileges for user_0d_1
echo "Listing privileges for user_0d_1:"
mysql -u "$MYSQL_USER" -p"$MYSQL_PASSWORD" -e "SHOW GRANTS FOR 'user_0d_1'@'localhost';"

# List privileges for user_0d_2
echo "Listing privileges for user_0d_2:"
mysql -u "$MYSQL_USER" -p"$MYSQL_PASSWORD" -e "SHOW GRANTS FOR 'user_0d_2'@'localhost';"

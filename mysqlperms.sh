#!/bin/bash

echo "is this a new user? y/n: " && read new
if [ $new = y ]
        then
                echo "what would you like to call the user?" && read name
                echo "Users password: " && read -s password
else
                echo "which user?"
                echo "select User from mysql.user;"|mysql -uroot -psyst3mp4ss && read name
                echo "Users password: " && read -s password
fi

echo "which Database would you like to give the user permissions to?" && mysqlshow -uroot -psyst3mp4ss && read database
echo "any particular table?(Use * for all)" && read table
echo "Granting privileges for $name to $database..."


echo "GRANT SELECT, INSERT, UPDATE, DELETE, CREATE, DROP, INDEX, ALTER, LOCK TABLES, CREATE TEMPORARY TABLES ON $database.$table TO $name@localhost IDENTIFIED BY \"$password\";" |mysql -uroot -psyst3mp4ss


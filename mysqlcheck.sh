#!/bin/bash
PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin

(
echo "show slave status \G"
) |mysql -u root -psyst3mp4ss 2>&1 |grep -q "Slave_IO_Running: Yes"
if [ "$?" -ne "1" ] ; then
echo "0:000:MySQL Replication was successful"
else
echo "2:200:MySQL Replication has failed"
fi

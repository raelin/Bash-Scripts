#!/bin/bash

#creates the windows server variable
echo "what is the server hosting the share?"
read server

#creates the share variable
echo "what is the share?"
read share
#the windows server share variable, uses each variable and combines them
winserver=\/\/$server\/$share

# the user account with permission to the share.
echo "which user are you using to access the share?"
read user
#the password to the user
echo "password:"
# read -s forces the terminal to not output the stdin AKA you can't see the password as you're typing it.
read -s password

#creates the variable to find where the mount is to be placed.
echo "where do you want it mounted? (full directory please)"
read mountpoint

what kind of file system is it?
echo "what form of file system is it? (E.g. ext4, ntfs, cifs, nfs)"
read fstype

# if CIFS share, make fsreal varible = cifs and continue
if [ "$fstype" = "cifs" ]
then
fsreal=cifs

#else if NFS share, make fsreal variable = nfs and continue
elif [ "$fstype" = "nfs" ]
then
fsreal=nfs
# else if ext4 partition make fsreal variable = ext4 and continue
elif [ "$fstype" = "ext4" ]
then
fsreal=ext4

#else echo the invalid filesystem error and exit
else
echo "Invalid Filesystem type"
exit 0
fi

#append the string created from the variables to the end of the /etc/fstab file,
echo "$winserver $mountpoint $fsreal gid=users filmode=0655 dir_mode=0775 auto username=$user password=$password 0 0" >> /etc/fstab

#now mount the mountpoint without a restart
mount -o remount "$mountpoint"

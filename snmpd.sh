#!/bin/bash
## Written, Tested and Approved by Matthew Vogel 7/03/2014
## Any questions please read the OneNote article in relation to this script
## Please avoid any modifications to this script, if you require to make modifications
## please create a .sh file and copy the script into it. modifying this script will cause some issues with data and/or case structure.

PS3="Please enter your choice: "
options=("POLARIS" "PIPE" "CANBERRA" "QUIT")
name=""
if [ -a '/etc/snmp/snmpd.conf' ]
        then
                echo "snmpd.conf exists, please remove and try again"
                exit
fi

echo "What is your name:"
read $name
select VAR in "${options[@]}";
do
        case "$VAR" in
                "POLARIS")
                        echo "creating polaris SNMP config"
                        touch /etc/snmp/snmpd.conf
                        echo "rocommunity emantra 127.0.0.1" >> /etc/snmp/snmpd.conf
                        echo "rocommunity emantra 10.10.10.16" >> /etc/snmp/snmpd.conf
                        echo "syslocation Polaris" >> /etc/snmp/snmpd.conf
                        echo "syscontact $name" >> /etc/snmp/snmpd.conf
                        break
                        ;;
                "PIPE")
                        echo "creating pipe SNMP config"
                        touch /etc/snmp/snmpd.conf
                        echo "rocommunity emantra 127.0.0.1" >> /etc/snmp/snmpd.conf
                        echo "rocommunity emantra 10.11.10.12" >> /etc/snmp/snmpd.conf
                        echo "syslocation Pipe" >> /etc/snmp/snmpd.conf
                        echo "syscontact $name" >> /etc/snmp/snmpd.conf
                        break
                        ;;
                "CANBERRA")
                        echo "creating Canberra SNMP config"
                        touch /etc/snmp/snmpd.conf
                        echo "rocommunity emantra 127.0.0.1" >> /etc/snmp/snmpd.conf
                        echo "rocommunity emantra 10.50.10.30" >> /etc/snmp/snmpd.conf
                        echo "syslocation Canberra" >> /etc/snmp/snmpd.conf
                        echo "syscontact $name" >> /etc/snmp/snmpd.conf
                        break
                        ;;
                "QUIT")
                        break
                        ;;
                *) echo invalid option
                        ;;
esac
done
exit


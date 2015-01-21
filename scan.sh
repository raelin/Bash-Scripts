#!/bin/bash

echo "ip address please"
read IP

nmap -v -A $IP

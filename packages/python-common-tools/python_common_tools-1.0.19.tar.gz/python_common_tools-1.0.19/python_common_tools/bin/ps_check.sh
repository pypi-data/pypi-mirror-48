#!/usr/bin/env bash

app_name=$1
ps -ef|grep $app_name|grep -v grep
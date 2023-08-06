#!/usr/bin/env bash

cd $PWD
. env/bin/activate

app_name=$1

nohup python $app_name >nohup.$app_name.out 2>&1 &
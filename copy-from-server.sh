#!/bin/zsh

pushd /Users/aaryan/cron
touch err out
date >> err
date >> out
rsync -ra --remove-source-files fruit-brute.cs:/tmp/aprakash/trained_model/ /Users/aaryan/college/fall2023/cs371/hw/final/trained_model/ 2>>err >>out

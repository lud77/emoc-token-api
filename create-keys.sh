#!/bin/bash

if [ -d ./.ssh ]; then
  echo "Keys already exist"
  echo "To create new keys, remove .ssh folder and run again"
  exit
fi

mkdir ./.ssh

ssh-keygen -t rsa -f ./.ssh/id_rsa
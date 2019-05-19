#!/bin/bash
git remote add upstream https://github.com/fengdu78/lihang-code.git 
git remote -v
git fetch upstream
git merge upstream/master
#git log
git push origin master

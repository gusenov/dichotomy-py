#!/bin/bash
set -x  # echo on

# Usage:
#  $ ./commit.sh

git add .
git commit -S -m "Функция-генератор nlr_gen. Классы BinaryTreeList и LevelIterator."
git tag -s v0.1.1 -m 'signed 0.1.1 tag'
git push -u --tags com.github.gusenov.dichotomy-py master:master

#!/bin/bash
set -x  # echo on

# Usage:
#  $ ./publi.sh
#  $ ./publi.sh -r=testpypi -n=dichotomy
#  $ ./publi.sh --repo=pypi --name=dichotomy

repo="testpypi"
package_name="dichotomy"

for i in "$@"
do
case $i in
    -r=*|--repo=*)
        repo="${i#*=}"
        shift # past argument=value
        ;;
    -n=*|--name=*)
        package_name="${i#*=}"
        shift # past argument=value
        ;;
esac
done

read -p "Вы уверены, что хотите провести публикацию $package_name в $repo? [Y/y] " -n 1 -r
echo    # (optional) move to a new line
if [[ $REPLY =~ ^[Yy]$ ]]
then
    pip3 uninstall "$package_name"

    python setup.py sdist upload -r $repo

    if [ "$repo" == "pypi" ]  # https://pypi.org/project/dichotomy/
    then
        pip3 install "$package_name" --user
    elif [ "$repo" == "testpypi" ]  # https://test.pypi.org/project/dichotomy/
    then
        pip3 install --extra-index-url https://testpypi.python.org/pypi "$package_name" --user
    fi

    pip3 list | grep "$package_name"
    ls ~/.local/lib/python*/site-packages/ | grep "$package_name"
fi

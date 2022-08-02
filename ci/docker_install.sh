#!/bin/bash

# We need to install dependencies only for Docker
[[ ! -e /.dockerenv ]] && exit 0

set -xe

export DEBIAN_FRONTEND=noninteractive
apt-get update -yqq
apt-get install git sudo php-xdebug php7.4-sqlite3 php7.4-curl\
    php7.4-xml php7.4-mbstring php7.4-json php7.4-zip php7.4-gd\
    php7.4-intl unzip curl wget nodejs npm sed gpsbabel make rsync composer -yqq > /dev/null 2>&1

curl --location --output /usr/local/bin/phpunit https://phar.phpunit.de/phpunit.phar
chmod +x /usr/local/bin/phpunit


#!/usr/bin/env sh

set -e # На error мы покидаем нашу программу, т.е. когда мы не смогли подключиться к БД

echo "Run apply migrations.."

alembic upgrade head # Через alembic мы будем выполнять миграцию - это команда, которую мы писали бы в терминал - накатить все миграции в БД

echo "Migrations applied"

exec "$@" # Запуск нашего сервиса
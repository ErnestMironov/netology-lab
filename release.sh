#!/bin/sh

# Сначала переключаемся на ветку prd
git checkout prod

# Затем сливаем изменения из ветки dev
git merge dev

# Создаем тег для релиза
git tag -a версия-1.0 -m "Релиз версии 1.0"

# Пушим изменения в ветку prd и отправляем тег в удаленный репозиторий
git push origin prd --tags

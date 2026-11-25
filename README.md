# Практика: локальный Quality Gate с pre-commit

Небольшой Python-проект для демонстрации автоматических проверок перед
локальным Git-коммитом. В конфигурации запускаются Ruff, Ruff Format и pytest.

## Подготовка

Если проект ещё не является Git-репозиторием, инициализируйте его:

```bash
git init
```

Создайте и активируйте виртуальное окружение:

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
```

Для macOS/Linux команда активации:

```bash
source .venv/bin/activate
```

Установите инструменты и установите Git-хук:

```bash
python -m pip install -r requirements-dev.txt
pre-commit install
```

`pre-commit install` нужно выполнить один раз после клонирования проекта.

## Проверки вручную

```bash
ruff check .
ruff format --check .
pytest
```

## Демонстрация на уроке

1. Убедитесь, что проверки проходят:

   ```bash
   git add .
   git commit -m "Add lesson starter"
   ```

2. В `lesson_app.py` добавьте неиспользуемый `import os` и намеренно нарушьте
   форматирование, например измените отступы или пробелы.
3. Добавьте изменения и попробуйте создать коммит:

   ```bash
   git add lesson_app.py
   git commit -m "Demonstrate quality gate"
   ```

4. Ruff исправит часть проблем, но pre-commit остановит коммит, чтобы изменения
   можно было проверить. Посмотрите diff, затем снова добавьте исправленный
   файл и повторите коммит:

   ```bash
   git diff
   git add lesson_app.py
   git commit -m "Demonstrate quality gate"
   ```

Конфигурация хуков находится в `.pre-commit-config.yaml`. `pass_filenames: false`
и `always_run: true` заставляют pytest запускать весь набор тестов при каждом
коммите, а не только файлы, переданные хуку.

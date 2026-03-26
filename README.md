# GitHub EXE Test

Тестовый репозиторий для автоматической сборки Windows EXE через GitHub Actions.

## Как работает

1. Пушишь код в `main`
2. GitHub Actions автоматически:
   - Устанавливает Python
   - Собирает EXE через PyInstaller
   - Создаёт Release с готовым файлом

## Скачать EXE

Идёшь в [Releases](../../releases) → выбираешь последнюю версию → скачиваешь `Hello-GitHub-Actions.exe`

## Структура

```
.
├── .github/workflows/build.yml  # Workflow сборки
├── main.py                      # Исходный код
├── requirements.txt             # Зависимости
└── README.md                    # Этот файл
```

## Ручная сборка локально

```bash
pip install pyinstaller
pyinstaller --onefile main.py
```
# Trigger workflow

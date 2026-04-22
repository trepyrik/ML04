# Vehicle Tracking System

Стартовый каркас проекта для продакшен-системы трекинга автомобилей в городе.

## Что уже есть
- FastAPI API
- заготовка для детектора
- заготовка для трекера
- базовая аналитика пересечения линии
- PostgreSQL + Redis через Docker Compose
- конфиги через `.env`
- структура под дальнейший рост до продакшена

## Быстрый старт

### 1. Создай окружение
```bash
python -m venv .venv
source .venv/bin/activate
```

Windows PowerShell:
```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

### 2. Установи зависимости
```bash
pip install -r requirements.txt
```

### 3. Подними инфраструктуру
```bash
docker compose up -d postgres redis
```

### 4. Запусти API
```bash
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

### 5. Проверь health endpoint
Открой:
- `http://127.0.0.1:8000/health`
- `http://127.0.0.1:8000/docs`

## Ближайшие шаги
1. Подключить реальный детектор авто (YOLO).
2. Подключить ByteTrack/DeepSORT.
3. Сохранять tracks/events в PostgreSQL.
4. Добавить обработку видео и RTSP потоков.
5. Добавить фоновые задачи для длинных jobs.

## Пример структуры
```text
app/
  api/           # HTTP endpoints
  core/          # config, logging, settings
  ingestion/     # чтение видео/RTSP
  detection/     # детекция объектов
  tracking/      # трекинг и track_id
  analytics/     # бизнес-аналитика и события
  storage/       # БД и репозитории
  services/      # orchestration layer
```

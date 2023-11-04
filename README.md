## Elapsed Test

___

### Стек:

- python 3.11
- FastAPI

___
(под Linux)

```Запуск:```

- Создать виртуальное окружение

Пример команды:

```shell
python3.11 -m virtualenv .venv
```

- Запустить виртуальную среду

```shell
source .venv/bin/activate
```

- Установить зависимости из файла req.pip

```shell
pip install -r req.pip
```

- В терминале прописать:

```shell
uvicorn src.main:app --host 0.0.0.0 --port 8000
```

```Запуск тестовых запросов```
```shell
source .venv/bin/activate
python test.py
```
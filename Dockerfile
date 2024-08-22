FROM python:3.10-alpine3.17

# Обновление репозиториев
RUN echo "https://dl-4.alpinelinux.org/alpine/v3.10/main" >> /etc/apk/repositories && \
    echo "https://dl-4.alpinelinux.org/alpine/v3.10/community" >> /etc/apk/repositories

# Установка chromedriver
RUN apk update
RUN apk add --no-cache chromium chromium-chromedriver tzdata

# Установка рабочего каталога
WORKDIR /app

# Копирование файлов
COPY requirements.txt .

#Стоит отметить, что шаг с удалением py-pip на самом деле размер итогового образа не уменьшит,
#ведь каждая команда RUN просто создаёт новый слой. Чтобы избежать этого, стоит объединять операции в RUN через &&.

# Обновление трех пакетов pip, setuptools, wheel.
RUN pip install --upgrade pip setuptools wheel

# Установка зависимостей
RUN pip install -r requirements.txt

# Копирование файлов
# Откуда(имя локальной папки с файлами)/ ./куда(имя папки в контейнере)
COPY tst/ ./tst

# Создание каталога для результатов
RUN mkdir -p allure-results

# Команда для запуска тестов
#                Путь к исполняемому файлу
CMD ["pytest", "tst/tests/test_blazemeter.py", "--alluredir=allure-results"]
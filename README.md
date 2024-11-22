"# library-management-systems" 

## Описание проекта

Это консольное приложение для управления библиотекой книг. Оно позволяет добавлять, удалять, искать и отображать книги. Каждая книга содержит следующие поля:

- `id`: уникальный идентификатор (генерируется автоматически).
- `title`: название книги.
- `author`: автор книги.
- `year`: год издания.
- `status`: статус книги ("в наличии" или "выдана").

## Установка и запуск

1. **Клонируйте репозиторий**:
    ```bash
    git clone https://github.com/A1astorrr/library-management-systems.git
    cd library_management_system
    ```

2. **Создайте виртуальное окружение и активируйте его**:
    ```bash
    python -m venv venv
    source venv/bin/activate  # Для Linux/Mac
    venv\Scripts\activate  # Для Windows
    ```

3. **Установите зависимости**:
    ```bash
    pip install -r requirements.txt
    ```
4. **Создайте файл .env в корне проекта и добавьте настройки базы данных:
   ```bash
   DB_HOST=localhost
   DB_PORT=5432
   DB_NAME=name
   DB_USER=username
   DB_PASS=password
   ```
6.  **Настройте базу данных PostgreSQL**: Убедитесь, что у вас установлен PostgreSQL и создана база данных для вашего приложения.

## Запуск приложения

Запустите приложение с помощью Uvicorn:

```bash
uvicorn app.main:app --host 0.0.0.0 --port 80 --reload

### Краткий отчет о проекте

#### Проектные решения

- **Использование FastAPI**: FastAPI был выбран из-за его высокой производительности и простоты использования, а также из-за автоматической генерации документации API.
  
- **База данных PostgreSQL**: PostgreSQL использовался как реляционная база данных для хранения постов, так как он хорошо интегрируется с SQLAlchemy.

#### Проблемы

- **Типы данных в SQLAlchemy**: При работе с SQLAlchemy возникали проблемы с типами данных, особенно при использовании операторов сравнения в запросах. Это было решено путем тщательной проверки передаваемых параметров.

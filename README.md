# copyright (backend)

![Static Badge](https://img.shields.io/badge/Yamemik-copyright)
![GitHub top language](https://img.shields.io/github/languages/top/Yamemik/copyright)
![GitHub](https://img.shields.io/github/license/Yamemik/copyright)
![GitHub Repo stars](https://img.shields.io/github/stars/Yamemik/copyright)
![GitHub issues](https://img.shields.io/github/issues/Yamemik/copyright)


## Общее описание
_____

### Стек технологий:
  - FastAPI;
  - postgreSQL.

## Техническое описание
_____

### ER-Diagrams
```mermaid
erDiagram
    USER }o--o{ COURSE : used    
    USER {
        int id PK      
        string email "*"
        string hashed_password "*"
        bool is_active
        bool is_superuser
        bool is_verified        
    }
    COURSE {
        int id PK
        string status
        int user_id FK       
    }
```


## Техническое описание
_____

### fastapi
```bash
# запустить сервер
$ uvicorn --factory src.main:create_app --reload
```

## Ссылки
_____
[by Yamemik](https://github.com/Yamemik)

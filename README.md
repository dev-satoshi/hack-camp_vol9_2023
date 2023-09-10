# 【技育CAMP】マンスリーハッカソン vol.9
Frontend https://github.com/SuperUltraTsuyoTsuyoEngineerTeam/oshi-rimind-frontend

### Technology

### ER Diagram

### Directory Configuration

### Development

デフォルトのDjango開発サーバを使用します

1. docker-compose.ymlおよび.env.devファイル内の環境変数を更新します
2. イメージをビルドし、コンテナーを実行します

```sh
$ docker-compose up -d --build
```

[http://localhost:8000](http://localhost:8000)でテストしてください<br>

### Production

Gunicornを使用します

1. docker-compose.prod.yml、.env.prod、.env.prod.dbファイル内の環境変数を更新します
2. イメージをビルドし、コンテナーを実行します

```sh
$ docker-compose -f docker-compose.prod.yml up -d --build
```

[http://localhost:1337](http://localhost:1337)でテストしてください<br>

### environmental variables

.env.dev
```
DEBUG=1
SECRET_KEY=change_me
DJANGO_ALLOWED_HOSTS=localhost 127.0.0.1 [::1]
CORS_ALLOW_ALL_ORIGINS=True
SQL_ENGINE=django.db.backends.postgresql
SQL_DATABASE=sample_db_dev
SQL_USER=admin
SQL_PASSWORD=password
SQL_HOST=db
SQL_PORT=5432
DATABASE=postgres
OpenAI_API_Key=chang_me
```

### API Document
[http://localhost:8000/api/schema/swagger-ui/](http://localhost:8000/api/schema/swagger-ui/)で確認してください<br>

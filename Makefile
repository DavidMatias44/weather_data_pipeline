include .env

up:
	docker compose up -d

down:
	docker compose down

psql:
	docker exec -it postgres_container psql -U $(POSTGRES_USER) -d $(POSTGRES_DB)

airflow-pass:
	docker compose logs airflow | grep "Password for user"

clean:
	docker compose down -v

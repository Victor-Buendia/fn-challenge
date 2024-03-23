.PHONY: deploy basic-services dbt-run env-check
deploy: env-check basic-services dbt-run
env-check:
	sh ./env_check.sh
	. .env
basic-services:
	docker-compose up --force-recreate -d
	docker-compose logs -f ingestion
dbt-run:
	docker-compose --profile transform up --force-recreate -d
	docker-compose logs -f dbt
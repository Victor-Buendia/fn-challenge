.PHONY: deploy basic-services dbt-run
deploy: basic-services dbt-run
basic-services:
	docker-compose up --force-recreate -d
	docker-compose logs -f ingestion
dbt-run:
	docker-compose --profile transform up --force-recreate -d
	docker-compose logs -f dbt
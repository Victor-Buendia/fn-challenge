PURPLE = \033[95m
CYAN = \033[96m
DARKCYAN = \033[36m
BLUE = \033[94m
GREEN = \033[92m
YELLOW = \033[93m
RED = \033[91m
BOLD = \033[1m
UNDERLINE = \033[4m
END = \033[0m

.PHONY: deploy basic-services dbt-run env-check info
deploy: env-check basic-services dbt-run info
env-check:
	sh ./env_check.sh
basic-services:
	docker-compose up --force-recreate -d rdbms pgadmin
	docker-compose up ingestion
dbt-run:
	docker-compose --profile transform up --no-deps dbt
info:
	@echo "============== INFORMATION "==============
	@echo ""
	@echo "- PgAdmin4 server at $(UNDERLINE)$(CYAN)http://localhost:5050$(END)"
	@echo "- PostGres server at $(UNDERLINE)$(YELLOW)http://localhost:9876$(END)"
	@echo ""
	@echo "- Python script and Dbt run are both ran in an $(BOLD)ephemeral containers$(END)"

.PHONY: help build-local up down logs ps psql test
.DEFAULT_GOAL := help

build-local:
	docker-compose build
up:
	docker compose up -d

down:
	docker-compose down -v

logs:
	docker-compose logs -f

ps:
	docker-compose ps

psql:
	docker-compose exec web-db psql -U postgres

init_migration:
	docker-compose exec web aerich init -t app.db.TORTOISE_ORM

init_db:
	docker-compose exec web aerich init-db

migration:
	docker-compose exec web aerich upgrade

test:
	docker-compose exec web python -m pytest

help: ## Show options
	@grep -E '^[a-zA-Z_]+:.*?## .*$$' $(MAKEFILE_LIST) | \
		awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'

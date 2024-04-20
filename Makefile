.PHONY: help

help:
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

install: ## Install python deps and setup shell
	@poetry install
	@poetry shell

server: ## Run server
	@poetry run python3 app/main.py


test: ## Run tests
	@poetry run behave tests/features
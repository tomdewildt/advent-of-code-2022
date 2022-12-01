.PHONY: init test lint
.DEFAULT_GOAL := help

NAMESPACE := tomdewildt
NAME := advent-of-code-2022

export PYTHONPATH=src:test

help: ## Show this help
	@echo "${NAMESPACE}/${NAME}"
	@echo
	@fgrep -h "##" $(MAKEFILE_LIST) | \
	fgrep -v fgrep | sed -e 's/## */##/' | column -t -s##

##

init: ## Initialize the environment
	for f in requirements/*.txt; do \
		pip install -r "$$f"; \
	done

##

run: ## Run the challenge
	python -m advent_of_code ${challenge} ./data/day${challenge}.txt

test: ## Run tests
	pytest test

##

lint: ## Run lint
	pylint src test

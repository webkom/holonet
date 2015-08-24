help:
	@echo 'venv            - create virtualenv venv-folder'
	@echo 'dev             - install dev requirements'
	@echo 'prod            - install prod requirements'
	@echo 'lint            - lint project'

dev: venv
	venv/bin/pip install -r requirements/dev.txt --upgrade

prod: venv
	venv/bin/pip install -r requirements/prod.txt --upgrade

venv:
	virtualenv -p `which python3` venv

holonet/settings/local.py:
	touch holonet/settings/local.py

lint:
	flake8

.PHONY: help dev prod lint

help:
	@echo 'venv            - create virtualenv venv-folder'
	@echo 'dev             - install dev requirements'
	@echo 'prod            - install prod requirements'
	@echo 'lint            - lint project'
	@echo 'docs            - build documentation'

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

docs:
	cd docs; make html && open _build/html/index.html; cd ..;

.PHONY: help init dev prod lint static watch docs

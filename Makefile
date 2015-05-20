help:
	@echo 'venv            - create virtualenv venv-folder'
	@echo 'dev             - install dev requirements'
	@echo 'prod            - install prod requirements'
	@echo 'init            - install frontend dependencies'
	@echo 'lint            - lint project'
	@echo 'static          - compile staticfiles'
	@echo 'docs            - build documentation'
	@echo 'watch           - watch for changes in frontend code'

node_modules:
	npm install

bower_components: node_modules
	npm run bower

init: node_modules bower_components

dev: venv
	venv/bin/pip install -r requirements/dev.txt --upgrade

prod: venv
	venv/bin/pip install -r requirements/prod.txt --upgrade

venv:
	virtualenv -p `which python3` venv

holonet/settings/local.py:
	touch holonet/settings/local.py

lint: node_modules
	flake8
	npm run lint

static: node_modules bower_components venv
	npm run build
	venv/bin/python manage.py collectstatic --noinput

watch: node_modules
	npm run watch

docs:
	cd docs; make html && open _build/html/index.html; cd ..;

.PHONY: help init dev prod lint static watch docs

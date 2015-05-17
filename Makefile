help:
	@echo 'venv            - create virtualenv venv-folder'
	@echo 'dev             - install dev requirements'
	@echo 'prod            - install prod requirements'
	@echo 'init            - install frontend dependencies'
	@echo 'lint            - lint project'
	@echo 'static          - compile staticfiles'
	@echo 'docs            - build documentation'
	@echo 'watch-frontend  - watch for changes in frontend code'

init:
	npm install
	npm run bower

dev: init
	pip install -r requirements/dev.txt --upgrade

prod: init
	pip install -r requirements/prod.txt --upgrade

venv:
	virtualenv -p `which python3` venv

holonet/settings/local.py:
	touch holonet/settings/local.py

lint:
	flake8
	npm run lint

static: init
	npm run build
	python manage.py collectstatic --noinput

watch-frontend: init
	npm run watch

docs:
	cd docs; make html && open _build/html/index.html; cd ..;

.PHONY: help init dev prod venv lint static watch-frontend docs

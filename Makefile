help:
	@echo 'dev        - install dev requirements'
	@echo 'prod       - install prod requirements'
	@echo 'venv       - create virtualenv venv-folder'
	@echo 'production - deploy production'
	@echo 'frontend   - build frontend'
	@echo 'watchify   - watch style and js files'
	@echo 'clean      - clean builds'

UGLIFY     = node_modules/.bin/uglifyjs
BROWSERIFY = node_modules/.bin/browserify
WATCHIFY   = node_modules/.bin/watchify

BUILD_JS    = holonet/dashboad/static/js/index.js
JS_MAIN   = holonet/dashboad/static/js/holonet/app.js

JS         = $(shell find holonet/dashboad/static/js/holonet/ -name "*.js")

TRANSFORMS = -t [ reactify --harmony ]

$(BUILD_JS): $(JS)
ifneq ($(NODE_ENV), development)
	$(BROWSERIFY) $(TRANSFORMS) $(JS_MAIN) | $(UGLIFY) > $(BUILD_JS)
else
	$(BROWSERIFY) $(TRANSFORMS) $(JS_MAIN) > $(BUILD_JS)
endif

clean:
	rm -f $(BUILD_JS)

init:
	npm install

frontend: $(BUILD_JS)

watchify:
	$(WATCHIFY) $(TRANSFORMS) $(JS_MAIN) -v -o $(BUILD_JS)

dev: init $(BUILD_JS)
	pip install -r requirements/dev.txt --upgrade

prod: init $(BUILD_JS)
	pip install -r requirements/prod.txt --upgrade

venv:
	virtualenv -p `which python3` venv

holonet/settings/local.py:
	touch holonet/settings/local.py

.PHONY: help dev prod venv frontend clean watchify

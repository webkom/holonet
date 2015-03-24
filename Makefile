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
STYLUS     = node_modules/.bin/stylus
NIB        = node_modules/nib/lib

BUILD_JS    = holonet/dashboard/static/js/index.js
BUILD_CSS   = holonet/dashboard/static/css/style.css

JS_MAIN   = holonet/dashboard/static/js/holonet/app.js
CSS_MAIN  = holonet/dashboard/static/styl/style.styl

JS         = $(shell find holonet/dashboard/static/js/holonet/ -name "*.js")
CSS        = $(shell find holonet/dashboard/static/styl/ -name "*.styl")

TRANSFORMS = -t [ reactify --harmony ]

$(BUILD_JS): $(JS)
ifneq ($(NODE_ENV), development)
	$(BROWSERIFY) $(TRANSFORMS) $(JS_MAIN) | $(UGLIFY) > $(BUILD_JS)
else
	$(BROWSERIFY) $(TRANSFORMS) $(JS_MAIN) > $(BUILD_JS)
endif

$(BUILD_CSS): $(CSS)
ifneq ($(NODE_ENV), development)
	$(STYLUS) --include $(NIB) \
	--include holonet/dashboard/static/styl \
	--compress < $(CSS_MAIN) > $(BUILD_CSS)
else
	$(STYLUS) --include $(NIB) \
	--include holonet/dashboard/static/styl \
	--include-css < $(CSS_MAIN) > $(BUILD_CSS)
endif

clean:
	rm -f $(BUILD_JS) $(BUILD_CSS)

init:
	npm install

frontend: $(BUILD_JS) $(BUILD_CSS)

watchify:
	$(WATCHIFY) $(TRANSFORMS) $(JS_MAIN) -v -o $(BUILD_JS)

watch-css: holonet/dashboard/static/css/style.css
	@true

watch:
	@forego start

dev: init $(BUILD_JS) $(BUILD_CSS)
	pip install -r requirements/dev.txt --upgrade

prod: init $(BUILD_JS) $(BUILD_CSS)
	pip install -r requirements/prod.txt --upgrade

venv:
	virtualenv -p `which python3` venv

holonet/settings/local.py:
	touch holonet/settings/local.py

docs:
	cd docs; make html && open _build/html/index.html; cd ..;

.PHONY: help dev prod venv frontend clean watchify watch-css watch docs

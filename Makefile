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

BUILD_JS    = holonet/dashboad/static/js/index.js
BUILD_CSS   = holonet/dashboad/static/css/style.css

JS_MAIN   = holonet/dashboad/static/js/holonet/app.js
CSS_MAIN  = holonet/dashboad/static/styl/style.styl

JS         = $(shell find holonet/dashboad/static/js/holonet/ -name "*.js")
CSS        = $(shell find holonet/dashboad/static/styl/ -name "*.styl")

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
	--include holonet/dashboad/static/styl \
	--compress < $(CSS_MAIN) > $(BUILD_CSS)
else
	$(STYLUS) --include $(NIB) \
	--include holonet/dashboad/static/styl \
	--include-css < $(CSS_MAIN) > $(BUILD_CSS)
endif

clean:
	rm -f $(BUILD_JS) $(BUILD_CSS)

init:
	npm install

frontend: $(BUILD_JS) $(BUILD_CSS)

watchify:
	$(WATCHIFY) $(TRANSFORMS) $(JS_MAIN) -v -o $(BUILD_JS)

watch-css: holonet/dashboad/static/css/style.css
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

.PHONY: help dev prod venv frontend clean watchify watch-css watch

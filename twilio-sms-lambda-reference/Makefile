.DEFAULT_GOAL = deploy

SAM_CLI ?= sam

.PHONY: build
build:
	$(SAM_CLI) build

.PHONY: deploy
deploy:
	$(SAM_CLI) deploy

.PHONY: watch
watch:
	$(SAM_CLI) logs --tail

.PHONY: redeploy
redeploy: build deploy watch

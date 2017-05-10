BOXES := $(notdir $(wildcard docker/*))

PLAYBOOK        ?= webhook

define USAGE
targets:

  all    build all Docker images (default)
  clean  remove all Docker images
  help   show this screen

machine targets:

  <machine>        build <machine> image
  <machine> clean  remove <machine> image
  <machine> test   provision and test <machine>

machines:

  $(BOXES)

variables:

  PLAYBOOK          Choose Playbook to test. Default: 'webhook'.
endef

is_machine_target = $(if $(findstring $(firstword $(MAKECMDGOALS)),$(BOXES)),true,false)

all:
	docker-compose build

clean:
ifeq (true,$(call is_machine_target))
	docker rmi -f ansiblewebhook_$(firstword $(MAKECMDGOALS))
else
	-docker images -q ansiblewebhook* | xargs docker rmi -f
endif

help:
	@echo $(info $(USAGE))

test:
ifeq (true,$(call is_machine_target))
	./scripts/ci.sh $(firstword $(MAKECMDGOALS)) $(PLAYBOOK)
else
	$(error `test` requires a machine name, see `make help`)
endif

$(BOXES):
# Don't build an image just to delete it.
ifeq (,$(findstring clean,$(lastword $(MAKECMDGOALS))))
	{ docker images ansiblewebhook_$@ | grep $@; } && exit || docker-compose build $@
endif

.PHONY: all \
        clean \
        help \
        test

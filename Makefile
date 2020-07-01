PYTHONCMD=python3
PYTHONTEST=$(PYTHONCMD) -m unittest -v --locals

# deprecated
.PHONY: old-test
old-test:
	@echo old running tests
	@# remove this test once unittests are better
	@$(PYTHONCMD) testing.py

# deprecated
.PHONY: old-run
old-run:
	@$(PYTHONCMD) Splendor.py

.PHONY: run
run:
	@$(PYTHONCMD) game.py

.PHONY: test
test:
	@echo running tests
	@# python3 unit tests
	@$(PYTHONTEST) tests/*.py

.PHONY: debug
debug:
	@echo display debugging
	@$(PYTHONCMD) debug.py

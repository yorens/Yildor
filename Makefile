PYTHONCMD=python3
PYTHONTEST=$(PYTHONCMD) -m unittest -v 

.PHONY: test
test:
	@echo running tests
	# remove this test once unittests are better
	@$(PYTHONCMD) testing.py
	# python3 unit tests
	@$(PYTHONTEST) tests/*.py
	
.PHONY: run
run:
	@$(PYTHONCMD) Splendor.py
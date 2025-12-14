.PHONY: run clear seed

run :
	@export FLASK_APP=customer_area.py && \
	export FLASK_ENV=development && \
	flask run

clear:
	@pkill -f flask || true
	@rm -rf database

seed:
	@python3 scripts/seed_database.py
.PHONY: run server clear

run server:
	@export FLASK_APP=customer_area.py && \
	export FLASK_ENV=development && \
	flask run

clear:
	@pkill -f flask || true
	@rm -rf database

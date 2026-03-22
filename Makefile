.PHONY: run clear seed clear_venv create_venv activate_venv deactivate_venv delete_venv install_dependencies ruff

run :
	@export FLASK_APP=customer_area.py && \
	export FLASK_ENV=development && \
	flask run &

clear_venv:
	@rm -rf venv

create_venv:
	@python3 -m venv venv

activate_venv:
	source venv/bin/activate

deactivate_venv:
	deactivate

delete_venv:
	@rm -rf venv

install_dependencies:
	@pip3 install -r requirements.txt

clear:
	@pkill -f flask || true
	@rm -rf database

seed:
	@python3 scripts/seed_database.py

ruff:
	@ruff check .
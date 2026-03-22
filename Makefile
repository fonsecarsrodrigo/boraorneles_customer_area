.PHONY: run clear seed clear_venv create_venv activate_venv deactivate_venv delete_venv install_dependencies ruff docker-fe-build docker-fe-run

BE_DIR := bora-be-service
FE_DIR := bora-fe-service

# Frontend (nginx in bora-fe-service): build context must be FE_DIR so COPY paths resolve
docker-fe-build:
	docker build -f $(FE_DIR)/bora-fe.docker -t bora-fe $(FE_DIR)

docker-fe-run:
	docker run --rm -p 8080:80 bora-fe

# Backend (Flask in bora-be-service)
run :
	@cd $(BE_DIR) && export FLASK_APP=customer_area.py && \
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
	@rm -rf $(BE_DIR)/database

seed:
	@python3 $(BE_DIR)/scripts/seed_database.py

ruff:
	@ruff check .

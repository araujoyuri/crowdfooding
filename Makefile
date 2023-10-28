generate_migration:
	alembic revision --autogenerate -m "$(name)"

migrate_up:
	alembic upgrade head

migrate_down:
	alembic downgrade -1

run_dev:
	uvicorn src.main:app --host 0.0.0.0 --port 8000 --reload
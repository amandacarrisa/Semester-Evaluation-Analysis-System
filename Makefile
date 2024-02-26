clean:
	sudo rm -rf backend db.sqlite3 manage.py data
stop:
	docker-compose stop
kill:
	docker-compose kill
up:
	docker-compose up
migrate:
	docker-compose run web python edom_backend/manage.py migrate
make_migration:
	yes | docker-compose run web python edom_backend/manage.py makemigrations --merge
build:
	docker-compose build

migrate:
	- python fastube/manage.py makemigrations users posts
	- python fastube/manage.py migrate

test:
	- pep8 .
	- python fastube/manage.py test posts -v2

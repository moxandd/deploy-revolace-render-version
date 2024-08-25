build-css:
	npm run build-css

startproject: build-css
	@echo Starting local server...
	python manage.py runserver
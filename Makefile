base_env:
	@echo "Installing base env requirements"
	pip install -r requirements/base.txt

dev_env:
	@echo "Installing dev env requirements"
	pip install -r requirements/dev.txt

run:
	@echo "Run comfy scraper"
	scrapy crawl comfy_products_list -a spiders_dir=comfy.spiders

analytic:
	@echo "Run analytics script. First of all, you need to generate csv file with data!"
	python analytics.py

format:
	@echo "Run format checks"
	isort .
	flake8 .

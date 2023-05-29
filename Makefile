run:
	scrapy crawl comfy_products_list -a spiders_dir=comfy.spiders

analytic:
	python analytics.py

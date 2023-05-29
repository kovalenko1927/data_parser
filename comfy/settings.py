# Scrapy settings for comfy project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = "comfy"

SPIDER_MODULES = ["comfy.spiders"]
NEWSPIDER_MODULE = "comfy.spiders"

# Crawl responsibly by identifying yourself (and your website) on the user-agent
# USER_AGENT = "comfy_ (+http://www.yourdomain.com)"

# Obey robots.txt rules
ROBOTSTXT_OBEY = True

# Configure maximum concurrent requests performed by Scrapy (default: 16)
CONCURRENT_REQUESTS = 1

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = 4
# RANDOMIZE_DOWNLOAD_DELAY = False
# The download delay setting will honor only one of:
CONCURRENT_REQUESTS_PER_DOMAIN = 1
CONCURRENT_REQUESTS_PER_IP = 1

# Disable cookies (enabled by default)
# COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
# TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Language": "en",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/113.0.0.0 Safari/537.36",
    "Cookie": "nlbi_1858972=JjpSer+P5j/rH1RVTxwWFAAAAAAYnBQhkLbYKNNcUJ+LCNIf; frontend=bo0fklmysx56hefwij5awo8l5i; "
              "digi_user_cookie=0%3Ali4phpnm%3A3fd3af-00a9a9-7cd009-00936c-507425; guest_quote_id=787756263; "
              "customer_group=0; esputnicSimilatAbTestCookie=r776v1546; active_city_id=506; X-Store=1; "
              "_userGUID=0:li4pso2s:93zdSzOuhZMkkGcXGTi_1Pkr8KG1_G6Y; "
              "pa=1685133482022.5680.8031633131950557comfy.ua0.403146652394494+1; "
              "visid_incap_1858972=1BMKjoSMTAOEc651NUrOG1zNcGQAAAAAQkIPAAAAAACAWo2sAdRaPjOsqxC1UwhCsZ/EuHT/cXvO; "
              "fp=32; lfp=10/27/2022, 11:38:35 PM; "
              "incap_ses_1083_1858972=dIkWJJJZeDWhNj75MpgHD4ONcWQAAAAAP6aU96F0R6Cy6jsSwbmqHg==; "
              "nlbi_1858972_2147483392=Pwv/ZbjkJWJ5TGoqTxwWFAAAAACu7OnvI+J6HCy1ReI/Qp7B; "
              "incap_ses_451_1858972=ELj6a1lY2w1QO2I+DEdCBo6fcWQAAAAAX/KUBobYWdFnmPYcwAQYeQ==; "
              "reese84=3:Jdfeak3+uUiPS4TYD7rucQ"
              "==:g1JBRvyWqQaOu6pkGU974AVn4T59pCfQCmaiYD7OnrRv0mpRVJ4gfzDePW6zwwqLkPmmopH2eb3PfmaZUvMrElOFl7"
              "/MC6otpt1l8S+GP2InhlaRMQBgJkYEd8OZZy1vKgIEM92Vn6qbBzkAn2sL27Aisdgil//nCIdj7PDdRk0PYDmFyXl"
              "+XYLLVOYFPwptvKRLXDsuocdaXf1TjsQJGGJVPsaP+W"
              "/usacPErBaGOdlNCtK7TiWOH4bmcLakOvbPsnDT5EUbbR7ofNmFzUdnHKsOdRqI11XPayWFdS4o3Tb0cZZFmxyXyO3IZUDdibVDYYLXJ"
              "tpsPz+3J1xF0+OmYn0GC32rjf5Wp1sJCoIKu1ZMra4owYhIuNDkHQfxer69rWZ9+aWi7hBDm7m1hZfrMkte+BrdTZ4d5/Aow1W1FaJih"
              "hy1s7fIIQsmA8ZYkIII1qwF9kH5wV/maVQg8mqLA==:k6yj868i5iBIq71leGgOD/GZ8deDB9IbO7969bIm7L0= "
}

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
# SPIDER_MIDDLEWARES = {
#    "comfy_.middlewares.ComfySpiderMiddleware": 543,
# }

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html

# SERIALIZATION_ENABLED = False
from shutil import which

SELENIUM_DRIVER_NAME = 'firefox'
SELENIUM_DRIVER_EXECUTABLE_PATH = which('geckodriver')
SELENIUM_DRIVER_ARGUMENTS = ['--headless']

DOWNLOADER_MIDDLEWARES = {
    'scrapy_selenium.SeleniumMiddleware': 800
}

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
# EXTENSIONS = {
#    "scrapy.extensions.telnet.TelnetConsole": None,
# }

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
    "comfy.pipelines.ComfyCSVPipeline": 300,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
# AUTOTHROTTLE_ENABLED = True
# The initial download delay
# AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
# AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
# AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
# AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
# HTTPCACHE_ENABLED = True
# HTTPCACHE_EXPIRATION_SECS = 0
# HTTPCACHE_DIR = "httpcache"
# HTTPCACHE_IGNORE_HTTP_CODES = []
# HTTPCACHE_STORAGE = "scrapy.extensions.httpcache.FilesystemCacheStorage"

# Set settings whose default value is deprecated to a future-proof value
REQUEST_FINGERPRINTER_IMPLEMENTATION = "2.7"
TWISTED_REACTOR = "twisted.internet.asyncioreactor.AsyncioSelectorReactor"
FEED_EXPORT_ENCODING = "utf-8"

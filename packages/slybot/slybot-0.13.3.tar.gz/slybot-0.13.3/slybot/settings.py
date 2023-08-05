from __future__ import absolute_import
SPIDER_LOADER_CLASS = 'slybot.spidermanager.SlybotSpiderManager'
EXTENSIONS = {'slybot.closespider.SlybotCloseSpider': 1}
ITEM_PIPELINES = {
    'slybot.dupefilter.DupeFilterPipeline': 1,
    'slybot.meta.DropMetaPipeline': 2
}
SPIDER_MIDDLEWARES = {'slybot.spiderlets.SpiderletsMiddleware': 999}  # as close as possible to spider output
DOWNLOADER_MIDDLEWARES = {
    'slybot.pageactions.PageActionsMiddleware': 700,
    'scrapy_splash.middleware.SplashCookiesMiddleware': 723,
    'slybot.splash.SlybotJsMiddleware': 725
}
PLUGINS = [
    'slybot.plugins.scrapely_annotations.Annotations',
    'slybot.plugins.selectors.Selectors'
]
SLYDUPEFILTER_ENABLED = True
SLYDROPMETA_ENABLED = False
DUPEFILTER_CLASS = 'scrapy_splash.SplashAwareDupeFilter'
PROJECT_DIR = 'slybot-project'
FEED_EXPORTERS = {
    'csv': 'slybot.exporter.SlybotCSVItemExporter',
}
CSV_EXPORT_FIELDS = None

try:
    from .local_slybot_settings import *
except ImportError:
    pass

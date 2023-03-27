from django.conf import settings
from django.test.runner import DiscoverRunner
from celery import current_app


USAGE = """\
Custom test runner to allow testing of celery delayed tasks.
"""


def _set_eager():
    settings.CELERY_ALWAYS_EAGER = True
    current_app.conf.CELERY_ALWAYS_EAGER = True
    settings.CELERY_EAGER_PROPAGATES_EXCEPTIONS = True  # Issue #75
    current_app.conf.CELERY_EAGER_PROPAGATES_EXCEPTIONS = True


class CeleryTestSuiteRunner(DiscoverRunner):
    """Django test runner allowing testing of celery delayed tasks.
    All tasks are run locally, not in a worker.
    To use this runner set ``settings.TEST_RUNNER``::
        TEST_RUNNER = 'djcelery.contrib.test_runner.CeleryTestSuiteRunner'
    """
    def setup_test_environment(self, **kwargs):
        _set_eager()
        super().setup_test_environment(**kwargs)

import pytest

from restiro import clean_examples_dir
from restiro.middlewares.webtest import TestApp
from nanohttp import configure

from nanohttp_notes.application import DemoApplication


@pytest.fixture(scope='session')
def app():
    wsgi_app = DemoApplication()
    configure(force=True)

    clean_examples_dir()
    test_app = TestApp(app=wsgi_app)
    yield test_app

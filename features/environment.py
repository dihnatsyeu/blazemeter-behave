from behave.fixture import use_fixture_by_tag

from web_source.web_factory import get_web

def before_all(context):
    web = get_web(context.config.userdata['browser'])
    context.web = web
from pyramid.config import Configurator
from sqlalchemy import engine_from_config

from .models import DBSession

def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    engine = engine_from_config(settings, 'sqlalchemy.')
    DBSession.configure(bind=engine)
    config = Configurator(settings=settings)
    # mako settings for file extension .html
    config.include('pyramid_jinja2')
    config.add_renderer(".pt", "pyramid.mako_templating.renderer_factory")
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_route('home', '/')
    
    #route for user
    config.add_route('user_init', '/user')
    config.add_route('user_save', '/user_save')

    #route for calculate
    config.add_route('calculate_init', '/calculate')
    config.add_route('calculate_values', '/calculate_values')
    config.scan()
    return config.make_wsgi_app()


from configparser import ConfigParser
import os

configure = ConfigParser(interpolation=None)
configure.read(os.path.join(os.getcwd(), 'url.cfg'))


def main_urls():
    url = configure.get('MAIN_URL', 'url')
    market = configure.get('MAIN_URL', 'market')
    lang = configure.get('MAIN_URL', 'lang')
    employ = configure.get('MAIN_URL', 'employ')
    anchor = configure.getint('MAIN_URL', 'anchor')
    chanelId = configure.get('MAIN_URL', 'chanelId')
    count = configure.getint('MAIN_URL', 'count')
    main_url = url + 'filter={}&'.format(market) + 'filter={}&'.format(lang) + 'filter={}&'.format(employ) + \
               'anchor={}&'.format(anchor) + 'consumerChannelId={}&'.format(chanelId) + 'count={}'.format(count)
    return main_url


def urls():
    url = configure.get('URL', 'url')
    market = configure.get('URL', 'market')
    lang = configure.get('URL', 'lang')
    employ = configure.get('URL', 'employ')
    anchor = configure.getint('URL', 'anchor')
    chanelId = configure.get('URL', 'chanelId')
    count = configure.getint('URL', 'count')
    url_ = url + 'filter={}&'.format(market) + 'filter={}&'.format(lang) + 'filter={}&'.format(employ) + \
           'consumerChannelId={}&'.format(chanelId) + 'count={}'.format(count)
    return url_

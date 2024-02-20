import configparser

config = configparser.ConfigParser()    

config['filepath'] = {}
config['filepath']['stars_data'] = './zodiac_stars.json'
config['filepath']['birth_data'] = './zodiac_births.json'
config['filepath']['config'] = './config.conf'

config['url'] = {}
config['url']['base_url'] = 'http://skyservice.pha.jhu.edu/DR14/ImgCutout/getjpeg.aspx'


# create config file as confog.conf
def create_config():
    with open('config.conf', 'w', encoding='utf-8') as f:
        config.write(f)
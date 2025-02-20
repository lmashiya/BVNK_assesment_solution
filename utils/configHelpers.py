from configparser import ConfigParser

path = 'configurations/config.ini'
def read_config(category,key):
    config = ConfigParser()
    config.read(path)
    return config.get(category,key)

def update_config(section, key, value):
    config = ConfigParser()
    config.read(path)

    if section not in config:
        config.add_section(section)
    config.set(section, key, value)

    with open(path, "w") as configfile:
        config.write(configfile)
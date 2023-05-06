import configparser

if __name__ == '__main__':


    config = configparser.ConfigParser()
    #
    # config["basic"] = {'map_name': '1152, 55, 1238, 81',
    #                      'cord_x': '1263, 56, 1308, 79',
    #                      'cord_y': '1320, 55, 1354, 78',
    #                      'monsters': '463, 258, 948, 581'
    #                      }
    #
    # config['bitbucket.org'] = {'User': 'hg'}
    # config['topsecret.server.com'] = {'Host Port': '50022', 'ForwardX11': 'no'}
    # with open('config_jf.ini', 'w') as configfile:
    #     config.write(configfile)
    config.read('config_jf.ini')
    print(config.sections())
    print('basic' in config)
    print(config['basic']['map_name'])
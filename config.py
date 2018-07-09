

class Config:
    def __init__(self, path):
        self.config = config
        print(config.sections())
        #for section in config.sections():
        #    self.__read_config(section)
        self.__db_conf(config)
        #self.__spectrogram_conf(config)
        #self.__image_conf(config)

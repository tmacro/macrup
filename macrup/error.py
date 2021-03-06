
class MacrupError(Exception):
    '''Root exception for all macrup errors'''
    pass

class UnknownError(MacrupError):
    '''You done fucked up. something happened, probably in a catch all'''
    pass

class ConfigError(MacrupError):
    '''Error regarding configuration'''
    pass

class InvalidConfigError(ConfigError):
    '''Error parsing a users configuration'''
    pass

class NoConfigError(ConfigError):
    '''Error locating a users config'''
    pass

class ConfigImportError(ConfigError):
    '''Error locating a child config file'''
    pass
class RequiredArguementError(MacrupError):
    pass
from flask import request
import socket



def getConfig(app):
    ''' --> dict
    Returns a dictionary object with the app configuration
    '''
    data ={}
    appParams = ('APPLICATION_ROOT', 'SERVER_NAME', 'ENV', 'DEBUG')

    data.update({'HOST-NAME' : socket.gethostname()}) 
    data.update({'HOST-IP' : socket.gethostbyname(socket.gethostname()) }) 
    for param in appParams :
        data.update({param:app.config[param]})

    return data

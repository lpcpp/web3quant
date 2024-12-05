OKX_SETTING = {
    "apikey": "",
    "secretkey": "",
    "IP": "",
    "name": "",
    "Permissions": "",
    "passphrase": ""
}

COINMARKET_SETTING = {
    "apikey": "",
}

try:
    from settings_prod import *
except:
    pass
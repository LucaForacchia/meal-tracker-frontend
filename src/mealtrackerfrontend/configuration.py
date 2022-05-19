import configparser

app_config = {}

def read_config(filename):
    parser = configparser.ConfigParser()
    parser.read(filename)
    print("Sections", parser.sections()) # []
    print(parser['DEFAULT']['backend_url'])
    return parser

## QUI DENTRO CREO UNA SOLA VOLTA IL SERVER REQUEST E LO CHIAMO CON IL GET?
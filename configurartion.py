import json
import logging


def json_data():
    body_json = {}
    body_json['userid'] = int("list_of_data"[0].strip())
    body_json['title'] = "list_of_data"[1].strip()
    body_json['body'] = "list_of_data"[2].strip()
    return (body_json) 


def get_config_data(key, file='config.json'):
    with open(file) as f:
        json_data = json.load(f)
    return (json_data[key])


def logger(error=False):
    logging.basicConfig(filename=get_config_data('log_file'), 
                        encoding='utf-8', 
                        format='%(asctime)s:-%(levelname)s:%(message)s', 
                        level=logging.DEBUG)
    if error:
        return logging.error
    else:
        return logging.info
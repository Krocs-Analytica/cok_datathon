import yaml

filename = 'cok_datathon\config\elt_config.yaml'
def read_config_file(filename=filename):
    with open(filename, 'r') as stream:
        try:
            config = yaml.safe_load(stream)
            return config
        except yaml.YAMLError as exc:
            print(exc)
            return None

# data = read_config_file(fn)
# if data.get('clean').get('check_missing_values'):
#     print('Missing values checked successfully!\n')
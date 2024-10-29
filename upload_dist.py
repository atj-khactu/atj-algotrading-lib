import os

api_token = os.environ['pypi_api_token']

os.system('py -m build')
os.system(f'py -m twine upload --repository pypi dist/* --username token --password {api_token}')
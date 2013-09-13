ckanext-ogdch_actions
=====================

Additional action APIs for opendata.admin.ch

## Installation

Use `pip` to install this plugin. This example installs it in `/home/www-data`

```bash
source /home/www-data/pyenv/bin/activate
pip install -e git+https://github.com/ogdch/ckanext-ogdch_actions.git#egg=ckanext-ogdch_actions --src /home/www-data
cd /home/www-data/ckanext-ogdch-actions
python setup.py develop
```

Make sure to add `ogdch_actions` to `ckan.plugins` in your config file.

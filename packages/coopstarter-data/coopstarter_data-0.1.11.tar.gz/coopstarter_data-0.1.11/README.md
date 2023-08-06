# CoopStarter Application data repository

This project is a Python module, compatible with Django REST Framework and DjangoLDP additional module, describing the models and the API needed and available on the future coopstarter application.

## Installation

Here is the detailed explaination of the preferred installation process.
Depending on your OS and your python installation, commands could have to be run using either `python` or `python3`.

### Using sib-manager

This is the easier way to setup the server side of the project but it is known to have some issues, especially on Ubuntu.

```sh
pip install sib-manager
sib startproject coopstarter -m coopstarter_data -m django_countries -m djangoldp_account -m djangoldp_circle -m djangoldp_conversation -m oidc_provider@django-oidc-provider
sib initproject
```

### Alternate installation procedure using virtualenv

If you get some errors about the `--user` flag and `permission denied` then you should try to setup a virtualenv first.
Then the full procedure is:

```
mkdir coopstarter
cd coopstarter
pip install virtualenv
virtualenv venv
source venv/bin/activate
pip install -U sib-manager
sib startproject coopstarter -m coopstarter_data -m django_countries -m djangoldp_account -m djangoldp_circle -m djangoldp_conversation -m oidc_provider@django-oidc-provider
cd coopstarter
sib initproject
```

For both of these installation procedure, you're ok if you can see the migrations being executed by the `initproject` command.

## Running the project

From your console, at the root of the coopstarter-server directories containing the manage.py file, please run the following commands:

```
cd coopstarter
python manage.py createsuperuser

```

This command will ask you for some information (username, email, password) to generate the initial administrator of your data server.

```
python manage.py runserver

```

If successful, this command will make available on `127.0.0.1:8000/admin/` the administrator backend. You will then be able to log-in using the credentials you set at the previous step.

## Initialising the database

As some fixtures are provided to enrich the application database easily, the following command will allow you to properly load them.

```
python manage.py loaddata ../venv/lib/python3.6/site-packages/coopstarter_data/fixtures/*.json
```

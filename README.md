# VINYL COLLECTOR

The goal of this app is to collect info about Vinyl you have in your collection and to have opportunity share info
about yours collection with friends via social networks.

## Quickstart

Run the following commands to bootstrap your environment:

    sudo apt-get install -y git python3-venv python3-pip vim
    git clone https://github.com/Rodionald/Vinyl_Collector
    cd Vinyl_Collector

    python3 -m venv venv
    source venv/bin/activate
    pip3 install -r requirements.txt

    cp .env.template .env


Run the app locally:

    python3 manage.py runserver 0.0.0.0:8000 --settings=core.settings.dev

Run the app with gunicorn:

    gunicorn core.wsgi -b 0.0.0.0:8001
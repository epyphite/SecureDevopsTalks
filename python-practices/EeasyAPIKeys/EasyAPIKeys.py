import json
import os

import click

from webapp.webapi import app

@click.command()
@click.option('--webserver', is_flag=True, help='Run Web Server')
@click.option('--eventfile', help='Send the event File is needed', default='')
@click.option('--api-key', help='Specify API KEY, default env if not', default='')
def main( webserver, eventfile, api_key):

    # Web Server overrides
    if webserver:
        if api_key == '':
            print("Using Environment Key")
            api_key = os.environ['APIKEY']

        if (api_key == ''):
            print("No Key set, exiting")
            return
        print("Running WebServer")
        app.config['APIKEY'] = api_key
        app.run(host='0.0.0.0', port=8000, debug=True)


if __name__ == '__main__':
    main()

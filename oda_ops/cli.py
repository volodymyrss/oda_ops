import click
from mattermostdriver import Driver
import json
from dynaconf import Dynaconf
from pathlib import Path
from os import getenv

settings = Dynaconf(
        settings_files=[
                Path(getenv("HOME")) / ".oda/settings.toml",
                Path(getenv("HOME")) / ".oda/private.toml",
        ],

        environments=False,
        load_dotenv=False,
        envvar_prefix="ODA",             # variables exported as `ODAKB_FOO=bar` becomes `settings.FOO == "bar"`
)


@click.group()
@click.pass_obj
def cli(obj):
    mm = Driver({
        'url': 'mattermost.astro.unige.ch',
        "token": settings.mattermost.access_token, ## THE TOKEN THAT YOU JUST CREATED
                'scheme': 'https',
                    'port': 443
                })

    mm.login()
    obj['mm'] = mm


@cli.command()
@click.argument("message")
@click.pass_obj
def send(obj, message):
    channel_name = "deployment"
    team = "cdci"

    mm = obj['mm']
    
    channel = mm.channels.get_channel_by_name_and_team_name(team, channel_name)
    channel_id = channel['id']

    mm.posts.create_post(options={
        'channel_id': channel_id,
        'message': message
        })


@cli.command()
@click.pass_obj
def listen(obj):
    async def my_event_handler(e):  
        message=json.loads(e)
        print(message)
        
    obj['mm'].init_websocket(my_event_handler)

def main():
    cli(obj={})

if __name__ == "__main__":
    main()


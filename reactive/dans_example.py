from charms.reactive import set_flag, when, when_not, set_state
from charms.reactive.helpers import data_changed
from charmhelpers.core import hookenv
from charmhelpers.fetch.archiveurl import ArchiveUrlFetchHandler
from charmhelpers.core.templating import render

from lib_dans_example import DansexampleHelper

from subprocess import check_call, CalledProcessError, call, check_output, Popen, PIPE
import os

au = ArchiveUrlFetchHandler()
#os.environ["JOSHUA"] = "/opt/joshua-runtime-6.0.5/"
port =  hookenv.config('port')
helper = DansexampleHelper()

@when_not('dans-example.installed')
def install_dans_example():
    hookenv.status_set('maintenance', 'Traefik')
    download()
    unzip()
    set_flag('dans-example.installed')

def download():
    au.download("https://github.com/containous/traefik/releases/download/v2.0.0/traefik_v2.0.0_linux_amd64.tar.gz", "/tmp/traefik_v2.0.0_linux_amd64.tar.gz")

def unzip():
    check_output(['tar', 'xvfz', "/tmp/traefik_v2.0.0_linux_amd64.tar.gz", '-C', '/opt'])

@when('dans-example.installed')
def start_traefik():
    try:
        check_call(['pgrep', '-f', 'traefik'])
    except CalledProcessError:
        hookenv.open_port(port)
        hookenv.log("Starting Traefik on " + hookenv.config('port'))

        render(
          source='traefik.toml.tmpl',
          target='/opt/traefik.toml',
          context={
              'traefik_api_debug': hookenv.config('traefik_api_debug')
          })
        Popen(['nohup /opt/traefik &'], cwd='/opt', stdout=PIPE,stderr=PIPE,shell=True)
       
    hookenv.status_set('active', 'Traefik running')


# Overview
This juju charm installs [Traefik v2.0.0](https://traefik.io/).

To build simply run the Makefile target
```bash
make build
```

To deploy locally, `cd /tmp/charm-builds` (or wherever your charms are staged locally) and run
```bash
juju switch lxd-local  (or  juju switch canonical-jimm.jujucharms.com:weechat
juju deploy ./dans-example
```

If you don't have a local lxd controller: `juju bootstrap localhost lxd-local` will get you setup :)

# Code
Main file is found at [dans_example.py](reactive/dans_example.py)

There's also a stock [traefik.toml template file](templates/traefik.toml.tmpl)

# Traefik Dashboard
Will be accessible at e.g. http://10.191.169.46:8080/dashboard/#/

Just replace the IP address with that of public IP of the Juju unit!

Testing is done via tox and there are two environments setup, one for unit and
one for functional testing. Each has a separate requirements file to setup the
virtualenv that they will be run in. These requirements are only needed for
running the tests.

Unit testing is performed via pytest. Tests are defined in
/tests/unit/test_XXX.py

To run unit test with tox run:
```bash
make unittest
```

Out of the gate, unit testing just verifies that the testing framework is
working. It is recommend that the library file in the lib folder be fully unit
tested.


The currently supported method of functional testing uses libjuju to interact
with juju and the units.

To run libjuju functional testing:
```bash
make functional
```
This requires a controller; a temporary model will be created and torn down at
the beginning and end of the testing session, respectively. A custom
module-scoped event loop is provided as to support fixtures with scopes beyond
'function'.

Several generic fixtures are provided in conftest.py, and reuse is encouraged.

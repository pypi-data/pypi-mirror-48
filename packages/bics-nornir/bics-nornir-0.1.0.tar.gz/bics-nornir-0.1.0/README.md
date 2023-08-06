# Bics_nornir
Nornir is a Python automation framework that provides support for concurrent execution of tasks against a set of hosts. It comes with pluggable inventory and task capabilities to promote composability and reusability.

`Bics_nornir` provides a set of BICS-developed plugins that addresses required functionality for communicating with the infrastructure as well as plugins as building blocks to implement _runbooks_. These plugins are:

- `.../plugins/connections/ncclient`: a connection plugin that uses `ncclient` to communicate with devices using Netconf
- `.../plugins/tasks/networking/nc`: a set of high-level task-plugins:
    - `get_config`: retrieves (a part of) the device's configuration using netconf. The selection of a subtree of the configuration is through the `path` parameter
    - `get`/ retrieves (a part of) the device's state information using netconf.
    - `nc_configure`: sends a configuration (python object) to the device, with support of candidate/running comparision, dry-run and associated commit() and discard()
- `.../plugins/tasks/data/load_intent`: loads intent files from a directory


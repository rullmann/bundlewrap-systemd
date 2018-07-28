# systemd

The 'systemd' bundle provides the `systemd-daemon-reload` action.
It can be used when altering systemd units.
E.g. to override default variables and so on.

Additionally it sets the timezone of a system. The timezone can be configured by using node or group metadata.

## Integrations

* Bundles:
  * By providing the `systemd-daemon-reload` action

## Metadata

No metadata is required, but you can use the following options:

    'metadata': {
        'timezone': 'UTC', # optional, change timezone from UTC to everything `timedatectl list-timezones` lists
    }
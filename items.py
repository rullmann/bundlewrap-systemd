timezone = node.metadata.get('timezone', 'UTC')

actions = {
    'systemd-daemon-reload': {
        'command': 'systemctl daemon-reload',
        'triggered': True,
        'needed_by': ['svc_systemd:'],
    },
    'timedatectl-set-timezone': {
        'command': 'timedatectl set-timezone ' + timezone,
        'unless': 'timedatectl | grep -F " Time zone: {} "'.format(timezone),
    },
}

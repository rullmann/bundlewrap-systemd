actions = {
    'systemd-daemon-reload': {
        'command': 'systemctl daemon-reload',
        'triggered': True,
        'needed_by': ['svc_systemd:'],
    },
}

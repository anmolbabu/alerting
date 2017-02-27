from tendrl.alerting.objects \
    import AlertingBaseObject
from tendrl.commons.etcdobj import EtcdObj


class NotificationMedia(AlertingBaseObject):
    def __init__(self, media=None, *args, **kwargs):
        super(NotificationMedia, self).__init__(*args, **kwargs)
        self.value = 'alerting/notification_medium/media'
        self.media = media
        self._etcd_cls = _NotificationMedia


class _NotificationMedia(EtcdObj):
    """A table of the node context, lazily updated

    """
    __name__ = 'alerting/notification_medium'
    _tendrl_cls = NotificationMedia
from holonet.core.manager import ServiceManager

from . import archive
from . import bounce

queues = ServiceManager()

queues.add('archive', archive.ArchiveQueue())
queues.add('bounce', bounce.BounceQueue())

get = queues.get

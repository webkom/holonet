from holonet.core.manager import ServiceManager

from . import archive
from . import bounce
from . import incoming
from . import outgoing
from . import pipeline
from . import retry
from . import virgin

queues = ServiceManager()

queues.add('archive', archive.ArchiveQueue())
queues.add('bounce', bounce.BounceQueue())
queues.add('in', incoming.IncomingQueue())
queues.add('out', outgoing.OutgoingQueue())
queues.add('pipeline', pipeline.PipelineQueue())
queues.add('retry', retry.RetryQueue())
queues.add('virgin', virgin.ViriginQueue())

get = queues.get

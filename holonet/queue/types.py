"""
The vigin queue handles messages constructed by the Holonet system.
"""
VIRGIN = 'virgin'

"""
The outgoing queue is the last stage before a message is sent off to a MTA.
"""
OUTGOING = 'outgoing'

"""
The incoming queue is the first entry for a new message entering the system.
"""
INCOMING = 'incoming'

"""
The bounce queue bounces a message. This is used by messages received by Holonet, but Holonet
does not know what to do with it or it can't be delivered.
"""
BOUNCE = 'bounce'

"""
The archive queue archives the message in the message store.
"""
ARCHIVE = 'archive'

"""
The digest queue stores and process digest for a message.
"""
DIGEST = 'digest'

"""
The pipeline does the lookup and modifies the headers of a message.
"""
PIPELINE = 'pipeline'

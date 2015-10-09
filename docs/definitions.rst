Definitions
-----------

Rules
=====
Rules has a simple task, return True of False. Rules does not manipulate messages. Rules gets
checked by chains and the performs actions based on rule matches. All rules get executed with
mailing_list, message and a metadata dictionary as arguments. Based on these values the rule
decides if it matches or not. Every rule has a record attribute, if this is True, the result of
the rule is stored in the metadata dictionary. It's important to note that the rules themselves
do not dispatch actions based on outcome.

Chains
======
Chains executes rules and acts based on the result. Chains moves messages to other chains or
approves messages and sends them to the pipeline.

Pipeline
========
When the message is approved for posting, it gets sent to the pipeline. The pipeline processes
messages through a set of handlers.

Handlers
========
The handlers task is to manipulate messages by adding/removing headers or change the payloads.
Handlers can also send messages to the different queues.

Queues
======
The queues is where the tasks gets executed. This operations is executed on worker nodes. Typical
queues: virgin, outgoing, incoming, pipeline, archive, digest, bounce.

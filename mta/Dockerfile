FROM phusion/baseimage:latest
MAINTAINER Abakus Webkom <webkom@abakus.no>

ENV DEBIAN_FRONTEND noninteractive

CMD ["/etc/holonet/start.sh"]

RUN set -e \
    && apt-get update \
    && apt-get install -y postfix dovecot-core \
    && apt-get autoremove -y \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

COPY ./etc/ /etc/

# RUN rm -f /etc/service/sshd/down
# ADD key.pub /tmp/key.pub
# RUN cat /tmp/key.pub >> /root/.ssh/authorized_keys && rm -f /tmp/key.pub


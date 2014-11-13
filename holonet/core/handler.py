# -*- coding: utf8 -*-

from .message import HolonetEmailMessage


def handle_mail(msg, sender, recipient):
    message = HolonetEmailMessage(msg, ['eirik@sylliaas.no', 'test@sylliaas.no'])
    message.send()


# -*- coding: utf8 -*-

import email

from django.test import TestCase

from holonet.core.handler import handle_mail


class MailHandlerTestCase(TestCase):

    def test_mail_handler(self):
        res = handle_mail(email.message_from_string("""From eirik@sylliaas.no  Thu Nov 13 17:47:20 2014
Return-Path: <eirik@sylliaas.no>
X-Original-To: eirik@test.abakus.no
From: Eirik Martiniussen Sylliaas <eirik@sylliaas.no>
Content-Type: text/plain; charset=us-ascii
Content-Transfer-Encoding: 7bit
Subject: test
Message-Id: <2901C19D-D44B-4BD8-B0F1-7E9BC283CD93@sylliaas.no>
Date: Thu, 13 Nov 2014 17:15:27 +0100
To: eirik@test.abakus.no
Mime-Version: 1.0 (Mac OS X Mail 8.0 \(1990.1\))
X-Mailer: Apple Mail (2.1990.1)

tetetete
"""), 'eirik@sylliaas.no', 'eirik@test.abakus.no')

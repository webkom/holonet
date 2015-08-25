import smtpd

CRLF = '\r\n'
ERR_451 = '451 Requested action aborted: error in processing'
ERR_501 = '501 Message has defects'
ERR_502 = '502 Error: command HELO not implemented'
ERR_550 = '550 Requested action not taken: mailbox unavailable'
ERR_550_MID = '550 No Message-ID header provided'


class Channel(smtpd.SMTPChannel):
    def __init__(self, server, conn, addr):
        smtpd.SMTPChannel.__init__(self, server, conn, addr)
        self._server = server

    def smtp_LHLO(self, arg):
        smtpd.SMTPChannel.smtp_HELO(self, arg)

    def smtp_HELO(self, arg):
        self.push(ERR_502)

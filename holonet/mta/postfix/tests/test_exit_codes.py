from django.test import TestCase

from holonet.mta.postfix.exit_codes import PostfixPipeExit, PostfixPolicyServiceExit


class ExitCodesTestCase(TestCase):

    def setUp(self):
        self.pipe_exit = PostfixPipeExit()
        self.policy_exit = PostfixPolicyServiceExit()

    def test_pipe_exits(self):
        with self.assertRaisesMessage(SystemExit, str(PostfixPipeExit.DATA_ERROR)):
            self.pipe_exit.data_error()

        with self.assertRaisesMessage(SystemExit, str(PostfixPipeExit.NO_USER)):
            self.pipe_exit.no_recipient()

        with self.assertRaisesMessage(SystemExit, str(PostfixPipeExit.NO_HOST)):
            self.pipe_exit.no_domain()

        with self.assertRaisesMessage(SystemExit, str(PostfixPipeExit.SERVICE_UNAVAILABLE)):
            self.pipe_exit.service_unavailable()

        with self.assertRaisesMessage(SystemExit, str(PostfixPipeExit.SOFTWARE_ERROR)):
            self.pipe_exit.system_error()

    def test_policy_data_error(self):
        self.assertTrue(self.policy_exit.data_error().startswith(
            PostfixPolicyServiceExit.REJECT_ACTION))

    def test_policy_no_recipient(self):
        self.assertTrue(self.policy_exit.no_recipient().startswith(
            PostfixPolicyServiceExit.REJECT_ACTION))

    def test_policy_no_domain(self):
        self.assertTrue(self.policy_exit.no_domain().startswith(
            PostfixPolicyServiceExit.REJECT_ACTION))

    def test_policy_service_unavailable(self):
        self.assertTrue(self.policy_exit.service_unavailable().startswith(
            PostfixPolicyServiceExit.REJECT_ACTION))

    def test_policy_system_error(self):
        self.assertTrue(self.policy_exit.system_error().startswith(
            PostfixPolicyServiceExit.REJECT_ACTION))

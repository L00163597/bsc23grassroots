from django.test import TestCase


class Batman:

    def __init__(self):
        pass

    def serve_justice(self) -> bool:
        bad_guy_in_jail = False
        batman_exists = True

        if batman_exists:
            bad_guy_in_jail = True

        return bad_guy_in_jail


class TestBatman(TestCase):
    def test_serving_justice(self):
        batman = Batman()
        self.assertTrue(batman.serve_justice())

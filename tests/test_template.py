""" Tests for 'project-name' package """
import pytest

from programs import template


def test_helloworld(capsys):
    """ Correct object argument prints """
    template.helloworld("cat")
    captured = capsys.readouterr()
    assert "cat" in captured.out


# This is supposed to fail
def test_helloworld_exception():
    with pytest.raises(TypeError):
        template.helloworld(1)

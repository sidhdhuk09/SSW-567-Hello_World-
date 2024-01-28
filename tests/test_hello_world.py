import pytest
import source.hello_world as hello_world

def test_hello(capsys):
    hello_world.hello_world()
    captured=capsys.readouterr()
    assert captured.out=="Hello World"

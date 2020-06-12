"""Tests for `packymcpackington` package."""
import pytest
from packymcpackington import packymcpackington


def test_convert(capsys):
    """Correct my_name argument prints"""
    packymcpackington.convert("Jill")
    captured = capsys.readouterr()
    assert "Jill" in captured.out
    
        
        

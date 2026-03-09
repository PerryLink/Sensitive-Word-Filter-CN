"""CLI测试"""

from click.testing import CliRunner
from sensitive_word_filter_cn.cli import main
import tempfile
import os


def test_filter_command():
    """测试filter命令"""
    runner = CliRunner()

    with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.txt') as f:
        f.write("傻瓜\n笨蛋\n")
        wordlist_path = f.name

    try:
        result = runner.invoke(main, ['filter', '你是个傻瓜', '-w', wordlist_path])
        assert result.exit_code == 0
        assert '**' in result.output
    finally:
        os.unlink(wordlist_path)


def test_find_command():
    """测试find命令"""
    runner = CliRunner()

    with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.txt') as f:
        f.write("傻瓜\n")
        wordlist_path = f.name

    try:
        result = runner.invoke(main, ['find', '你是个傻瓜', '-w', wordlist_path])
        assert result.exit_code == 0
    finally:
        os.unlink(wordlist_path)


def test_benchmark_command():
    """测试benchmark命令"""
    runner = CliRunner()

    with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.txt') as f:
        f.write("傻瓜\n")
        wordlist_path = f.name

    try:
        result = runner.invoke(main, ['benchmark', '-w', wordlist_path])
        assert result.exit_code == 0
    finally:
        os.unlink(wordlist_path)

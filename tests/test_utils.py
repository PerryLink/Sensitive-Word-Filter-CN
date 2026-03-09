"""工具函数测试"""

from sensitive_word_filter_cn.utils import (
    normalize_text,
    to_pinyin_variants,
    to_traditional_simplified,
    is_chinese_char
)


def test_normalize_text():
    """测试文本规范化"""
    text = "你好*世界!"
    normalized, pos_map = normalize_text(text)

    assert normalized == "你好世界"
    assert len(pos_map) == 4


def test_pinyin_variants():
    """测试拼音变体生成"""
    variants = to_pinyin_variants("傻瓜")

    assert "shagua" in variants
    assert "sg" in variants


def test_traditional_simplified():
    """测试繁简体转换"""
    traditional, simplified = to_traditional_simplified("傻瓜")

    assert traditional == "傻瓜"
    assert simplified == "傻瓜"


def test_is_chinese_char():
    """测试中文字符判断"""
    assert is_chinese_char("你")
    assert is_chinese_char("好")
    assert not is_chinese_char("a")
    assert not is_chinese_char("1")

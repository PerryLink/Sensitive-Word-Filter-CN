"""核心功能测试"""

import pytest
from sensitive_word_filter_cn import SensitiveWordFilter


def test_basic_filter():
    """测试基本过滤功能"""
    filter_obj = SensitiveWordFilter()
    filter_obj.add_word("傻瓜")

    assert filter_obj.contains("你是个傻瓜")
    assert filter_obj.filter("你是个傻瓜") == "你是个**"


def test_pinyin_variant():
    """测试拼音变体检测"""
    filter_obj = SensitiveWordFilter()
    filter_obj.add_word("傻瓜")

    assert filter_obj.contains("你是个shagua")
    assert filter_obj.filter("你是个shagua") == "你是个******"


def test_symbol_interference():
    """测试符号干扰处理"""
    filter_obj = SensitiveWordFilter()
    filter_obj.add_word("傻瓜")

    assert filter_obj.contains("你是个傻*瓜")
    assert filter_obj.filter("你是个傻*瓜") == "你是个***"


def test_traditional_simplified():
    """测试繁简体转换"""
    filter_obj = SensitiveWordFilter()
    filter_obj.add_word("傻瓜")

    # 简体检测繁体
    assert filter_obj.contains("你是個傻瓜")


def test_find_all():
    """测试查找所有敏感词"""
    filter_obj = SensitiveWordFilter()
    filter_obj.add_words(["傻瓜", "笨蛋"])

    matches = filter_obj.find_all("你是个傻瓜和笨蛋")
    assert len(matches) == 2
    assert matches[0].word == "傻瓜"
    assert matches[1].word == "笨蛋"


def test_empty_text():
    """测试空文本"""
    filter_obj = SensitiveWordFilter()
    filter_obj.add_word("傻瓜")

    assert not filter_obj.contains("")
    assert filter_obj.filter("") == ""


def test_no_match():
    """测试无匹配"""
    filter_obj = SensitiveWordFilter()
    filter_obj.add_word("傻瓜")

    text = "你好世界"
    assert not filter_obj.contains(text)
    assert filter_obj.filter(text) == text


def test_batch_add():
    """测试批量添加"""
    filter_obj = SensitiveWordFilter()
    words = ["傻瓜", "笨蛋", "白痴"]
    filter_obj.add_words(words)

    assert filter_obj.get_stats()['word_count'] == 3

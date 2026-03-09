"""性能基准测试"""

import pytest
from sensitive_word_filter_cn import SensitiveWordFilter


@pytest.fixture
def large_filter():
    """创建包含大量敏感词的过滤器"""
    filter_obj = SensitiveWordFilter()
    # 添加1000个测试敏感词
    words = [f"敏感词{i}" for i in range(1000)]
    filter_obj.add_words(words)
    return filter_obj


@pytest.fixture
def long_text():
    """生成长文本"""
    return "这是一段正常的文本。" * 1000


def test_load_performance(benchmark):
    """测试词库加载性能"""
    def load_words():
        filter_obj = SensitiveWordFilter()
        words = [f"敏感词{i}" for i in range(1000)]
        filter_obj.add_words(words)
        return filter_obj

    benchmark(load_words)


def test_filter_performance(benchmark, large_filter, long_text):
    """测试过滤性能"""
    benchmark(large_filter.filter, long_text)


def test_find_all_performance(benchmark, large_filter, long_text):
    """测试查找性能"""
    benchmark(large_filter.find_all, long_text)


def test_contains_performance(benchmark, large_filter, long_text):
    """测试检测性能"""
    benchmark(large_filter.contains, long_text)

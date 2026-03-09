"""使用示例"""

from sensitive_word_filter_cn import SensitiveWordFilter


def main():
    # 创建过滤器
    filter_obj = SensitiveWordFilter()

    # 添加敏感词
    filter_obj.add_words(["傻瓜", "笨蛋", "白痴"])

    # 或从文件加载
    # filter_obj.load_from_file('data/sample_words.txt')

    # 测试文本
    texts = [
        "你是个大傻瓜",
        "你是个shagua",
        "你是个傻*瓜",
        "你是個傻瓜",  # 繁体
        "正常文本"
    ]

    print("=" * 50)
    print("敏感词过滤演示")
    print("=" * 50)

    for text in texts:
        print(f"\n原文: {text}")

        # 检测是否包含敏感词
        if filter_obj.contains(text):
            # 查找所有敏感词
            matches = filter_obj.find_all(text)
            print(f"发现敏感词: {[m.word for m in matches]}")

            # 过滤敏感词
            filtered = filter_obj.filter(text)
            print(f"过滤后: {filtered}")
        else:
            print("✓ 未发现敏感词")

    # 获取统计信息
    print("\n" + "=" * 50)
    print("统计信息:")
    stats = filter_obj.get_stats()
    for key, value in stats.items():
        print(f"  {key}: {value}")


if __name__ == '__main__':
    main()

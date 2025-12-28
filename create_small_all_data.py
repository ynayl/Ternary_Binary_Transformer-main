import pandas as pd

# 定义文件路径和截取行数
config = {
    "train": {"src": "D:/Ternary_Binary_Transformer-main/dataset/cnn_dailymail/train.csv",
              "dst": "D:/Ternary_Binary_Transformer-main/dataset/cnn_dailymail/train_small.csv",
              "n_rows": 300},  # 训练集100行
    "validation": {"src": "D:/Ternary_Binary_Transformer-main/dataset/cnn_dailymail/validation.csv",
                   "dst": "D:/Ternary_Binary_Transformer-main/dataset/cnn_dailymail/validation_small.csv",
                   "n_rows": 100},  # 验证集50行
    "test": {"src": "D:/Ternary_Binary_Transformer-main/dataset/cnn_dailymail/test.csv",
             "dst": "D:/Ternary_Binary_Transformer-main/dataset/cnn_dailymail/test_small.csv",
             "n_rows": 100}  # 测试集25行
}

# 批量生成小文件（避免CSV格式错误）
for data_type, cfg in config.items():
    try:
        # 读取原始数据，跳过损坏行
        df = pd.read_csv(cfg["src"], encoding="utf8", on_bad_lines="skip")
        # 截取前n行，重置索引
        small_df = df.head(cfg["n_rows"]).reset_index(drop=True)
        # 保存为格式正确的CSV
        small_df.to_csv(
            cfg["dst"],
            index=False,
            encoding="utf8",
            quoting=1  # 强制引号转义，避免解析错误
        )
        print(f" {data_type}小文件生成完成：{cfg['dst']}，共{len(small_df)}行")
    except FileNotFoundError:
        print(f" {data_type}原始文件不存在：{cfg['src']}，跳过")
    except Exception as e:
        print(f" {data_type}生成失败：{e}")
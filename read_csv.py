import pandas as pd
import csv

df = pd.read_csv(
    '/data3/fujinji/Kaggle_Chatbot/code/input/lmsys-chatbot-arena/train_copy.csv',
    dtype=str,
    engine='python',   # 一定要强制使用 python 解析器
    quoting=csv.QUOTE_NONE,   # 忽略所有引号
    on_bad_lines='skip'
)

print(len(df))

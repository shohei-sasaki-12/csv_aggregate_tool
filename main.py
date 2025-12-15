import pandas as pd
import os

print('[INFO] Processing started.')

try:
    # csv読み込み
    input_path = os.path.join(os.getcwd(), 'input.csv')
    df = pd.read_csv(input_path)
    print('[INFO] Loaded ' + str(df.shape[0]) + ' rows.')

    # 数値以外の値をNaNに変換
    df['amount'] = pd.to_numeric(df['amount'], errors='coerce')
    print('[INFO] Skipped ' + str(df['amount'].isnull().sum()) + ' invalid rows.')

    # 集計
    col = ['sum', 'mean', 'max', 'min', 'count']
    df_group = df.groupby('category')['amount'].agg(col).reset_index()

    # float表示の場合、「.0」が残るため以下の処理で整数表示にする
    for i in col:
        df_group[i] = df_group[i].apply(lambda x: f"{x:.15g}")

    # csv書き込み
    output_path = os.path.join(os.getcwd(), 'output_summary.csv')
    df_group.to_csv(output_path, index=False)   # indexは出力しない

except FileNotFoundError:   # ファイルが見つからない
    print('[INFO] File not found.')

else:
    print('[INFO] Summary saved to output.csv.')
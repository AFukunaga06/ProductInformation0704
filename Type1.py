def extract_jan_codes(input_file):
    with open(input_file, "r", encoding="utf-8") as infile:
        for line in infile:
            if "JANコード" in line:
                jan_code = line.split('\t')[1].strip()  # テキストの2番目のタブの数値を取得
                print(jan_code)  # コマンドプロンプトに出力

# 入力ファイルのパスを指定
input_file = "input.txt"

# 関数を実行
extract_jan_codes(input_file)

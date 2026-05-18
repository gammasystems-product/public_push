import re

def count_text_segments(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # 区切り文字を正規表現で定義
        # ===== または @@SEPARATOR@@ を区切りとして分割
        # re.splitで分割すると、区切り文字自身もリストに含まれるため、それを考慮します
        segments = re.split(r'(=====|@@SEPARATOR@@)', content)

        # 最初のブロック（最初の区切り文字の前）から処理開始        
        block_count = 1
        for i in range(0, len(segments), 2):
            text_block = segments[i]

            if text_block:
                print(f"--- ブロック {block_count} ---")
                print(f"文字数: {len(text_block)}文字")
                # print(f"内容冒頭: {text_block[:30]}...") # 必要であれば内容の冒頭を表示（確認用）
                print("-" * 20)
                block_count += 1
            if i + 1 < len(segments):
                print(f"[区切り文字発見: {segments[i+1]}]\n") # 区切り文字が存在すれば表示


    except FileNotFoundError:
        print("指定されたファイルが見つかりません。")
    except Exception as e:
        print(f"エラーが発生しました: {e}")

# ファイル名を指定して実行
file_name = 'sample.txt'  # ここを対象のファイルパスに変更してください
count_text_segments(file_name)
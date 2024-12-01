import pdfplumber
import os
import argparse

def extract_text_from_pdf(pdf_path, output_path):
    try:
        # PDFファイルを開く
        with pdfplumber.open(pdf_path) as pdf:
            # 全ページのテキストを格納するリスト
            text_content = []
            
            # 各ページからテキストを抽出
            for page in pdf.pages:
                # ページからテキストを抽出（レイアウトを保持）
                text = page.extract_text(layout=True)
                if text:
                    text_content.append(text)
            
            # 抽出したテキストを結合
            full_text = '\n\n'.join(text_content)
            
            # テキストファイルに書き出し
            with open(output_path, 'w', encoding='utf-8') as output_file:
                output_file.write(full_text)
                
            print(f"テキストの抽出が完了しました。出力先: {output_path}")
            
    except Exception as e:
        print(f"エラーが発生しました: {str(e)}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Process a target file.")
    
    # 必須の引数
    parser.add_argument(
        "relative_path",
        type=str,
        help="The relative path from the current directory to the target file."
    )
    
    
    args = parser.parse_args()

    # 処理対象のファイルを絶対パスに変換
    file_path = os.path.abspath(args.relative_path)
    
    # 出力テキストファイルのパス
    output_path = file_path.replace(".pdf", ".txt")     
    # PDFが存在することを確認
    if not os.path.exists(file_path):
        print(f"エラー: PDFファイルが見つかりません: {file_path}")
    else:
        # テキスト抽出を実行
        extract_text_from_pdf(file_path, output_path)

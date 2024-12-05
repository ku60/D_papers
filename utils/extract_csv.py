import pandas as pd
import os
import argparse

def excel_to_csv(excel_path):
    try:
        # 出力ファイル名を作成（同じディレクトリに.csvとして保存）
        output_path = os.path.splitext(excel_path)[0] + '.csv'
        
        # Excelファイルを読み込み
        df = pd.read_excel(excel_path)
        
        # CSVとして保存
        df.to_csv(output_path, index=False, encoding='utf-8')
        
        print(f"変換が完了しました。出力先: {output_path}")
            
    except Exception as e:
        print(f"エラーが発生しました: {str(e)}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="ExcelファイルをCSVに変換します")
    
    # 必須の引数
    parser.add_argument(
        "excel_path",
        type=str,
        help="Excelファイルへの相対パスまたは絶対パス"
    )
    
    args = parser.parse_args()
    
    # 処理対象のファイルを絶対パスに変換
    file_path = os.path.abspath(args.excel_path)
    
    # ファイルの存在確認
    if not os.path.exists(file_path):
        print(f"エラー: ファイルが見つかりません: {file_path}")
    else:
        # 変換を実行
        excel_to_csv(file_path)
from utils.extract_txt import extract_text_from_pdf
import glob
import os
import argparse

def extract_txts(folder_path, output_path):
    pdf_files = glob.glob(os.path.join(folder_path, '*.pdf'))

    for pdf_file in pdf_files:
        output_path = pdf_file.replace(".pdf", ".txt")     
        extract_text_from_pdf(pdf_file, output_path)

if __name__ == "__main__":
    
    parser = argparse.ArgumentParser(description="Process a target file.")
    
    # 必須の引数
    parser.add_argument(
        "relative_path",
        type=str,
        help="The relative path from the current directory to the target file."
    )
    
    args = parser.parse_args()

    extract_txts(args.relative_path, "data/txt")
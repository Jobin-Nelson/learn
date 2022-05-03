'''Sets up the environment for reading books'''
from typing import Optional, Sequence
import subprocess, argparse

def main(argv: Optional[Sequence[str]] = None) -> int:
    '''Opens Sumatra PDF Viewer and Visual Studio Code'''
    parser = argparse.ArgumentParser(description='opens reader with or wihout text editor')
    parser.add_argument('-c', '--vscode', action='store_true', help='opens vs code in the book code directory')
    args = parser.parse_args(argv)


    sumatra_path = r'C:\Users\jobin\AppData\Local\SumatraPDF\SumatraPDF.exe'
    vs_code_path = r'C:\Users\jobin\AppData\Local\Programs\Microsoft VS Code\bin\code.CMD'
    book_code_path = r'C:\Users\jobin\playground\learn\Python\Book_code\impractical_python_projects'

    if args.vscode: 
        subprocess.Popen([vs_code_path, book_code_path])
    subprocess.Popen(sumatra_path)
    return 0

if __name__ == '__main__':
    raise SystemExit(main())

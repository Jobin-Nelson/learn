'''
Renames american date style files into european date style
'''
import shutil, os, re, pathlib

def main():
    # generate pattern to identify american dates 13-30
    pattern = re.compile(r'^(\D*)([10]?\d)-(1[3-9]|2[0-9]|3[10])-(19\d\d|20\d\d|\d\d)(.*?)$')

    # get file names and identify the american ones 
    path = pathlib.Path.cwd() / 'test'
    for file in os.listdir(path):
        mo = pattern.match(file)
        if mo is None:
            continue
        before_part, month, date, year, after_part = mo.groups()
        euro_name = f'{before_part}{date}-{month}-{year}{after_part}'

        # rename the matched files
        shutil.move(path / file, path / euro_name)
        print(f'Renaming {path/file} to {path/euro_name}')

if __name__ == '__main__':
    main()

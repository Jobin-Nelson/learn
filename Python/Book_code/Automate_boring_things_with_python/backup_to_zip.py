'''
Copies an entire folder and its contents into a zip file whose filename increments
'''
import zipfile, os


def main():
    backupToZip('test')

def backupToZip(path: str) -> None:
    '''Back up the entire contents of the folder into a zip file'''
    # get the full path
    folder = os.path.abspath(path)

    # generate zipfilename
    number = 1
    while True:
        zipfilename = os.path.basename(f'{folder}_{number}.zip')
        if not os.path.exists(zipfilename):
            break
        number += 1
    
    # create zip
    print(f'Creating {zipfilename}...')
    with zipfile.ZipFile(zipfilename, 'w') as z:
        for foldername, subfolders, files in os.walk(folder):
            print(f'Adding {foldername} to zip')
            z.write(foldername)

            for file in files:
                new_base = os.path.basename(folder) + '_'
                if file.startswith(new_base) and file.endswith('.zip'):
                    continue
                print(f'Adding {file} to zip')
                z.write(os.path.join(folder, file))
    print('done.')

if __name__ == '__main__':
    main()

import os
import argparse
import patoolib #pip install patool
import platform

rar_program = None
if (platform.system() == "Windows"):
    rar_program = r"C:\Program Files\WinRAR\UnRAR.exe"

def unrar_files(root, files):
    for file in files:
        filename, file_extension = os.path.splitext(file)
        if (file_extension == ".rar"):
            print("rar file: ", file)
            file_to_extract = os.path.join(root, file)
            print ("to extract: ", file_to_extract)
            patoolib.extract_archive(file_to_extract, outdir=root, program = rar_program, interactive=False)
        if (".part" in file):
            break

def delete_rar_files(root, files):
    for file in files:
        filename, file_extension = os.path.splitext(file)
        print ("ext: ", file_extension[:-2])
        if (file_extension[:2] == ".r"):
            print ("Removing: ", os.path.join(root, file))
            os.remove(os.path.join(root, file))

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-l', '--launch_directory',help='directory to use',action='store')
    args = parser.parse_args()
    print ("Unrarer starting in: ", args.launch_directory)

    for root, dirs, files in os.walk(args.launch_directory, followlinks=True):
        try:
            unrar_files(root, files)
            delete_rar_files(root, files)
        except:
            print ("Something went wrong: ", root)

if __name__ == '__main__':
    main()

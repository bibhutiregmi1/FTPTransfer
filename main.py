from process import FTPFunction
import sys

def main(filename):
    try:
        print(filename)
        f = FTPFunction()
        f.downloadFile(filename)
        f.file_split(filename)
        for i in f.file_list:
            f.uploadFile(i)
    except:
        print("Error occured!")

if __name__ == "__main__":
    main(str(sys.argv[1]))
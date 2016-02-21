import threading, zipfile, os, tarfile
'''
Alternative version of execution zipping, includes using threads. At this moment is not used in main program, but can be simple attached
'''

class AsyncZipFile(threading.Thread):

    def __init__(self, dirPath, filePath):
        threading.Thread.__init__(self)
        self.filePath = filePath
        self.dirPath = dirPath

    def run(self):
        f = zipfile.ZipFile(self.filePath, 'w', zipfile.ZIP_DEFLATED)
        for root, dirs, files in os.walk(self.dirPath):
            print root
            for file in files:
                f.write(os.path.join(root, file))
                print os.path.join(root, file)
        f.close()


class AsyncTarFile(AsyncZipFile, threading.Thread):

    def __init__(self, dirPath, filePath):
        threading.Thread.__init__(self)
        self.filePath = filePath
        self.dirPath = dirPath

    def run(self):
        compr_meth = "w:gz"
        f = tarfile.open(self.filePath, compr_meth)
        f.add(self.dirPath, arcname = "TarName")
        f.close()

def main():
    background_thread_zip = AsyncZipFile(r'C:\Users\lozoxmac\Documents\Trainings', r'C:\Users\lozoxmac\Documents\file.zip')
    background_thread_zip.start();
    background_thread_zip.join()
    background_thread_tar = AsyncTarFile(r'C:\Users\lozoxmac\Documents\Trainings', r'C:\Users\lozoxmac\Documents\file.tar.gz')
    background_thread_tar.start();
    background_thread_tar.join()
    print "Zipping was ended"
if __name__ == '__main__':
    main()
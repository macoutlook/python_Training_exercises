import os
import zipfile
import tarfile
from zipfile import ZipFile


class ZipFolder(object):
    """
    base class which provides method for zippers classes
    """
    def __init__(self, dir_path):
        self.folder_path = dir_path

    def get_zipped_file_size(self):
        """
        checking size of zipped file regardless method of zipping
        :return:
        """
        self.zip_file_size = os.path.getsize(self.zip_file_path)

    def get_path_for_zip(self):
        """
        Getting path for zipped file regardless method of zipping
        :return:
        """
        folder_elements = self.folder_path.split("\\")
        zip_file_name = folder_elements[-2]
        result =''

        for element in folder_elements[:-2]:
            result = result + element + '\\'
        zip_folder_path = result

        return os.path.join(zip_folder_path, zip_file_name)


class ZipFolder_zipfile(ZipFolder):
    """
    This class uses zipfile class as compression method
    """

    def zip_with_ZipFile(self, zip_compression = zipfile.ZIP_DEFLATED):
        """
        this method implements compression of dir with zipfile class
        :param zip_compression:
        :return:
        """
        self.label_of_method = "zip"
        path_for_zip = self.get_path_for_zip()
        self.zip_file_path = path_for_zip + ".zip"
        self.zip_file = ZipFile(self.zip_file_path, 'w', zip_compression)
        # print path_for_zip
        for root, dirs, files in os.walk(self.folder_path):
            #print root
            for file in files:
                self.zip_file.write(os.path.join(root, file))
                # print os.path.join(root, file)


class ZipFolder_tarfile(ZipFolder):
    """
    This class uses tarfile class as compression method
    """

    def zip_with_tarfile(self, compr_meth = "w:gz"):
        """
        Compression of dir with tarfile class
        :return:
        """
        self.label_of_method = compr_meth
        path_for_zip = self.get_path_for_zip()
        self.zip_file_path = path_for_zip + ".tar.gz"
        # "w:gz" lets using other compression method, w:bz2
        self.zip_file = tarfile.open(self.zip_file_path, compr_meth)
        self.zip_file.add(self.folder_path, arcname = "TarName")
        self.zip_file.close()

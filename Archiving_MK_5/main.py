import argparse
import ZipFolder
import utilities


def main():
    compress_lvl_lst = []
    #To calculate compression_ratio: compression_ratio = Uncompressed_Size / Compressed_Size
    #parsing argument - path to folder which should be zipped
    parser = argparse.ArgumentParser()
    parser.add_argument("path_to_folder", type=str, help="Give path to directory which should be zipped")
    args = parser.parse_args()

    #getting uncompressed folder size
    folder_size = utilities.get_folder_size(args.path_to_folder)
    print folder_size

    #creating object for class zipfile and calculating its volume and compression level
    zip_folder_zf = ZipFolder.ZipFolder_zipfile(args.path_to_folder)
    zip_folder_zf.zip_with_ZipFile()
    zip_folder_zf.get_zipped_file_size()
    print zip_folder_zf.zip_file_size
    compr_zf = utilities.calculate_compression(folder_size, zip_folder_zf.zip_file_size)

    #creating object for class tarfile and calculating its volume and compression level
    zip_folder_tf = ZipFolder.ZipFolder_tarfile(args.path_to_folder)
    zip_folder_tf.zip_with_tarfile()
    zip_folder_tf.get_zipped_file_size()
    print zip_folder_tf.zip_file_size
    compr_tf = utilities.calculate_compression(folder_size, zip_folder_tf.zip_file_size)

    #creating object for class tarfile and bzw compression method and calculating its volume and compression level
    zip_folder_tf_bz2 = ZipFolder.ZipFolder_tarfile(args.path_to_folder)
    zip_folder_tf_bz2.zip_with_tarfile("w:bz2")
    zip_folder_tf_bz2.get_zipped_file_size()
    print zip_folder_tf_bz2.zip_file_size
    compr_tf_bz2 = utilities.calculate_compression(folder_size, zip_folder_tf_bz2.zip_file_size)

    #creating list with compression levels and creating plot
    compress_lvl_lst.append(compr_zf)
    compress_lvl_lst.append(compr_tf)
    compress_lvl_lst.append(compr_tf_bz2)
    compress_name_lvl_lst = []
    compress_name_lvl_lst.append(zip_folder_zf.label_of_method)
    compress_name_lvl_lst.append(zip_folder_tf.label_of_method)
    compress_name_lvl_lst.append(zip_folder_tf_bz2.label_of_method)
    utilities.create_plot(folder_size, compress_lvl_lst, compress_name_lvl_lst)

if __name__ == '__main__':
    main()
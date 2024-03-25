import zipfile

def extract_archive(archivepath, dest_dir):
    with zipfile.ZipFile(archivepath, 'r') as archive:
        archive.extractall(dest_dir)


if __name__ == "__main__":
    extract_archive("/Users/linxin/PycharmProjects/pythonMegaCourse/app1/bonus/compressed.zip",
                    "/Users/linxin/PycharmProjects/pythonMegaCourse/app1/bonus/files")
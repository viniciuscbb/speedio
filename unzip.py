import zipfile


class Unzipper:
    def __init__(self, file_path):
        self.file_path = file_path

    def unzip_file(self):
        print(f'Descompactando {self.file_path}...')

        zipdata = zipfile.ZipFile(f'./files/{self.file_path}.zip')
        zipinfos = zipdata.infolist()

        for zipinfo in zipinfos:
            zipinfo.filename = f'{self.file_path}.csv'
            zipdata.extract(zipinfo, './csv')
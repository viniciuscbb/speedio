import requests, sys, time

class Downloader:
    def __init__(self, file_name, url):
        self.file_name = f'{file_name}.zip'
        self.url = url
        self.start = time.perf_counter()

    def download_file(self):
        print(f'Baixando arquivo: {self.file_name}')
        with open(f'./files/{self.file_name}', 'wb') as f:
            r = requests.get(self.url, stream=True)
            total_length = int(r.headers.get('content-length'))
            dl = 0
            if total_length is None:
                f.write(r.content)
            else:
                for chunk in r.iter_content(1024):
                    dl += len(chunk)
                    f.write(chunk)
                    done = int(30 * dl / total_length)
                    sys.stdout.write("\r[%s%s] %s Mbps" % ('=' * done, ' ' * (30-done), dl//(time.perf_counter() - self.start) / 100000))
        return (time.perf_counter() -  self.start)
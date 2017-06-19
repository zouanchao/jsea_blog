# coding:UTF-8
from django.http import StreamingHttpResponse
from common.utils.utils_log import log


def big_file_download(file,file_name_s):
    # do something...

    def file_iterator(file_name, chunk_size=512):
                f = open(file_name, "rb")
                while True:
                    c = f.read(chunk_size)
                    if c:
                        yield c
                    else:
                        break
                f.close()
    # file_name_s = file.split("/")[-1]
    response = StreamingHttpResponse(file_iterator(file))
    response['Content-Type'] = 'application/octet-stream'
    response['Content-Disposition'] = 'attachment;filename="{0}"'.format(file_name_s)
    return response

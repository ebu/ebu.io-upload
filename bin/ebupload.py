import requests
import os
import sys

HOST = "ebu.io"
URL = "http://{}/downloads/upload/".format(HOST)

if len(sys.argv) != 3:
    print("Usage: {}: token filename".format(sys.argv[0]))
    exit(1)
else:
    if not os.path.exists(sys.argv[2]):
        sys.stderr.write("file {} does not exist\n".format(sys.argv[2]))
        exit(2)
    files = {'file':open(sys.argv[2])}
    param = {'token':sys.argv[1]}
    print("uploading to {}".format(URL))
    resp = requests.post(URL, files=files, data=param)
    if resp.ok:
        print("upload done")
    else:
        sys.stderr.write("error {} \n".format(resp.content))

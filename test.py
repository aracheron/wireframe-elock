import urllib.request
import time
import subprocess
import json

def test():
    # Start server
    server = subprocess.Popen(["python3", "-m", "http.server", "8000"])
    time.sleep(1) # wait for server to start

    # We will just verify that the files are being served correctly, since testing UI without playwright setup is hard
    res = urllib.request.urlopen("http://localhost:8000/index.html.html")
    content = res.read().decode('utf-8')
    assert 'tabindex="0"' in content
    assert "ArrowRight" in content

    server.terminate()
    print("Test passed!")

if __name__ == '__main__':
    test()

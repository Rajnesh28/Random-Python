import urllib.request

def main():
    try:
        weburl = urllib.request.urlopen("http://www.google.com")
        print("result code: ", weburl.getcode())
        data = weburl.read()
        print(data)
    except:
        print("Exception thrown")
if __name__ == "__main__":
    main()

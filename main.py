import urllib.request

from selenium_master import


def photo_saver(url_):
    try:
        urllib.request.urlopen(url_)
    except urllib.error.URLError as e:
        print("Ошибка при скачивании фото:", e)
    else:
        try:
            with open(f'captcha.jpg', 'wb') as f:
                f.write(urllib.request.urlopen(url_).read())
                print("Фото успешно скачано!")
        except Exception:
            print("Ошибка при скачивании фото:")

    try:


    except Exception as e:
        sys.exit(e)

    else:
        sys.exit('solved: ' + str(result))
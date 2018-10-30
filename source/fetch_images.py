import json
import requests
import time

json_data = open("heroes.json").read()
data = json.loads(json_data)


def dl_image(url, name):
    time.sleep(0.5)
    print(url)
    print(name)
    with open(name, 'wb') as handle:
        response = requests.get(url, stream=True)

        if not response.ok:
            print(response)

        for block in response.iter_content(1024):
            if not block:
                break

            handle.write(block)


for hero in data:
    dl_image(hero['url_full_portrait'], "img/{}_{}.png".format(hero['id'], "full"))
    dl_image(hero['url_small_portrait'], "img/{}_{}.png".format(hero['id'], "sb"))
    dl_image(hero['url_large_portrait'], "img/{}_{}.png".format(hero['id'], "lg"))
    dl_image(hero['url_vertical_portrait'], "img/{}_{}.jpg".format(hero['id'], "vert"))

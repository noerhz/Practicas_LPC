import requests
import os
import re


def load_photo(input_url):
    req = requests.Session()
    offset = 0

    while True:
        url = "{}{}".format(input_url, offset)
        res = req.get(url, cookies=cookies)
        html = res.text
        match = re.findall(r"/photo.php\?fbid=([0-9]*)&amp;", html)
        if match:
            for m in match:
                f = open("{}/{}.jpg".format(friend_id, m),"wb")
                res = req.get("https://mbasic.facebook.com/photo/view_full_size/?fbid={}".format(m), cookies=cookies)
                html = res.text
                z = re.search(r"a href=\"(.*?)\"", html)
                if z:
                    url = str(z.groups()[0]).replace("&amp;", "&")
                    res = req.get(url, cookies=cookies)
                    f.write(res.content)
                    f.close()
                else:
                    break
            offset+=12
            print(offset)
        else:
            break


cookies = {
    "c_user": "100001046347658",
    "xs": "25%3AsnbqCSA9Jeqcpg%3A2%3A1633396366%3A-1%3A5573%3A%3AAcVkTCUs72NBKnmyIk6k1_cDmPrmTgq1Pt7POJTN3Q"
}
friend_id = "100005024646601"

if __name__ == "__main__":
    if not os.path.exists(friend_id):
        os.makedirs(friend_id)

    url_photo_tag = "https://mbasic.facebook.com/{}/photoset/pb.{}.-2207520000../?owner_id={}&offset=".format(friend_id, friend_id, friend_id)
    url_photo_upload = "https://mbasic.facebook.com/{}/photoset/t.{}/?owner_id={}&offset=".format(friend_id, friend_id, friend_id)

    load_photo(url_photo_tag)
    load_photo(url_photo_upload)

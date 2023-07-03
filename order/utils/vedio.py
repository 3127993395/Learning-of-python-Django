import re
import requests


def get_old_view_count(video_url):
    for _ in range(5):
        try:
            res = requests.get(
                url=video_url,
                headers={
                    "user_agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.43",
                    "refer": "https://m.yangshipin.cn/",
                }
            )
            match_object = re.findall(r'"subtitle":"(.+)次观看","', res.text)
            if not match_object:
                return True, 0
            return True,match_object[0]
        except Exception:
            pass
    return False, 0


if __name__ == '__main__':
    count = get_old_view_count("https://w.yangshipin.cn/video?type=0&vid=f0000711h22")
    print(count)
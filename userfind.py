import sys
import requests

# Teste un pseudo sur plusieurs sites et dit sur lesquels un profil existe.
# On se contente de regarder le code HTTP de la page de profil (public).
# Principe de base d'outils OSINT comme Sherlock, en beaucoup plus simple.

SITES = {
    "GitHub": "https://github.com/{}",
    "Reddit": "https://www.reddit.com/user/{}",
    "Instagram": "https://www.instagram.com/{}",
    "TikTok": "https://www.tiktok.com/@{}",
    "Twitch": "https://www.twitch.tv/{}",
}

UA = {"User-Agent": "Mozilla/5.0 (userfind)"}


def exists(url):
    try:
        r = requests.get(url, headers=UA, timeout=8, allow_redirects=True)
    except requests.RequestException:
        return None
    return r.status_code == 200


def run(username):
    print(f"recherche de '{username}'\n")
    for name, pattern in SITES.items():
        url = pattern.format(username)
        res = exists(url)
        if res is True:
            print(f"[trouve]  {name:<10} {url}")
        elif res is False:
            print(f"[rien]    {name}")
        else:
            print(f"[erreur]  {name}")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("usage: python userfind.py <pseudo>")
    else:
        run(sys.argv[1])

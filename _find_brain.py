import urllib.request

url = "https://icaidiet26.tech/assets/index-Bx72zHDS.js"
js = urllib.request.urlopen(url, timeout=60).read().decode("utf-8", "replace")
open(r"e:\website\snsgroups\SNS-Groups\_icaidiet.js", "w", encoding="utf-8").write(js)
low = js.lower()
print("len", len(js), "brain", low.count("brain"))
idx = 0
hits = 0
while hits < 20:
    i = low.find("brain", idx)
    if i < 0:
        break
    hits += 1
    print("\n---", i, "---")
    print(js[max(0, i - 200): i + 400])
    idx = i + 5
print("HITS", hits)

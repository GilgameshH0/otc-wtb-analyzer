from telethon import TelegramClient, events

api_id = ''
api_hash = ''

client = TelegramClient('mirror', api_id, api_hash)

client.start()
main = []
projects = []
for message in client.iter_messages(-1001244789214, 5000):
    s = message.text.upper()
    if "WTB" in s and "WL" in s:
        lines = s.split("\n")
        for l in lines:
            if "WL" in l:
                scp = str(message.sender_id) + ':' + l[:l.index("WL")]
                final = l[:l.index("WL")]
                if "SPRA" in l[:l.index("WL")]:
                    print(message.text)
                if scp in main:
                    continue
                else:
                    main.append(scp)
                    projects.append(final)

doned = []
for p in projects:
    d = p + ": " + str(projects.count(p))
    if d in doned:
        continue
    else:
        doned.append(d)
        print(d)
                
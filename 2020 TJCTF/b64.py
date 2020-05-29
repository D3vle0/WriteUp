import sys
import base64

a = 'eyIxIjpmYWxzZSwiMiI6ZmFsc2UsIjMiOmZhbHNlLCI0IjpmYWxzZSwiNSI6ZmFsc2UsIjYiOnRydWUsIjciOnRydWUsIjgiOnRydWUsIjkiOnRydWUsIjEwIjp0cnVlfQ=='.encode('utf-8')
print(base64.b64decode(a))
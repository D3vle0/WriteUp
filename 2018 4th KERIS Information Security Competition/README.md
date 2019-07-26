# KERIS 제 4회 정보보안 경진대회 Write-up
---
## Network 1
[FINDme.pcapng](https://github.com/developleo/keris-writeup/blob/master/%EA%B2%BD%EC%A7%84%EB%8C%80%ED%9A%8C/writeup/%EB%84%A4%ED%8A%B8%EC%9B%8C%ED%81%AC1/FINDme.pcapng) 파일이 주어진다. pcapng 파일은 패킷 캡쳐 파일이므로, Wireshark 로 열어준다.  

![0.PNG](https://raw.githubusercontent.com/developleo/keris-writeup/master/%EA%B2%BD%EC%A7%84%EB%8C%80%ED%9A%8C/writeup/%EB%84%A4%ED%8A%B8%EC%9B%8C%ED%81%AC1/0.PNG)

처음에는 1440번 Packet 에 있는 success.txt 파일이 수상해서 분석해보았지만 아무런 결과가 없었다.  
flag 값 자체가 전송된 패킷이 있는지 FIlter Option 에  
```
frame contains flag
```
이렇게 입력을 하니 1470번 단 하나의 Packet 이 검색되었다.

![1.png](https://raw.githubusercontent.com/developleo/keris-writeup/master/%EA%B2%BD%EC%A7%84%EB%8C%80%ED%9A%8C/writeup/%EB%84%A4%ED%8A%B8%EC%9B%8C%ED%81%AC1/1.PNG)

![2.png](https://raw.githubusercontent.com/developleo/keris-writeup/master/%EA%B2%BD%EC%A7%84%EB%8C%80%ED%9A%8C/writeup/%EB%84%A4%ED%8A%B8%EC%9B%8C%ED%81%AC1/2.PNG)

우클릭 > Follow > TCP Stream 으로 들어가면...

![3.png](https://raw.githubusercontent.com/developleo/keris-writeup/master/%EA%B2%BD%EC%A7%84%EB%8C%80%ED%9A%8C/writeup/%EB%84%A4%ED%8A%B8%EC%9B%8C%ED%81%AC1/3.PNG)

플래그를 구할 수 있다.  
### flag{N3tw0rk_Ch@llenge_SOlv3d!_Congr@tz!!}   
---
## Cryptography 1
[XOR](https://github.com/developleo/keris-writeup/blob/master/%EA%B2%BD%EC%A7%84%EB%8C%80%ED%9A%8C/XOR) 파일이 주어진다. 텍스트 에디터로 열면   
>$.#%96-&#;b+1b!.-7&;lb1-b/;b$''.+,%b+1b,-6b%--&b'+6*'0l? 
>
이런 값이 나오는데 문제 힌트에 따르면 flag와 특정 문자 한 개를 XOR 연산한 것이라고 한다. [xor_app](http://blog.naver.com/PostView.nhn?blogId=wwwkasa&logNo=220121139415) 이라는 툴을 사용하면 편하다. 참고로 이 툴을 다운로드 받았을 때 확장자가 .exe_ 로 되어있을 것이다.

![1.png](https://raw.githubusercontent.com/developleo/keris-writeup/master/%EA%B2%BD%EC%A7%84%EB%8C%80%ED%9A%8C/writeup/%EC%95%94%ED%98%B8%ED%99%941/1.PNG)

exe로 바꿔서 실행한 뒤 입력란에 xor 된 값을 붙어넣는다.

![2.png](https://raw.githubusercontent.com/developleo/keris-writeup/master/%EA%B2%BD%EC%A7%84%EB%8C%80%ED%9A%8C/writeup/%EC%95%94%ED%98%B8%ED%99%941/2.PNG)

![3.png](https://raw.githubusercontent.com/developleo/keris-writeup/master/%EA%B2%BD%EC%A7%84%EB%8C%80%ED%9A%8C/writeup/%EC%95%94%ED%98%B8%ED%99%941/3.PNG)

### flag{today is cloudy. so my feeling is not good either.} 
---
## Web 1
![1.png](https://raw.githubusercontent.com/developleo/keris-writeup/master/%EA%B2%BD%EC%A7%84%EB%8C%80%ED%9A%8C/writeup/%EC%9B%B91/1.PNG)

문제 설명에 admin으로 접속하라길래 특정 ID/PW 가 있는 줄 알았는데 이내 SQL Injection 이라는 것을 알았다. SQL Injection 이란 악의적인 SQL문을 넣어서 DB를 비정상적으로 조작하는 웹 해킹 기법이다. 

![2.png](https://raw.githubusercontent.com/developleo/keris-writeup/master/%EA%B2%BD%EC%A7%84%EB%8C%80%ED%9A%8C/writeup/%EC%9B%B91/2.PNG)

로그인 없이 PW를 참으로 만들기 위해 ID 와 PW에
```
OR 1=1 --'
```
을 써주면...

![3.png](https://raw.githubusercontent.com/developleo/keris-writeup/master/%EA%B2%BD%EC%A7%84%EB%8C%80%ED%9A%8C/writeup/%EC%9B%B91/3.PNG)

alert() 로 flag 값이 나온다.
### flag{I_4m_k1ng_0f_tH2_w0rlD!}
---
##Web 2

![1.png](https://raw.githubusercontent.com/developleo/keris-writeup/master/%EA%B2%BD%EC%A7%84%EB%8C%80%ED%9A%8C/writeup/%EC%9B%B92/1.PNG)

특정 사진 파일을 조각내서 무작위로 섞어 놓은 페이지이다.  
처음에는 Burp Suite 로 무작위로 섞이는 함수 (스트립트) 를 중지 시키고 원본의 사진을 불러와야 하는 줄 알았는데 Ctrl + Shift + I 로 개발자 도구를 꺼내서

![2.png](https://raw.githubusercontent.com/developleo/keris-writeup/master/%EA%B2%BD%EC%A7%84%EB%8C%80%ED%9A%8C/writeup/%EC%9B%B92/2.PNG)

섞일 사진이 있는 위치 (top > 13.124.40.205 > img > th1s_1s_r3al_f14g) 를 찾아가면 플래그를 볼 수 있다.

![3.png](https://raw.githubusercontent.com/developleo/keris-writeup/master/%EA%B2%BD%EC%A7%84%EB%8C%80%ED%9A%8C/writeup/%EC%9B%B92/3.PNG)

### flag{PuzZ13_pUzZ13_f0R_fuN_!@#$}
---

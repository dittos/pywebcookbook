가상 환경
-------------

### 용도

가상환경은 실제 OS 에서 사용되는 파이썬 인터프리터 및 패키지들과 어플리케이션에서 사용할 환경을 격리하는 역활을 합니다. 각각의 어플리케이션들은 각기 다른 패키지들을 사용하는데 각기 다른 운영 환경을 필요로 할 가능성이 있습니다.

### 사용법

#### 가상환경 설치

	$ pip install virtualenv

#### 가상환경 생성

ENV 라는 가상환경을 생성합니다. 실제로 ENV 라는 디렉토리가 생기며 관련 라이브러리와 설정파일들이 복사되게 됩니다.

	$ virtualenv ENV


#### 가상환경 활성화

쉘에서 가상 환경을 활성화 하는 방법입니다. 먼저 가상환경의 디렉토리에 들어가서 다음과 같은 명령을 내립니다.

	$ source bin/activate


### 조언

 * 개발은 가상환경에서 하십시오.

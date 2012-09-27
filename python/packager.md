패키지 관리자
-------------

### pypi

pypi는 파이썬 패키지 인덱스의 약자로서 http://pypi.python.org/pypi 에서 제공되는 서비스입니다. 개발자들이 직접 올려놓은 패키지들을 검색하고 다운받을수 있습니다.

### pip

pip 는 pypi 에서 패키지를 내려받아 설치해주고 관리해주는 툴입니다. easy_install 보다 후에 나왔으며 pip 의 사용을 좀 더 권장합니다. 

다음과 같이 패키지를 설치합니다.

	$ pip install simplejson

다음과 같이 패키지를 업그레이드 합니다.

	$ pip install -u simplejson

다음과 같이 설치된 패키지들의 리스트를 받아옵니다.

	$ pip freeze

다음과 같이 설치된 패키지들의 리스트를 requirements.txt 에 저장합니다.

	$ pip freeze > requirements.txt

freeze 명령어로 저장된 패키지들을 설치하려면 다음과 같이 합니다.

	$ pip install -r requirements.txt
	
### easy_install

setuptools 라는 패키지의 일부로 패키지를 설치할때 쓰입니다. 기본적으로 파이썬 배포판에 들어있는 경우가 많습니다. 보통은 pip 를 설치하는 용도로 쓰입니다.

	$ easy_install pip
	

### OS 에서 제공하는 패키지 관리자

각 OS 에서 제공하는 python 패키지들이 있습니다. 안정적이지만 대부분 버젼이 낮은 경우가 많습니다.

	$ # 우분투의 경우
	$ apt-get install python-pip

### 조언 

 * 바이너리 의존성이 있는 패키지 설치를 위해서는 pip 나 easy_install 설치 이전에 컴파일러와 개발 환경을 설치해야하는 경우가 많습니다.
 * 위의 세가지 방법중 가급적 하나로 통일해서 사용하시기 바랍니다.

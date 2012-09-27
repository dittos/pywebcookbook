SQLAlchemy 시작하기
-----------------

*이 장은 SQL에 대한 기본 지식이 필요합니다.*

[SQLAlchemy](http://sqlalchemy.org)는 파이썬에서 MySQL 등의 데이터베이스를 쉽게 사용할 수 있게 해주는 라이브러리입니다. 크게 파이썬 코드로 SQL 쿼리를 생성하고 실행하는 것을 담당하는 Core 부분과, 파이썬 객체를 DB에 저장하거나 DB에서 다시 파이썬 객체를 읽어오는 작업을 도와주는 ORM 부분으로 구성되어 있습니다. 이 문서에서는 주로 ORM에 대해서 다룰 것입니다.

### 엔진 생성

SQLAlchemy가 DB에 접근하려면, DB 접속 정보를 알아야 합니다. 이러한 접속 정보를 받아서 연결을 관리하는 객체가 `Engine`입니다. `sqlalchemy.create_engine` 함수에 데이터베이스 접속 주소를 넘겨 엔진을 생성할 수 있습니다.

지금은 일단 파이썬 표준 라이브러리로 포함되어 있는 SQLite를 사용하도록 하겠습니다. (물론 MySQL, MS-SQL, Oracle, PostgreSQL 등 다양한 RDBMS를 지원하니 걱정하지 않으셔도 됩니다.) 또한, 앞으로 어떤 SQL문이 실행되는지 살펴보기 위해 `echo` 옵션을 켜겠습니다.

	from sqlalchemy import create_engine
	engine = create_engine('sqlite:///test.db', echo=True)
	
### 매핑 선언

SQLAlchemy ORM은 파이썬의 객체들이 어떤 식으로 DB에 저장될지 선언해주면 알아서 객체를 저장하고 불러오는 일을 해줍니다. 먼저 이러한 대응 정보를 관리하는 기반 클래스를 만들고, ORM이 관리할 클래스에서 상속받아야 합니다. 기반 클래스는 `sqlalchemy.ext.declarative.declarative_base` 함수로 만듭니다.

	from sqlalchemy.ext.declarative import declarative_base
	Base = declarative_base()
	
이제 ORM이 관리하는 클래스를 만들어보겠습니다. 위에서 만든 `Base` 클래스를 상속합니다. 매핑 선언은 SQL 테이블 스키마를 짜는 것과 상당히 비슷합니다.

	from sqlalchemy import Column, Integer, Unicode, String
	
	class Store(Base):
		__tablename__ = 'stores'
		
		id = Column(Integer, primary_key=True)
		name = Column(Unicode(50), nullable=False)
		phone = Column(String(20))
		
* `stores` 테이블에 대응되는 `Store` 클래스를 선언했습니다.
* `id`라는 이름의 대표 키 필드를 선언합니다. ORM을 사용하기 위해서는 대표 키 필드가 반드시 하나 이상 존재해야 합니다. `Column`의 첫번째 인자로는 필드의 자료형을 지정해줍니다.
* `name`과 `phone` 필드를 선언했습니다. `Unicode`와 `String` 자료형에는 길이를 지정할 수 있습니다. 또한 모든 필드는 `NULL`(파이썬의 `None`)을 저장할 수 있는 것이 기본값인데, 상점 이름이 NULL일 수는 없으므로 `nullable`을 껐습니다.

### 테이블 생성

매핑 선언으로부터 테이블을 만들 수 있습니다. 매핑 선언이 실제로 저장되는 곳은 `Base.metadata`이고, 메타데이터 객체의 `create_all` 메소드를 호출하면 `Base`가 알고 있는 모든 테이블이 생성됩니다. 메타데이터는 엔진과 독립적이므로 `engine` 객체를 직접 넘겨줍니다.

	Base.metadata.create_all(engine)
	
앞에서 `echo` 옵션을 켰기 때문에 실행되는 SQL문이 출력될 것입니다.

	CREATE TABLE stores (
		id INTEGER NOT NULL, 
		name VARCHAR(50) NOT NULL, 
		phone VARCHAR(20), 
		PRIMARY KEY (id)
	)

### 더 알아보기

* [SQLAlchemy가 지원하는 DB 종류와 접속 주소 형식](http://docs.sqlalchemy.org/en/latest/core/engines.html#database-urls)
* [`Column`에 추가로 지정할 수 있는 옵션들](http://docs.sqlalchemy.org/en/latest/core/schema.html#sqlalchemy.schema.Column.__init__)
* [`Column`에 지정할 수 있는 자료형 목록](http://docs.sqlalchemy.org/en/latest/core/types.html)
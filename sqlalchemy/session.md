SQLAlchemy: 세션
---------------

세션 객체는 ORM의 모든 작업을 관장하는 역할을 합니다. DB에서 객체를 꺼내올 때, 아니면 아직 DB에 저장된 적이 없는 객체를 추가할 때 세션 객체를 사용합니다.

### 세션 만들기

세션을 만들 때는 직접 SQLAlchemy의 `Session` 클래스를 부르는 것이 아니라, `sqlalchemy.orm.sessionmaker` 함수로 세션 팩토리를 만든 뒤에 다시 팩토리를 호출하여 세션을 만듭니다.

	from sqlalchemy.orm import sessionmaker
	Session = sessionmaker(bind=engine)

이제 DB를 사용할 곳에서 `Session` 인스턴스를 만듭니다.

	session = Session()

### 객체 추가하기

`Base` 클래스를 상속하면 자동으로 생성자를 만들어줍니다. 기본 생성자는 키워드 인자를 받아서 해당하는 필드에 값을 넣어줍니다. 예를 들어 예제로 선언한 `Store` 객체를 다음과 같이 만들 수 있습니다.

	store = Store(name=u'나의 가게', phone='02 9999 9999')

그렇지만 이 객체는 아직 DB에 저장되지 않았습니다. 먼저 세션에 객체를 추가해야 합니다.

	session.add(store)

그러면 바로 DB에 저장이 되는 걸까요? 아직 아닙니다. 실제로 SQL 문이 실행되기 위해서는 `flush` 메소드를 불러야 합니다. 그리고 세션은 기본적으로 데이터베이스의 트랜잭션을 활성화시키기 때문에 커밋 명령까지 내려야 비로소 DB에 반영될 것입니다. `commit` 메소드는 `flush`와 트랜잭션 커밋을 한번에 해줍니다. 따라서,

	session.commit()
	
을 실행하면 다음 쿼리가 순서대로 실행되는 것을 볼 수 있습니다.

	BEGIN
	INSERT INTO stores (…)
	COMMIT

그리고 자동으로 할당된 `id` 값이 `store.id`에 들어갑니다.

### 객체 고치기

객체의 속성을 바꾼 뒤 DB에 반영하려면 어떻게 해야할까요? 보통 객체의 속성을 바꾸는 것과 마찬가지로 하면, SQLAlchemy 세션이 알아서 그것을 감지하여 객체를 `dirty` 상태로 바뀝니다. 이 변경 사항을 `commit`하면 실제로 DB에 저장이 되겠죠.

	store.name = u'우리 가게'
	session.commit()
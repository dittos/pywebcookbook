# -*- coding: utf-8 -*-

from getting_started import engine, Store

from sqlalchemy.orm import sessionmaker
Session = sessionmaker(bind=engine)

session = Session()

store = Store(name=u'나의 가게', phone='02 9999 9999')
session.add(store)
session.commit()
print store.id

store.name = u'우리 가게'
session.commit()

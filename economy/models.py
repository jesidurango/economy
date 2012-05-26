from sqlalchemy import (
    Column,
    Integer,
    Text,
    ForeignKey,
    DECIMAL,
    )
from sqlalchemy.types import BIGINT

from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.orm import (
    scoped_session,
    sessionmaker,
    )

from zope.sqlalchemy import ZopeTransactionExtension

DBSession = scoped_session(sessionmaker(extension=ZopeTransactionExtension()))
Base = declarative_base()

class BaseEntity(object):
    __table_args__ = {
        'mysql_engine': 'InnoDB',
        'mysql_charset': 'utf8'
    }

class MyModel(Base):
    __tablename__ = 'models'
    id = Column(Integer, primary_key=True)
    name = Column(Text, unique=True)
    value = Column(Integer)

    def __init__(self, name, value):
        self.name = name
        self.value = value

class Product(Base, BaseEntity):
    __tablename__ = 'ec_product'
    id = Column('product_id', BIGINT(unsigned = True), primary_key = True)
    name = Column(Text, nullable=False)
    product_value = Column(DECIMAL(precision = 8, scale = 2))

class Calculate(Base, BaseEntity):
    __tablename__ = 'ec_calculate'
    id = Column('calculate_id', BIGINT(unsigned = True), primary_key = True)
    product_id = Column(BIGINT(unsigned = True)), ForeignKey('ec_product.product_id', name='fk_calculate_product',
            onupdate='RESTRICT', ondelete='RESTRICT', nullable=False)


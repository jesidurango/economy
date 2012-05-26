from sqlalchemy import (
    Column,
    String,
    ForeignKey,
    DECIMAL,
    )
from sqlalchemy.types import BIGINT
from sqlalchemy.types import DateTime
from sqlalchemy.orm import relationship

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

class User(Base, BaseEntity):
    __tablename__ = 'ec_users'
    id = Column('user_id', BIGINT(unsigned = True), primary_key = True)
    user_name = Column(String(20), nullable=False)
    password = Column(String(12), nullable=False)
    registration_date = Column(DateTime)

    def __init__(self, user_name, password, registration_date):
        self.user_name = user_name
        self.password = password
        self.registration_date = registration_date

class Calculate(Base, BaseEntity):
    __tablename__ = 'ec_calculate'
    id = Column('calculate_id', BIGINT(unsigned = True), primary_key = True)
    product_name = Column(String(60), nullable=False)
    product_value = Column(DECIMAL(precision = 8, scale = 2))
    interest_rate = Column(DECIMAL(precision=4, scale=2))
    user_id = Column(BIGINT(unsigned=True), ForeignKey('ec_users.user_id', name='fk_users_calculate',
            onupdate='RESTRICT', ondelete='RESTRICT'), nullable=False)
    unser_name = relationship('User', passive_deletes=True, passive_updates=True)

    def __init__(self, product_name, user_id, product_value, interest_rate):
        self.product_name = product_name
        self.user_id = user_id
        self.product_value = product_value
        self.interest_rate = interest_rate



from sqlalchemy import (
    Column,
    Integer,
    String,
    Text,
    DateTime,
    UniqueConstraint,
)
from datetime import datetime

from ...database import Base


class PatentModel(Base):
    __tablename__ = 'patents'

    id = Column(Integer, primary_key=True)
    patent_number = Column(String(128), nullable=False)
    jurisdiction = Column(String(128), nullable=False)
    app_grp_art_number = Column(String(128))
    country_code = Column(String(128))
    document_number = Column(String(128))
    kind_code = Column(String(128))
    primary_identifier = Column(String(256))
    abstract_text = Column(Text)
    applicant = Column(String(256))
    inventors = Column(String(256))
    title = Column(String(256))
    url = Column(String(500))
    grant_date = Column(DateTime)
    submission_date = Column(DateTime)
    updated_at = Column(
        DateTime,
        default=datetime.utcnow,
        onupdate=datetime.utcnow,
    )

    __table_args__ = (UniqueConstraint('patent_number', 'jurisdiction'),)

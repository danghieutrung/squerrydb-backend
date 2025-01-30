from sqlalchemy import Column, String, Integer, Boolean, ForeignKey, DECIMAL
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()

class Series(Base):
    __tablename__ = "series"

    tconst = Column(String, primary_key=True)
    titletype = Column(String, nullable=False)
    primarytitle = Column(String, nullable=False)
    originaltitle = Column(String, nullable=False)
    isadult = Column(Boolean, nullable=False)
    startyear = Column(Integer, nullable=True)
    endyear = Column(Integer, nullable=True)
    runtimeminutes = Column(Integer, nullable=True)
    genres = Column(String, nullable=True)
    averagerating = Column(DECIMAL(3, 1), nullable=False)
    numvotes = Column(Integer, nullable=False)

    episodes = relationship("Episode", back_populates="parent", cascade="all, delete")

class Episode(Base):
    __tablename__ = "episodes"

    tconst = Column(String, primary_key=True)
    parenttconst = Column(String, ForeignKey("series.tconst", ondelete="CASCADE"), nullable=False)
    seasonnumber = Column(Integer, nullable=False)
    episodenumber = Column(Integer, nullable=False)
    titletype = Column(String, nullable=False)
    primarytitle = Column(String, nullable=False)
    originaltitle = Column(String, nullable=False)
    isadult = Column(Boolean, nullable=False)
    startyear = Column(Integer, nullable=True)
    endyear = Column(Integer, nullable=True)
    runtimeminutes = Column(Integer, nullable=True)
    genres = Column(String, nullable=True)
    averagerating = Column(DECIMAL(3, 1), nullable=False)
    numvotes = Column(Integer, nullable=False)

    parent = relationship("Series", back_populates="episodes")
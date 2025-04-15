from sqlalchemy import Column, Integer, String, DateTime, Boolean, TIMESTAMP, Enum
from manage.db import Base
import enum

class ClinicStatus(enum.Enum):
    SCHEDULED = "Scheduled"
    IN_PROGRESS = "In progress"
    CLOSED = "Closed"
    CANCELLED = "Cancelled"

class ClinicType(enum.Enum):
    ASSESSMENT = "Assessment"
    SCREENING = "Screening"

class RiskType(enum.Enum):
    MIXED_RISK = "Mixed risk"
    ROUTINE_RISK = "Routine risk"
    MOBILE = "Mobile"

class Clinic(Base):
    __tablename__ = 'clinics'
    id = Column(Integer, primary_key=True)
    setting = Column(String(255), nullable=False)
    starts_at = Column(TIMESTAMP, nullable=False)
    ends_at = Column(TIMESTAMP, nullable=False)
    location = Column(String(255), nullable=False)
    status = Column(Enum(ClinicStatus), nullable=False, default=ClinicStatus.SCHEDULED)
    type = Column(Enum(ClinicType), nullable=False, default=ClinicType.SCREENING)
    risk_type = Column(Enum(RiskType), nullable=False, default=RiskType.MIXED_RISK)
    
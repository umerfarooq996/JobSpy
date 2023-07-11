from typing import Union
from datetime import datetime
from enum import Enum

from pydantic import BaseModel


class JobType(Enum):
    FULL_TIME = "fulltime"
    PART_TIME = "parttime"
    CONTRACT = "contract"
    TEMPORARY = "temporary"
    INTERNSHIP = "internship"

    PER_DIEM = "perdiem"
    NIGHTS = "nights"
    OTHER = "other"


class Location(BaseModel):
    country: str
    city: str = None
    state: str = None
    postal_code: str = None
    address: str = None


class CompensationInterval(Enum):
    YEARLY = "yearly"
    MONTHLY = "monthly"
    WEEKLY = "weekly"
    DAILY = "daily"
    HOURLY = "hourly"


class Compensation(BaseModel):
    interval: CompensationInterval
    min_amount: float
    max_amount: float
    currency: str = "US"


class JobPost(BaseModel):
    title: str
    company_name: str
    job_url: str
    location: Location

    description: str = None
    job_type: JobType = None
    compensation: Compensation = None
    date_posted: datetime = None


class JobResponse(BaseModel):
    success: bool
    error: str = None

    job_count: int = None
    jobs: list[JobPost] = []

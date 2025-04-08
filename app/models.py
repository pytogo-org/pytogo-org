from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime


class Speaker(BaseModel):
    name: str
    title: str
    image_url: str


class ScheduleItem(BaseModel):
    time: str
    title: str
    description: Optional[str] = None


class Event(BaseModel):
    id: int
    title: str
    description: str
    short_description: str
    category: str
    date: str
    time: str
    location: str
    venue_address: Optional[str] = None
    image_url: str
    status: str  # "upcoming", "ongoing", or "past"
    speakers: Optional[List[Speaker]] = []
    schedule: Optional[List[ScheduleItem]] = []



new_event = Event(
    id=1,
    title="PyDay Togo 2024",
    description="""Learn how to use Python for data analysis and visualization in this full-day workshop. This
        workshop is perfect for beginners who want to get started with data science using Python.
        
        Topics covered include:
        - Introduction to Python for data analysis
        - Data manipulation with pandas
        - Numerical computing with numpy
        - Data visualization with matplotlib and seaborn
        - Introduction to machine learning with scikit-learn
        
        Participants should bring their own laptops with Python installed. We will provide
        instructions for setting up your environment before the workshop.""",
    short_description="Learn how to use Python for data analysis and visualization. This workshop covers pandas, numpy, and matplotlib.",
    category="Conference",
    date="30 November 2024",
    time="09:00 - 17:00",
    location="Institute Polytechnic Defitech",
    venue_address="Sito-Aéroport, Lomé, Togo",
    image_url="/static/images/events/pyday.jpeg",
    status="upcoming",
    speakers=[
        Speaker(
            name="Dr. Kodjo Adade",
            title="Data Scientist, University of Lomé",
            image_url="/static/images/speakers/kodjo_adade.jpg",
        ),
        Speaker(
            name="Dr. Ama Serwaa",
            title="Data Scientist, University of Accra",
            image_url="/static/images/speakers/ama_serwaa.jpg",
        ),
    ],
    schedule=[
        ScheduleItem(
            time="09:00 - 09:30",
            title="Registration",
            description="Sign in and get your name badge."
        ),
        ScheduleItem(
            time="09:30 - 10:00",
            title="Opening Remarks",
            description="Welcome to PyDay Togo 2024! Learn about the day's schedule and what to expect."
        ),
        ScheduleItem(
            time="10:00 - 11:00",
            title="Introduction to Python for Data Analysis",
            description="Learn the basics of Python and how to use it for data analysis."
        ),
        ScheduleItem(
            time="11:00 - 12:00",
            title="Data Manipulation with Pandas",
            description="Explore the pandas library for data manipulation and analysis."
        ), 

    ],
)

print(new_event.dict())
from supabase import create_client, Client

from dotenv import load_dotenv
import os   


load_dotenv()

url: str = os.getenv("SUPABASE_URL")
key: str = os.getenv("SUPABASE_KEY")



client: Client = create_client(url, key)

# response = client.table("user").insert({"name": "Pluto"}).execute()

# print(response)
# responses = (
#     client.table('user')
#     .select('*')
#     .execute()
# )


# events

event = dict(
    {
        
        "title": "PyDay Togo 2024",
        "description": """Learn how to use Python for data analysis and visualization in this full-day workshop. This
            workshop is perfect for beginners who want to get started with data science using Python.
            
            Topics covered include:
            - Introduction to Python for data analysis
            - Data manipulation with pandas
            - Numerical computing with numpy
            - Data visualization with matplotlib and seaborn
            - Introduction to machine learning with scikit-learn
            
            Participants should bring their own laptops with Python installed. We will provide
            instructions for setting up your environment before the workshop.""",
        "short_description": "Learn how to use Python for data analysis and visualization. This workshop covers pandas, numpy, and matplotlib.",
        "category": "Conference",
        "date": "30 November 2024",
        "start_date": "30 November 2024 09:00 GMT",
        "end_date": "30 November 2024 17:00 GMT",
        "time": "09:00 - 17:00",
        "location": "Institute Polytechnic Defitech",
        "venue_address": "Sito-Aéroport, Lomé, Togo",
        "image_url": "/static/images/events/pyday.jpeg",
        "status": "upcoming",
        "speakers": [
            {
                "name": "Dr. Kodjo Adade",
                "title": "Data Scientist, University of Lomé",
                "image_url": "/static/images/speakers/kodjo_adade.jpg",
            },
            {
                "name": "Ama Sika",
                "title": "Python Developer, Tech Togo",
                "image_url": "/static/images/speakers/ama_sika.jpg",
            },
            {
                "name": "Pascal Mensah",
                "title": "ML Engineer, AI Africa",
                "image_url": "/static/images/speakers/pascal_mensah.jpg",
            },
        ],
        "schedule": [
            {
                "time": "09:00 - 09:30",
                "title": "Registration and Setup",
                "description": "Get set up with the workshop environment and materials",
            },
            {
                "time": "09:30 - 11:00",
                "title": "Introduction to Python for Data Science",
                "description": "Overview of Python and its data science ecosystem",
            },
            {
                "time": "11:00 - 12:30",
                "title": "Data Manipulation with Pandas",
                "description": "Learn how to load, clean, and transform data",
            },
            {"time": "12:30 - 13:30", "title": "Lunch Break", "description": ""},
            {
                "time": "13:30 - 15:00",
                "title": "Data Visualization",
                "description": "Creating effective visualizations with matplotlib and seaborn",
            },
            {
                "time": "15:00 - 16:30",
                "title": "Introduction to Machine Learning",
                "description": "Basic ML concepts and implementing simple models with scikit-learn",
            },
            {
                "time": "16:30 - 17:00",
                "title": "Q&A and Wrap-up",
                "description": "Final questions and next steps",
            },
        ],
    },
)



# response = client.table("events").insert(event).execute()

responses = (
    client.table('events')
    .select('*')
    .execute()
)

print(responses.data[0]["schedule"])



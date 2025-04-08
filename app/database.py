from datetime import datetime, timezone, timedelta

import random
import json

hero_images = [
    "https://res.cloudinary.com/dvg7vky5o/image/upload/v1744070856/hero_iapsxz.jpg",
    "https://res.cloudinary.com/dvg7vky5o/image/upload/v1744070811/groupe_picture_accra_rudcom.jpg",
    "https://res.cloudinary.com/dvg7vky5o/image/upload/v1744070808/pycon_lezpmd.jpg",
    "https://res.cloudinary.com/dvg7vky5o/image/upload/v1744070949/WUL_0456_qerwtk.jpg",
]

events_data = [
    {
        "id": 1,
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
    {
        "id": 2,
        "title": "PyCon Togo 2024",
        "description": "The biggest Python conference in Togo. Three days of talks, workshops, and networking with Python enthusiasts from across West Africa.",
        "short_description": "The biggest Python conference in Togo. Three days of talks, workshops, and networking.",
        "category": "Conference",
        "date": "Coming Soon",
        "start_date": "30 November 2024 09:00 GMT",
        "end_date": "30 November 2024 17:00 GMT",
        "time": "All day",
        "location": "Institute Polytechnic Defitech",
        "venue_address": "Sito-Aéroport, Lomé, Togo",
        "image_url": "/static/images/events/pyday_togo.JPG",
        "status": "ongoing",
        "speakers": [],
        "schedule": [],
    },
    {
        "id": 3,
        "title": "PyCon Togo 2025",
        "description": "The biggest Python conference in Togo. Three days of talks, workshops, and networking with Python enthusiasts from across West Africa.",
        "short_description": "The biggest Python conference in Togo. Three days of talks, workshops, and networking.",
        "category": "Conference",
        "date": "Coming Soon",
        "start_date": "30 November 2025 09:00 GMT",
        "end_date": "30 November 2025 17:00 GMT",
        "time": "All day",
        "location": "Coming Soon",
        "venue_address": "Coming Soon",
        "image_url": "/static/images/events/pyday_togo.JPG",
        "status": "ongoing",
        "speakers": [],
        "schedule": [],
    },
    {
        "id": 3,
        "title": "Django Web Development",
        "description": "Learn how to build web applications using Django, the Python web framework for perfectionists with deadlines.",
        "short_description": "Learn how to build web applications using Django, the Python web framework.",
        "category": "Meetup",
        "date": "15 April 2025",
        "start_date": "15 April 2025 18:00 GMT",
        "end_date": "15 April 2025 20:00 GMT",
        "time": "18:00 - 20:00",
        "location": "Coming Soon",
        "venue_address": "45 Rue des Entrepreneurs, Lomé",
        "image_url": "/static/images/events/django_meetup.webp",
        "status": "upcoming",
        "speakers": [],
        "schedule": [],
    },
    {
        "id": 4,
        "title": "What is Python and Why Should You Learn It?",
        "description": "What is Python and why should you learn it? In this workshop, we'll cover the basics of Python and how it can be used for data analysis, web development, and more.",
        "short_description": "What is Python and why should you learn it? In this workshop, we'll cover the basics of Python.",
        "category": "Blog",
        "date": datetime.now(timezone.utc).strftime("%d %B %Y"),
        "start_date": datetime.now(timezone.utc).strftime("%d %B %Y %H:%M %Z"),
        "end_date": (
            (datetime.now(timezone.utc) + timedelta(days=1)).strftime(
                "%d %B %Y %H:%M %Z"
            )
        ),
        "time": datetime.now(timezone.utc).strftime("%H:%M %Z"),
        "location": "Coming Soon",
        "venue_address": "45 Rue des Entrepreneurs, Lomé",
        "image_url": "/static/images/events/What-is-Python.jpg",
        "status": "upcoming",
        "speakers": [],
        "schedule": [],
    },
]


teams_members = [
    {
        "name": "Wachiou BOURAIMA",
        "role": "President | Co-founder",
        "image": "https://res.cloudinary.com/dvg7vky5o/image/upload/v1744072317/wass_lejeso.jpg",
    },
    {
        "name": "Agnilonda PAKOU",
        "role": "Vice-President | co-founder",
        "image": "https://res.cloudinary.com/dvg7vky5o/image/upload/v1744072312/pakou_rks87v.jpg",
    },
    {
        "name": " Geoffrey LOGOVI",
        "role": "Executive Director | co-founder",
        "image": "https://res.cloudinary.com/dvg7vky5o/image/upload/v1744072313/geoffrey_bfcnl4.png",
    },
    {
        "name": "Parfait TOKE",
        "role": "General Councillor | co-founder",
        "image": "https://res.cloudinary.com/dvg7vky5o/image/upload/v1744072320/parfait_gvjg7z.jpg",
    },
    {
        "name": "Laboré kodjo AGBETSIASSI",
        "role": "Education, Training and Mentoring Managers | co-founder",
        "image": "https://res.cloudinary.com/dvg7vky5o/image/upload/v1744072336/labore_bamkph.jpg",
    },
    {
        "name": "Samadou OURO-AGOROUKO",
        "role": "Education, Training and Mentoring Managers | co-founder",
        "image": "https://res.cloudinary.com/dvg7vky5o/image/upload/v1744072312/samadou_hpu656.jpg",
    },
    {
        "name": "Irène AMEDJI",
        "role": "Head of Communications and Design | Co-founder",
        "image": "https://res.cloudinary.com/dvg7vky5o/image/upload/v1744072311/irene_avrtzw.jpg",
    },
    {
        "name": "Yves HOUANGASSI",
        "role": "Head of Communications and Design | Co-founder",
        "image": "https://res.cloudinary.com/dvg7vky5o/image/upload/v1744072323/yves_m5ijgw.png",
    },
    {
        "name": "Samira AMADOU",
        "role": "Partnerships and External Relations Advisor | Co-founder",
        "image": "https://res.cloudinary.com/dvg7vky5o/image/upload/v1744072314/samira_x3b53b.jpg",
    },
    {
        "name": "Emmanuel AMELA",
        "role": "Deputy Secretary | Co-founder",
        "image": "https://res.cloudinary.com/dvg7vky5o/image/upload/v1744072309/emmanuel_fgzpks.jpg",
    },
    {
        "name": "Medede BIDASSA",
        "role": "Treasurer | co-founder",
        "image": "https://res.cloudinary.com/dvg7vky5o/image/upload/v1744072309/happy_fqkpto.jpg",
    },
    {
        "name": "Waficah OLOSSOUMARE",
        "role": "Deputy Treasurer | Co-founder",
        "image": "https://res.cloudinary.com/dvg7vky5o/image/upload/v1744072333/waficah2_iebump.jpg",
    },
    {
        "name": "Akinwumi OGUNDIPE",
        "role": "Product Designer | Core Contributor",
        "image": "https://res.cloudinary.com/dvg7vky5o/image/upload/v1744072311/akinwumi_nei6fq.jpg",
    },
]

galleries = [
    {
        "url": "https://res.cloudinary.com/dvg7vky5o/image/upload/v1744070809/pyconafrica20241_syencp.jpg",
        "caption": "Community networking session",
        "height": random.randrange(30, 60),
    },
    {
        "url": "https://res.cloudinary.com/dvg7vky5o/image/upload/v1744070809/pyconafrica20242_qg88cd.jpg",
        "caption": "PyCon Africa 2024 Team",
        "height": random.randrange(30, 60),
    },
    {
        "url": "https://res.cloudinary.com/dvg7vky5o/image/upload/v1744070815/pyconafrica20243_dtrdhr.jpg",
        "caption": "Python workshop for beginners",
        "height": random.randrange(30, 60),
    },
    {
        "url": "https://res.cloudinary.com/dvg7vky5o/image/upload/v1744070870/WUL_0426_md0krb.jpg",
        "caption": "Keynote presentation",
        "height": random.randrange(30, 60),
    },
    {
        "url": "https://res.cloudinary.com/dvg7vky5o/image/upload/v1744070989/WUL_0338_sktoqk.jpg",
        "caption": "Networking during coffee break",
        "height": random.randrange(30, 60),
    },
    {
        "url": "https://res.cloudinary.com/dvg7vky5o/image/upload/v1744070811/groupe_picture_accra_rudcom.jpg",
        "caption": "Hackathon winning team",
        "height": random.randrange(30, 60),
    },
    {
        "url": "https://res.cloudinary.com/dvg7vky5o/image/upload/v1744070949/WUL_0456_qerwtk.jpg",
        "caption": "Conference venue entrance",
        "height": random.randrange(30, 60),
    },
    {
        "url": "https://res.cloudinary.com/dvg7vky5o/image/upload/v1744070862/WUL_0433_1_wuak8r.jpg",
        "caption": "Keynote presentation",
        "height": random.randrange(30, 60),
    },
    {
        "url": "https://res.cloudinary.com/dvg7vky5o/image/upload/v1744070878/WUL_0433_vdmj2j.jpg",
        "caption": "Keynote presentation",
        "height": random.randrange(30, 60),
    },
    {
        "url": "https://res.cloudinary.com/dvg7vky5o/image/upload/v1744070808/pycon_lezpmd.jpg",
        "caption": "PyConAfrica",
        "height": random.randrange(30, 60),
    },
    {
        "url": "https://res.cloudinary.com/dvg7vky5o/image/upload/v1744070948/WUL_0468_1_pdlydh.jpg",
        "caption": "PyDay Togo 2024",
        "height": random.randrange(30, 60),
    },
    {
        "url": "https://res.cloudinary.com/dvg7vky5o/image/upload/v1744070841/WUL_0317_vyezwq.jpg",
        "caption": "Keynote presentation",
        "height": random.randrange(30, 60),
    },
    {
        "url": "https://res.cloudinary.com/dvg7vky5o/image/upload/v1744070843/WUL_0393_arlbnx.jpg",
        "caption": "Keynote presentation",
        "height": random.randrange(30, 60),
    },
    {
        "url": "https://res.cloudinary.com/dvg7vky5o/image/upload/v1744070975/WUL_0481_krzjew.jpg",
        "caption": "Networking during coffee break",
        "height": random.randrange(30, 60),
    },
    {
        "url": "https://res.cloudinary.com/dvg7vky5o/image/upload/v1744070824/WUL_0390_uaf6ac.jpg",
        "caption": "Keynote presentation",
        "height": random.randrange(30, 60),
    },
    {
        "url": "https://res.cloudinary.com/dvg7vky5o/image/upload/v1744070968/WUL_0468_bcodxc.jpg",
        "caption": "Python in Africa",
        "height": random.randrange(30, 60),
    },
    {
        "url": "https://res.cloudinary.com/dvg7vky5o/image/upload/v1744070872/WUL_0434_b7vxhx.jpg",
        "caption": "Keynote presentation",
        "height": random.randrange(30, 60),
    },
    {
        "url": "https://res.cloudinary.com/dvg7vky5o/image/upload/v1744070913/WUL_0440_m1kzzu.jpg",
        "caption": "Keynote presentation",
        "height": random.randrange(30, 60),
    },
    {
        "url": "https://res.cloudinary.com/dvg7vky5o/image/upload/v1744070954/WUL_0469_spgjme.jpg",
        "caption": "attendees networking",
        "height": random.randrange(30, 60),
    },
    {
        "url": "https://res.cloudinary.com/dvg7vky5o/image/upload/v1744070900/WUL_0437_1_wmcpun.jpg",
        "caption": "attendee questions",
        "height": random.randrange(30, 60),
    },
]

parteners = [
    {
        "name": "Python Software Foundation",
        "logo_url": "https://res.cloudinary.com/dvg7vky5o/image/upload/v1744077536/psf-logo_xk6r0e.png",
        "symbol": "PSF",
    },
    {
        "name": "Python Ghana",
        "logo_url": "https://res.cloudinary.com/dvg7vky5o/image/upload/v1744077536/pyghana_jvziwn.png",
        "symbol": "pyghana-logo",
    },
    {
        "name": "Hyever",
        "logo_url": "https://res.cloudinary.com/dvg7vky5o/image/upload/v1744077535/hyver_niqoii.png",
        "symbol": "hyver-logo",
    },
    {
        "name": "Tech Communities Day",
        "logo_url": "https://res.cloudinary.com/dvg7vky5o/image/upload/v1744077535/tcd_ejwwzi.png",
        "symbol": "tcd-logo",
    },
    {
        "name": "Amazing Girls In Tech",
        "logo_url": "https://res.cloudinary.com/dvg7vky5o/image/upload/v1744077535/amz_girls_ppdv9h.png",
        "symbol": "amz_girls-logo",
    },
    {
        "name": "TEDx VITChennai",
        "logo_url": "https://res.cloudinary.com/dvg7vky5o/image/upload/v1744077536/tedx_wet3rx.png",
        "symbol": "tcd-logo",
    },
    {
        "name": "Africa Blockchain Community",
        "logo_url": "https://res.cloudinary.com/dvg7vky5o/image/upload/v1744077536/abc-logo-full_hlu0uj.png",
        "symbol": "abc-logo",
    },

]

# [{"url": "", "caption": "", "data-height": random.randrange(30, 60)}]
swags = [
    {
        "name": "Python Togo T-Shirt",
        "description": "Proudly represent the Python Togo community with our official t-shirt. Made from high-quality cotton.",
        "price": 3500,
        "originalPrice": 5000,
        "images": [
            "/static/images/swags/tshirt.png",
        ],
    },
    {
        "name": "Python Togo Travel Mugs & Tumblers",
        "description": "This tumbler boasts a large capacity and an ergonomic handle for a comfortable hold.",
        "price": 2500,
        "originalPrice": 5000,
        "images": [
            "/static/images/swags/thunder.png",
            "/static/images/swags/bootle.png",
        ],
    },
    {
        "name": "Python Togo Hoodie",
        "description": "Stay warm with our Python Togo hoodie. Perfect for coding nights and meetups.",
        "price": 7500,
        "originalPrice": 9000,
        "images": [
            "/static/images/swags/hoodie.png",
        ],
    },
    {
        "name": "Python Togo Cap",
        "description": "Complete your tech look with our exclusive Python Togo cap. Adjustable and comfortable.",
        "price": 2500,
        "originalPrice": 3500,
        "images": [
            "/static/images/swags/cap.png",
        ],
    },
    {
        "name": "Python Togo Stickers",
        "description": "Decorate your laptop, phone, and more with our Python Togo stickers. Durable and waterproof.",
        "price": 500,
        "originalPrice": 1000,
        "images": [
            "/static/images/favicon.png",
            "/static/images/logo.png",
        ],
    },
]


def get_all_events():
    now = datetime.now(timezone.utc)

    for event in events_data:
        date_obj = datetime.strptime(event["start_date"], "%d %B %Y %H:%M %Z")
        end_date_obj = datetime.strptime(event["end_date"], "%d %B %Y %H:%M %Z")

        start_date = date_obj.replace(tzinfo=timezone.utc)
        end_date = end_date_obj.replace(tzinfo=timezone.utc)
        if start_date > now:
            event["status"] = "upcoming"
        elif start_date < now and end_date < now:
            event["status"] = "past"
        else:
            event["status"] = "ongoing"

    return events_data


def get_events_by_status(status):
    return [event for event in events_data if event["status"] == status]


def get_event_by_id(event_id):
    for event in events_data:
        if event["id"] == event_id:
            return event
    return None


def get_teams_members():
    return teams_members


def get_swags():
    return swags


def get_parteners():
    return parteners


def get_heros():
    return hero_images

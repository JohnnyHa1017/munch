from app.models import db, BusinessImage, environment, SCHEMA
from sqlalchemy.sql import text

def seed_business_images():
    business_images = [
        # Pokemon Cafe (8 Images Total)
        BusinessImage(business_id=1, url="", preview=True),
        BusinessImage(business_id=1, url="", preview=False),
        BusinessImage(business_id=1, url="", preview=False),
        BusinessImage(business_id=1, url="", preview=False),
        BusinessImage(business_id=1, url="", preview=False),
        BusinessImage(business_id=1, url="", preview=False),
        # Stardew Farmhouse (6 Images Total)
        BusinessImage(business_id=2, url="", preview=True),
        BusinessImage(business_id=2, url="", preview=False),
        BusinessImage(business_id=2, url="", preview=False),
        BusinessImage(business_id=2, url="", preview=False),
        # Hunters Cafe (14 Images Total)
        BusinessImage(business_id=3, url="", preview=True),
        BusinessImage(business_id=3, url="", preview=False),
        BusinessImage(business_id=3, url="", preview=False),
        BusinessImage(business_id=3, url="", preview=False),
        BusinessImage(business_id=3, url="", preview=False),
        BusinessImage(business_id=3, url="", preview=False),
        BusinessImage(business_id=3, url="", preview=False),
        BusinessImage(business_id=3, url="", preview=False),
        BusinessImage(business_id=3, url="", preview=False),
        BusinessImage(business_id=3, url="", preview=False),
        BusinessImage(business_id=3, url="", preview=False),
        BusinessImage(business_id=3, url="", preview=False),
        # Continental Hotel (13 Images Total)
        BusinessImage(business_id=4, url="", preview=True),
        BusinessImage(business_id=4, url="", preview=False),
        BusinessImage(business_id=4, url="", preview=False),
        BusinessImage(business_id=4, url="", preview=False),
        BusinessImage(business_id=4, url="", preview=False),
        BusinessImage(business_id=4, url="", preview=False),
        BusinessImage(business_id=4, url="", preview=False),
        BusinessImage(business_id=4, url="", preview=False),
        BusinessImage(business_id=4, url="", preview=False),
        BusinessImage(business_id=4, url="", preview=False),
        BusinessImage(business_id=4, url="", preview=False),
        # Baratie (9 Images Total)
        BusinessImage(business_id=5, url="", preview=True),
        BusinessImage(business_id=5, url="", preview=False),
        BusinessImage(business_id=5, url="", preview=False),
        BusinessImage(business_id=5, url="", preview=False),
        BusinessImage(business_id=5, url="", preview=False),
        BusinessImage(business_id=5, url="", preview=False),
        BusinessImage(business_id=5, url="", preview=False),
        # Cafe Leblanc (7 Images Total)
        BusinessImage(business_id=6, url="", preview=True),
        BusinessImage(business_id=6, url="", preview=False),
        BusinessImage(business_id=6, url="", preview=False),
        BusinessImage(business_id=6, url="", preview=False),
        BusinessImage(business_id=6, url="", preview=False),
        # Urahara Shoten (5 Images Total)
        BusinessImage(business_id=7, url="", preview=True),
        BusinessImage(business_id=7, url="", preview=False),
        BusinessImage(business_id=7, url="", preview=False),
        # Four Horsemen Izakaya (7 Images Total)
        BusinessImage(business_id=8, url="", preview=True),
        BusinessImage(business_id=8, url="", preview=False),
        BusinessImage(business_id=8, url="", preview=False),
        BusinessImage(business_id=8, url="", preview=False),
        BusinessImage(business_id=8, url="", preview=False),
        # Animal Crossing Deli and Cafe (9 Images Total)
        BusinessImage(business_id=9, url="", preview=True),
        BusinessImage(business_id=9, url="", preview=False),
        BusinessImage(business_id=9, url="", preview=False),
        BusinessImage(business_id=9, url="", preview=False),
        BusinessImage(business_id=9, url="", preview=False),
        BusinessImage(business_id=9, url="", preview=False),
        BusinessImage(business_id=9, url="", preview=False),
        # Ghibli's Desserts (8 Images Total)
        BusinessImage(business_id=10, url="", preview=True),
        BusinessImage(business_id=10, url="", preview=False),
        BusinessImage(business_id=10, url="", preview=False),
        BusinessImage(business_id=10, url="", preview=False),
        BusinessImage(business_id=10, url="", preview=False),
        BusinessImage(business_id=10, url="", preview=False)
    ]

    db.session.add_all(business_images)
    db.session.commit()


def undo_business_images():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.business_images RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM business_images"))

    db.session.commit()

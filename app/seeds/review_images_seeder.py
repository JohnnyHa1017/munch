from app.models import db, ReviewImage, environment, SCHEMA
from sqlalchemy.sql import text

def seed_review_images():
    review_images = [
        # Pokemon Cafe
        ReviewImage(review_id=1, url=""),
        ReviewImage(review_id=2, url=""),
        # Stardew Farmhouse
        ReviewImage(review_id=3, url=""),
        ReviewImage(review_id=4, url=""),
        # Hunters Cafe (14 Images Total)
        ReviewImage(review_id=5, url=""),
        ReviewImage(review_id=6, url=""),
        # Continental Hotel
        ReviewImage(review_id=7, url=""),
        ReviewImage(review_id=8, url=""),
        # Baratie (9 Images Total)
        ReviewImage(review_id=9, url=""),
        ReviewImage(review_id=10, url=""),
        # Cafe Leblanc
        ReviewImage(review_id=11, url=""),
        ReviewImage(review_id=12, url=""),
        # Urahara Shoten
        ReviewImage(review_id=13, url=""),
        ReviewImage(review_id=14, url=""),
        # Four Horsemen Izakaya
        ReviewImage(review_id=15, url=""),
        ReviewImage(review_id=16, url=""),
        # Animal Crossing Deli and Cafe
        ReviewImage(review_id=17, url=""),
        ReviewImage(review_id=18, url=""),
        # Ghibli's Desserts
        ReviewImage(review_id=19, url=""),
        ReviewImage(review_id=20, url="")
    ]

    db.session.add_all(review_images)
    db.session.commit()

def undo_review_images():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.review_images RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM review_images"))

    db.session.commit()

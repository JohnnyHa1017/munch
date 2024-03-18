from app.models import db, ReviewImage, environment, SCHEMA
from sqlalchemy.sql import text

def seed_review_images():
    # Pokemon Cafe
    pc_review_image1 = ReviewImage(review_id=1)
    pc_review_image2 = ReviewImage(review_id=1)
    # Stardew Farmhouse
    sf_review_image1 = ReviewImage(review_id=2)
    sf_review_image2 = ReviewImage(review_id=2)
    # Hunters Cafe (14 Images Total)
    hc_review_image1 = ReviewImage(review_id=3)
    hc_review_image2 = ReviewImage(review_id=3)
    # Continental Hotel
    ch_review_image1 = ReviewImage(review_id=4)
    ch_review_image2 = ReviewImage(review_id=4)
    # Baratie (9 Images Total)
    ba_review_image1 = ReviewImage(review_id=5)
    ba_review_image2 = ReviewImage(review_id=5)
    # Cafe Leblanc
    cl_review_image1 = ReviewImage(review_id=6)
    cl_review_image2 = ReviewImage(review_id=6)
    # Urahara Shoten
    us_review_image1 = ReviewImage(review_id=7)
    us_review_image2 = ReviewImage(review_id=7)
    # Four Horsemen Izakaya
    fhi_review_image1 = ReviewImage(review_id=8)
    fhi_review_image2 = ReviewImage(review_id=8)
    # Animal Crossing Deli and Cafe
    acd_review_image1 = ReviewImage(review_id=9)
    acd_review_image2 = ReviewImage(review_id=9)
    # Ghibli's Desserts
    gd_review_image1 = ReviewImage(review_id=10)
    gd_review_image2 = ReviewImage(review_id=10)

    db.session.add_all([
        pc_review_image1, pc_review_image2,
        sf_review_image1, sf_review_image2,
        hc_review_image1, hc_review_image2,
        ch_review_image1, ch_review_image2,
        ba_review_image1, ba_review_image2,
        cl_review_image1, cl_review_image2,
        us_review_image1, us_review_image2,
        fhi_review_image1, fhi_review_image2,
        acd_review_image1, acd_review_image2,
        gd_review_image1, gd_review_image2
    ])
    db.session.commit()

def undo_review_images():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.review_images RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM review_images"))

    db.session.commit()

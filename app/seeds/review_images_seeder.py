from app.models import db, ReviewImage, environment, SCHEMA
from sqlalchemy.sql import text

def seed_review_images():
    # Pokemon Cafe
    pc_review_image1 = ReviewImage(review_id=1, url="1")
    pc_review_image2 = ReviewImage(review_id=2, url="2")
    # Stardew Farmhouse
    sf_review_image1 = ReviewImage(review_id=3, url="3")
    sf_review_image2 = ReviewImage(review_id=4, url="4")
    # Hunters Cafe (14 Images Total)
    hc_review_image1 = ReviewImage(review_id=5, url="5")
    hc_review_image2 = ReviewImage(review_id=6, url="6")
    # Continental Hotel
    ch_review_image1 = ReviewImage(review_id=7, url="7")
    ch_review_image2 = ReviewImage(review_id=8, url="8")
    # Baratie (9 Images Total)
    ba_review_image1 = ReviewImage(review_id=9, url="9")
    ba_review_image2 = ReviewImage(review_id=10, url="10")
    # Cafe Leblanc
    cl_review_image1 = ReviewImage(review_id=11, url="11")
    cl_review_image2 = ReviewImage(review_id=12, url="12")
    # Urahara Shoten
    us_review_image1 = ReviewImage(review_id=13, url="13")
    us_review_image2 = ReviewImage(review_id=14, url="14")
    # Four Horsemen Izakaya
    fhi_review_image1 = ReviewImage(review_id=15, url="15")
    fhi_review_image2 = ReviewImage(review_id=16, url="16")
    # Animal Crossing Deli and Cafe
    acd_review_image1 = ReviewImage(review_id=17, url="17")
    acd_review_image2 = ReviewImage(review_id=18, url="18")
    # Ghibli's Desserts
    gd_review_image1 = ReviewImage(review_id=19, url="19")
    gd_review_image2 = ReviewImage(review_id=20, url="20")

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

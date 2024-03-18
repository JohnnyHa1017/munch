from app.models import db, ReviewImage, environment, SCHEMA
from sqlalchemy.sql import text

def seed_review_images():
    # Pokemon Cafe
    pc_review_image1 = ReviewImage(review_id=1, url='img.jpg')
    pc_review_image2 = ReviewImage(review_id=1, url='img.jpg')
    # Stardew Farmhouse
    sf_review_image1 = ReviewImage(review_id=2, url='img.jpg')
    sf_review_image2 = ReviewImage(review_id=2, url='img.jpg')
    # Hunters Cafe (14 Images Total)
    hc_review_image1 = ReviewImage(review_id=3, url='img.jpg')
    hc_review_image2 = ReviewImage(review_id=3, url='img.jpg')
    # Continental Hotel
    ch_review_image1 = ReviewImage(review_id=4, url='img.jpg')
    ch_review_image2 = ReviewImage(review_id=4, url='img.jpg')
    # Baratie (9 Images Total)
    ba_review_image1 = ReviewImage(review_id=5, url='img.jpg')
    ba_review_image2 = ReviewImage(review_id=5, url='img.jpg')
    # Cafe Leblanc
    cl_review_image1 = ReviewImage(review_id=6, url='img.jpg')
    cl_review_image2 = ReviewImage(review_id=6, url='img.jpg')
    # Urahara Shoten
    us_review_image1 = ReviewImage(review_id=7, url='img.jpg')
    us_review_image2 = ReviewImage(review_id=7, url='img.jpg')
    # Four Horsemen Izakaya
    fhi_review_image1 = ReviewImage(review_id=8, url='img.jpg')
    fhi_review_image2 = ReviewImage(review_id=8, url='img.jpg')
    # Animal Crossing Deli and Cafe
    acd_review_image1 = ReviewImage(review_id=9, url='img.jpg')
    acd_review_image2 = ReviewImage(review_id=9, url='img.jpg')
    # Ghibli's Desserts
    gd_review_image1 = ReviewImage(review_id=10, url='img.jpg')
    gd_review_image2 = ReviewImage(review_id=10, url='img.jpg')

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

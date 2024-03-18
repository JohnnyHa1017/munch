from app.models import db, ReviewImage, environment, SCHEMA
from sqlalchemy.sql import text

def seed_review_images():
    # Pokemon Cafe
    pc_review_image1 = ReviewImage(review_id=1, url="https://i.postimg.cc/50Z0HDHf/fluffyeeveepancakes.jpg")
    pc_review_image2 = ReviewImage(review_id=1, url="https://i.postimg.cc/YS58dqZg/burnt-caramelvulpixsundae.jpg")
    # Stardew Farmhouse
    sf_review_image1 = ReviewImage(review_id=2, url="https://i.postimg.cc/y8KXk9Tt/Banana-Pudding.png")
    sf_review_image2 = ReviewImage(review_id=2, url="https://i.postimg.cc/GphFjCVj/Triple-Shot-Espresso.png")
    # Hunters Cafe (14 Images Total)
    hc_review_image1 = ReviewImage(review_id=3, url="https://i.postimg.cc/tTX9Vkg1/Meow-Meow-Fantasy.jpg")
    hc_review_image2 = ReviewImage(review_id=3, url="https://i.postimg.cc/PrBhMTxn/Dragons-Breath.jpg")
    # Continental Hotel
    ch_review_image1 = ReviewImage(review_id=4, url="https://i.postimg.cc/L6jbg1Jf/Continental-Hotel-Gelato.jpg")
    ch_review_image2 = ReviewImage(review_id=4, url="https://i.postimg.cc/rwcY1w4H/Continental-Hotel-Bandaid.jpg")
    # Baratie (9 Images Total)
    ba_review_image1 = ReviewImage(review_id=5, url="https://i.postimg.cc/T1XyHFft/Baratie-Mandarin-Orange-Jelly.png")
    ba_review_image2 = ReviewImage(review_id=5, url="https://i.postimg.cc/Qxh9Q26t/Baratie-Red-Nosed-Mousse.png")
    # Cafe Leblanc
    cl_review_image1 = ReviewImage(review_id=6, url="https://i.postimg.cc/xCTJr7Z5/Cafe-Leblanc-Omelette-Coffee.jpg")
    cl_review_image2 = ReviewImage(review_id=6, url="https://i.postimg.cc/2ShBnnvQ/Cafe-Leblanc-Deluxe-Curry.jpg")
    # Urahara Shoten
    us_review_image1 = ReviewImage(review_id=7, url="https://i.postimg.cc/WpCXwLt0/Urahara-Shoten-Kon-Dog.jpg")
    us_review_image2 = ReviewImage(review_id=7, url="https://i.postimg.cc/MXJGdFJz/Urahara-Shoten-Kirio-Feast.webp")
    # Four Horsemen Izakaya
    fhi_review_image1 = ReviewImage(review_id=8, url="https://i.postimg.cc/pXVXC77X/Four-Horsemen-Izakaya-Makima-Curry-Udon.jpg")
    fhi_review_image2 = ReviewImage(review_id=8, url="https://i.postimg.cc/t4wqXggY/Four-Horsemen-Izakaya-Hayakawa-Gyoza.png")
    # Animal Crossing Deli and Cafe
    acd_review_image1 = ReviewImage(review_id=9, url="https://i.postimg.cc/cHPvKcTG/Animal-Crossing-Deli-Peach-Smoothie.webp")
    acd_review_image2 = ReviewImage(review_id=9, url="https://i.postimg.cc/05LSr9HK/Animal-Crossing-Deli-Coconut-Juice.webp")
    # Ghibli's Desserts
    gd_review_image1 = ReviewImage(review_id=10, url="https://i.postimg.cc/DfCtMsVN/jiji-donut.png")
    gd_review_image2 = ReviewImage(review_id=10, url="https://i.postimg.cc/ZnD2vkFm/otori-sama-macaron.png")

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

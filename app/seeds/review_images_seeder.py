from app.models import db, ReviewImage, environment, SCHEMA
from sqlalchemy.sql import text


def seed_review_images():
    review1_img = ReviewImage(review_id=1, url="POKEMONurl_for_review_1.jpg")
    review2_img = ReviewImage(review_id=2, url="POKEMONurl_for_review_2.jpg")
    review3_img = ReviewImage(review_id=3, url="STARDEWurl_for_review_3.jpg")
    review4_img = ReviewImage(review_id=4, url="STARDEWurl_for_review_4.jpg")
    review5_img = ReviewImage(review_id=5, url="HUNTER_for_review_5.jpg")
    review6_img = ReviewImage(review_id=6, url="HUNTER_for_review_6.jpg")
    review7_img = ReviewImage(review_id=7, url="CONTINENTAL_for_review_7.jpg")
    review8_img = ReviewImage(review_id=8, url="CONTINENTAL_for_review_8.jpg")
    review9_img = ReviewImage(review_id=9, url="BARATIE_for_review_9.jpg")
    review10_img = ReviewImage(review_id=10, url="BARATIE_for_review_10.jpg")
    review11_img = ReviewImage(review_id=11, url="CAFELEBLANC_review_11.jpg")
    review12_img = ReviewImage(review_id=12, url="CAFELEBLANC_review_12.jpg")
    review13_img = ReviewImage(review_id=13, url="URAHARA_for_review_13.jpg")
    review14_img = ReviewImage(review_id=14, url="URAHARA_for_review_14.jpg")
    review15_img = ReviewImage(review_id=15, url="FOURHORSE_for_review_15.jpg")
    review16_img = ReviewImage(review_id=16, url="FOURHORSE_for_review_16.jpg")
    review17_img = ReviewImage(review_id=17, url="ANIMALCROSSING_for_review_17.jpg")
    review18_img = ReviewImage(review_id=18, url="ANIMALCROSSING_for_review_18.jpg")
    review19_img = ReviewImage(review_id=19, url="GHIBLI_for_review_19.jpg")
    review20_img = ReviewImage(review_id=20, url="GHIBLI_for_review_20.jpg")

    db.session.add_all(
        [
            review1_img,
            review2_img,
            review3_img,
            review4_img,
            review5_img,
            review6_img,
            review7_img,
            review8_img,
            review9_img,
            review10_img,
            review11_img,
            review12_img,
            review13_img,
            review14_img,
            review15_img,
            review16_img,
            review17_img,
            review18_img,
            review19_img,
            review20_img,
        ]
    )
    db.session.commit()


def undo_review_images():
    if environment == "production":
        db.session.execute(
            f"TRUNCATE table {SCHEMA}.review_images RESTART IDENTITY CASCADE;"
        )
    else:
        db.session.execute(text("DELETE FROM review_images"))

    db.session.commit()

from app.models import db, Review, environment, SCHEMA
from sqlalchemy.sql import text

def seed_reviews():
    # Pokemon Cafe
    pokemon_cafe_review1 = Review(
        business_id=1,
        user_id=2,
        review="Had a delightful time at Pokemon Cafe! The ambiance was great, especially for a Pokemon enthusiast like myself. Definitely coming back!",
        star=5
    )
    pokemon_cafe_review2 = Review(
        business_id=1,
        user_id=3,
        review="Pokemon Cafe exceeded my expectations! The atmosphere was vibrant and welcoming. I appreciated the option for reservations as it ensured I had a table waiting. The restaurant was great for groups; we had a blast! Highly recommend it to fellow trainers!",
        star=4
    )

    # Stardew Farmhouse
    stardew_farmhouse_review1 = Review(
        business_id=2,
        user_id=3,
        review="Stardew Farmhouse was a cozy retreat! The delivery service was prompt, and the food was deliciously fresh. Pickup option was convenient for busy days. Vegetarian choices were ample and flavorful. Street parking made it hassle-free to visit. However, I missed having outdoor seating. Nonetheless, a delightful experience overall!",
        star=4
    )
    stardew_farmhouse_review2 = Review(
        business_id=2,
        user_id=4,
        review="Stardew Farmhouse is a gem! The pickup service was efficient, and the vegetarian options were a pleasant surprise. Will definitely return for more!",
        star=5
    )

    # Hunters Cafe
    hunters_cafe_review1 = Review(
        business_id=3,
        user_id=4,
        review="Had a decent experience at Hunters Cafe. The pickup option was convenient, but the lack of vegetarian options was disappointing.",
        star=3
    )
    hunters_cafe_review2 = Review(
        business_id=3,
        user_id=5,
        review="Enjoyed my time at Hunters Cafe! Outdoor seating added to the charm. Would recommend for a casual dining experience.",
        star=4
    )

    # Continental Hotel
    continental_hotel_review1 = Review(
        business_id=4,
        user_id=1,
        review="Had a fantastic experience at Continental Hotel! The reservation process was seamless, and the staff was attentive.",
        star=5
    )
    continental_hotel_review2 = Review(
        business_id=4,
        user_id=6,
        review="Enjoyed my meal at Continental Hotel! The delivery service was efficient. Free Wi-Fi and street parking made it convenient.",
        star=4
    )

    # Baratie
    baratie_review1 = Review(
        business_id=5,
        user_id=8,
        review="Had a pleasant experience at Baratie! The reservation process was smooth, and the staff was friendly. Accepts credit card option was convenient.",
        star=4
    )
    baratie_review2 = Review(
        business_id=5,
        user_id=9,
        review="Baratie was alright. The outdoor seating was disappointing, an average experience.",
        star=2
    )

    # Cafe Leblanc
    cafe_leblanc_review1 = Review(
        business_id=6,
        user_id=10,
        review="The staff was attentive. Delivery service was prompt, and the food was delicious...",
        star=5
    )
    cafe_leblanc_review2 = Review(
        business_id=6,
        user_id=7,
        review="Enjoyed my meal at Cafe Leblanc! The reservation ensured a table was ready upon arrival. Outdoor seating would have been a bonus!",
        star=4
    )

    # Urahara Shoten
    urahara_shoten_review1 = Review(
        business_id=7,
        user_id=2,
        review="Urahara Shoten was GREAT. The pickup option was convenient with plenty of street parking!",
        star=5
    )
    urahara_shoten_review2 = Review(
        business_id=7,
        user_id=8,
        review="Enjoyed my time at Urahara Shoten! Pickup service was quick and hassle-free. The atmosphere was cozy, although free Wi-Fi would have been appreciated.",
        star=4
    )

    # Four Horsemen Izakaya
    four_horsemen_izakaya_review1 = Review(
        business_id=8,
        user_id=4,
        review="Had a fantastic experience at Four Horsemen Izakaya! The reservation process was seamless, and the staff was attentive.",
        star=5
    )
    four_horsemen_izakaya_review2 = Review(
        business_id=8,
        user_id=5,
        review="Enjoyed my meal at Four Horsemen Izakaya! Outdoor seating would have been a bonus.",
        star=4
    )

    # Animal Crossing Deli and Cafe
    animal_crossing_review1 = Review(
        business_id=9,
        user_id=6,
        review="Had a pleasant experience at Animal Crossing Deli and Cafe! The staff was friendly. Would recommend for a casual dining experience.",
        star=4
    )
    animal_crossing_review2 = Review(
        business_id=9,
        user_id=10,
        review="Animal Crossing Deli and Cafe was alright. The lack of outdoor seating was disappointing.",
        star=2
    )

    # Ghibli's Desserts
    ghiblis_desserts_review1 = Review(
        business_id=10,
        user_id=8,
        review="Ghibli's Desserts exceeded my expectations! Pickup option was convenient for busy days. Free Wi-Fi and outdoor seating made it a wonderful experience.",
        star=5
    )
    ghiblis_desserts_review2 = Review(
        business_id=10,
        user_id=9,
        review="Enjoyed my desserts at Ghibli's Desserts! Will definitely return for more!",
        star=4
    )

    db.session.add_all([
        pokemon_cafe_review1,
        pokemon_cafe_review2,
        stardew_farmhouse_review1,
        stardew_farmhouse_review2,
        hunters_cafe_review1,
        hunters_cafe_review2,
        continental_hotel_review1,
        continental_hotel_review2,
        baratie_review1,
        baratie_review2,
        cafe_leblanc_review1,
        cafe_leblanc_review2,
        urahara_shoten_review1,
        urahara_shoten_review2,
        four_horsemen_izakaya_review1,
        four_horsemen_izakaya_review2,
        animal_crossing_review1,
        animal_crossing_review2,
        ghiblis_desserts_review1,
        ghiblis_desserts_review2
    ])

    db.session.commit()

def undo_reviews():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.reviews RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM reviews"))

    db.session.commit()

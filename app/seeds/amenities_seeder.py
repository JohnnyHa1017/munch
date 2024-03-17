from app.models import db, Amenity, environment, SCHEMA
from sqlalchemy.sql import text

def seed_amenities():
    pokemon_cafe_am = Amenity(
        business_id = 0,
        reservation = True,
        delivery= False,
        pickup=False,
        vegetarian=False,
        accepts_credit_card= True,
        free_wi_fi= True,
        street_parking= False,
        good_for_groups= True,
        outdoor_seating= True
    )
    stardew_farmhouse_am = Amenity(
        business_id = 1,
        reservation = False,
        delivery= True,
        pickup= True,
        vegetarian= True,
        accepts_credit_card= True,
        free_wi_fi= True,
        street_parking= True,
        good_for_groups= True,
        outdoor_seating= False
    )
    hunters_cafe_am = Amenity(
        business_id = 2,
        reservation = False,
        delivery= False,
        pickup= True,
        vegetarian= False,
        accepts_credit_card= False,
        free_wi_fi= False,
        street_parking= True,
        good_for_groups= True,
        outdoor_seating= True
    )
    continental_hotel_am = Amenity(
        business_id = 3,
        reservation = True,
        delivery= True,
        pickup= True,
        vegetarian= False,
        accepts_credit_card= True,
        free_wi_fi= True,
        street_parking= True,
        good_for_groups= False,
        outdoor_seating= False
    )
    baratie_am = Amenity(
        business_id = 4,
        reservation = True,
        delivery= False,
        pickup= False,
        vegetarian= False,
        accepts_credit_card= True,
        free_wi_fi= True,
        street_parking= False,
        good_for_groups= True,
        outdoor_seating= True
    )
    cafe_leblanc_am = Amenity(
        business_id = 5,
        reservation = True,
        delivery= True,
        pickup= True,
        vegetarian= False,
        accepts_credit_card= True,
        free_wi_fi= True,
        street_parking= True,
        good_for_groups= True,
        outdoor_seating= False
    )
    urahara_shoten_am = Amenity(
        business_id = 6,
        reservation = False,
        delivery= False,
        pickup= True,
        vegetarian= False,
        accepts_credit_card= True,
        free_wi_fi= False,
        street_parking= True,
        good_for_groups= True,
        outdoor_seating= False
    )
    four_horsemen_izakaya_am = Amenity(
        business_id = 7,
        reservation = True,
        delivery= False,
        pickup= True,
        vegetarian= False,
        accepts_credit_card= True,
        free_wi_fi= False,
        street_parking= False,
        good_for_groups= True,
        outdoor_seating= False
    )
    animal_crossing_deli_and_cafe_am = Amenity(
        business_id = 8,
        reservation = False,
        delivery= True,
        pickup= True,
        vegetarian= True,
        accepts_credit_card= True,
        free_wi_fi= True,
        street_parking= True,
        good_for_groups= False,
        outdoor_seating= False
    )
    ghiblis_desserts_am = Amenity(
        business_id = 9,
        reservation = False,
        delivery= False,
        pickup= True,
        vegetarian= True,
        accepts_credit_card= True,
        free_wi_fi= True,
        street_parking= False,
        good_for_groups= False,
        outdoor_seating= True
    )

    db.session.add_all([pokemon_cafe_am,
                        stardew_farmhouse_am,
                        hunters_cafe_am,
                        continental_hotel_am,
                        baratie_am,
                        cafe_leblanc_am,
                        urahara_shoten_am,
                        four_horsemen_izakaya_am,
                        animal_crossing_deli_and_cafe_am,
                        ghiblis_desserts_am
    ])

    db.session.commit()

def undo_amenities():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.amenities RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM amenities"))

    db.session.commit()

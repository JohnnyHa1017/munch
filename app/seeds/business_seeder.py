from app.models import db, Business, environment, SCHEMA
from sqlalchemy.sql import text
import json




def seed_businesses():


   pokemon_cafe = Business(
       owner_id= 6,
       title= 'Pokemon Cafe',
       address= '2-4-1 Nihombashi',
       city= 'Chuo-ku',
       state= 'Tokyo',
       country= 'Japan',
       price_rating= 3,
       category= json.dumps(["Cafe", "Brunch", "Japanese"]),
       lat= 35.68092399279239,
       lng= 139.77345635400394,
       phone_number= '555-555-5555',
       description= 'A locally owned Cafe perfect for a small bite with friends ',
       schedule='Monday: 6:00am - 3:00pm, Tuesday: 6:00am - 3:00pm, Wednesday: 6:00am - 3:00pm, Thursday: 6:00am - 3:00pm, Friday: 6:00am - 5:00pm, Saturday: 6:00am - 5:00pm, Sunday: 6:00am - 5:00pm'


   )


   stardew_farmhouse = Business(
       owner_id= 1,
       title= 'Stardew Farmhouse',
       address= '203 Pike St',
       city= 'Seattle',
       state= 'Washington',
       country= 'United States of America',
       price_rating= 1,
       category= json.dumps(["Italian"]),
       lat= 47.609410746763395,
       lng= -122.33846094232874,
       phone_number= '243-555-2343',
       description= 'Italian cuisine with lots of vegetarian options.',
       schedule='Monday: 10:00am - 9:00pm, Tuesday: 10:00am - 9:00pm, Wednesday: 10:00am - 9:00pm, Thursday: 10:00am - 9:00pm, Friday: 10:00am - 9:00pm, Saturday: 10:00am - 11:00pm, Sunday: 10:00am - 11:00pm'
   )


   hunters_cafe = Business(
       owner_id= 5,
       title= 'Hunters Cafe',
       address= '1 Chrome-1-10 Pasela Resorts AKIBA Multi Entertainment 3F',
       city= 'Chiyoda City',
       state= 'Tokyo',
       country= 'Japan',
       price_rating= 2,
       category= json.dumps(["Cafe", "Bar", "Japanese"]),
       lat= 35.69781456877865,
       lng= 139.7703628318951,
       phone_number= '0120-888-888',
       description= 'Hunters! Seeking respite from the rigors of battling monsters? Look no further than Monster Cafe, your premier destination for relaxation and refreshment, where friendly feline companions serve as hosts and bartenders.',
       schedule='Monday: 5:00pm - 1:00am, Tuesday: :5:00pm - 1:00am, Wednesday: :5:00pm - 1:00am, Thursday: 5:00pm - 2:00am, Friday: 5:00pm - 4:00am, Saturday: 5:00pm - 4:00am, Sunday: 5:00pm - 2:00am'
   )


   continental_hotel = Business(
       owner_id= 1,
       title= 'Continental Hotel',
       address= '1 Beaver Street',
       city= 'New York',
       state= 'New York',
       country= 'United States of America',
       price_rating= 4,
       category= json.dumps(["Italian"]),
       lat= 40.70537093863372,
       lng= -74.00824708070003,
       phone_number= '718-888-8888',
       description= 'You know the rules: No business can be conducted on these premises lest incurring heavy penalties. Have a drink and relax, for now. - Winston',
       schedule='Monday: 6:00am - 11:00pm, Tuesday: 6:00am - 11:00pm, Wednesday: 6:00am - 11:00pm, Thursday: 6:00am - 11:00pm, Friday: 6:00am - 11:00pm, Saturday: 6:00am - 11:00pm, Sunday: 6:00am - 11:00pm'    )


   baratie = Business(
       owner_id= 4,
       title= 'Baratie',
       address= 'Floating around',
       city= 'Sambas Region',
       state= 'Close to the entrance of the Grand Line',
       country= 'Sekai',
       price_rating= 2,
       category= json.dumps(["Japanese", "Seafood", "Italian"]),
       lat= 20.07090,
       lng= -130.6637,
       phone_number= '1-844-4357-387',
       description= "Welcome to The Baratie, owned by former pirate captain Zeff, known as Red-Leg. Our staff includes outcasts, exiles, and pirates. Our chefs are skilled fighters, who have defended our food against pirates who dare steal our food. The Baratie was also home to the famous pirate Sanji. Join us for gourmet cuisine with breathtaking ocean views. The Baratie promises a memorable dining experience.",
       schedule='Monday: 8:00am - 10:00pm, Tuesday: 8:00am - 10:00pm, Wednesday: 8:00am - 10:00pm, Thursday: None - None, Friday: 8:00am - 10:00pm, Saturday: 8:00am - 11:00pm, Sunday: None - None'


   )


   cafe_leblanc = Business(
       owner_id= 1,
       title= 'Cafe Leblanc',
       address= '2-chōme-14 Sangenjaya',
       city= 'Setagaya City',
       state= 'Tokyo',
       country= 'Japan',
       price_rating= 1,
       category= json.dumps(["Cafe"]),
       lat= 35.6434,
       lng= 139.6715,
       phone_number= '605-475-6961',
       description= "Discover our renowned restaurant, celebrated for its signature coffee and flavorful curry. Savor the rich aroma of expertly brewed pour-over coffee, meticulously prepared using a Hario V60 dripper. Indulge in our tantalizing curry, crafted with a blend of spices. Our cafe also features siphon/vacuum coffee makers, adding a touch of theater to your coffee experience. Whether you're here for the coffee or the curry, our restaurant promises a memorable dining experience.",
       schedule='Monday: 6:00am - 8:00pm, Tuesday: 6:00am - 8:00pm, Wednesday: 6:00am - 8:00pm, Thursday: 6:00am - 8:00pm, Friday: 6:00am - 8:00pm, Saturday: 6:00am - 8:00pm, Sunday: 6:00am - 8:00pm'
   )


   urahara_shoten = Business(
       owner_id= 7,
       title= 'Urahara Shōten',
       address= '1-1 Osakajo',
       city= 'Chuo Ward',
       state= 'Osaka',
       country= 'Japan',
       price_rating= 3,
       category= json.dumps(["Japanese", "German", "Asian Fusion"]),
       lat= 34.687485146266695,
       lng= 135.52587197488396,
       phone_number= '326-214-4231',
       description= "While it appears to be no more than an average shop on the outside, it is a shop that caters to every Shinigami's needs!",
       schedule='Monday: None - None, Tuesday: None - None, Wednesday: None - None, Thursday: None - None, Friday: 7:00pm - 4:00am, Saturday: 7:00pm - 4:00am, Sunday: None - None'
   )


   four_horsemen_izakaya = Business(
       owner_id= 1,
       title= 'Four Horsemen Izakaya',
       address= '106-0045 Tokyo',
       city= 'Minato City',
       state= 'Azabujuban',
       country= 'Japan',
       price_rating= 2,
       category= json.dumps(["Japanese", "Bar", "Asian Fusion"]),
       lat= 35.65648279953456,
       lng= 139.73433664043887,
       phone_number= '454-522-3151',
       description= "Step into Four Horsemen Izakaya and immerse yourself in the vibrant atmosphere of a traditional Japanese bar. Nestled in the heart of bustling streets, our izakaya welcomes you with warm wooden interiors.",
       schedule='Monday: None - None, Tuesday: None - None, Wednesday: None - None, Thursday: None - None, Friday: 7:00pm - 4:00am, Saturday: 7:00pm - 4:00am, Sunday: None - None'
   )


   animal_crossing_deli_cafe = Business(
       owner_id= 6,
       title= 'Animal Crossing Deli and Cafe',
       address= '459 S Hewitt St',
       city= 'Los Angeles',
       state= 'California',
       country= 'United States of America',
       price_rating= 1,
       category= json.dumps(["Cafe", "Deli"]),
       lat= 89.345,
       lng= -43.435624,
       phone_number= '453-555-3436',
       description= "Your local bagel shop with fresh juice and smoothies.",
       schedule='Monday: 7:00am - 4:00pm, Tuesday: 7:00am - 4:00pm, Wednesday: 7:00am - 4:00pm, Thursday: 7:00am - 4:00pm, Friday: 7:00am - 4:00pm, Saturday: None - None, Sunday: None - None'


   )


   ghiblis_desserts = Business(
       owner_id= 9,
       title= "Ghibli's Desserts",
       address= '1 Chome-1-83 Shimorenjaku',
       city= 'Mitaka',
       state= 'Tokyo',
       country= 'Japan',
       price_rating= 2,
       category= json.dumps(["Dessert"]),
       lat= 35.69645144378257,
       lng= 139.570506798222,
       phone_number= '934-652-4643',
       description= "Handcrafted desserts that are almost too cute to eat!",
       schedule='Monday: 12:00pm - 11:00pm, Tuesday: 12:00pm - 11:00pm, Wednesday: 12:00pm - 11:00pm, Thursday: 12:00pm - 11:00pm, Friday: 12:00pm - 11:00pm, Saturday: 11:00am - 11:00pm, Sunday: 11:00am - 11:00pm'
   )




   db.session.add_all([pokemon_cafe, stardew_farmhouse, hunters_cafe, continental_hotel, baratie, cafe_leblanc, urahara_shoten, four_horsemen_izakaya, animal_crossing_deli_cafe, ghiblis_desserts])
   db.session.commit()




# Uses a raw SQL query to TRUNCATE or DELETE the users table. SQLAlchemy doesn't
# have a built in function to do this. With postgres in production TRUNCATE
# removes all the data from the table, and RESET IDENTITY resets the auto
# incrementing primary key, CASCADE deletes any dependent entities.  With
# sqlite3 in development you need to instead use DELETE to remove all data and
# it will reset the primary keys for you as well.
def undo_businesses():
   if environment == "production":
       db.session.execute(f"TRUNCATE table {SCHEMA}.businesses RESTART IDENTITY CASCADE;")
   else:
       db.session.execute(text("DELETE FROM businesses"))


   db.session.commit()

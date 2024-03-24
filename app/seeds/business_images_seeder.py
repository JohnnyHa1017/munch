from app.models import db, BusinessImage, environment, SCHEMA
from sqlalchemy.sql import text

def seed_business_images():
    # Pokemon Cafe (5 Images Total)
    pc_business_image1 = BusinessImage(business_id=1, url="https://i.postimg.cc/DzpmhSnJ/cheesyrowletpizza.jpg", preview=True, menu_id=1)
    pc_business_image2 = BusinessImage(business_id=1, url="https://i.postimg.cc/qR8fLFbJ/piquantpikachucurry.jpg", preview=False, menu_id=2)
    pc_business_image3 = BusinessImage(business_id=1, url="https://i.postimg.cc/kGK5Ww8K/happysnorlaxlocomoco.jpg", preview=False, menu_id=3)
    pc_business_image4 = BusinessImage(business_id=1, url="https://i.postimg.cc/QCs2nqwp/teddiursaicedcoffee.jpg", preview=False, menu_id=4)
    pc_business_image5 = BusinessImage(business_id=1, url="https://i.postimg.cc/d173VJVW/eeveelatte.jpg", preview=False, menu_id=5)
    pc_business_image6 = BusinessImage(business_id=1, url="https://i.postimg.cc/50Z0HDHf/fluffyeeveepancakes.jpg", preview=False, menu_id=6)
    pc_business_image7 = BusinessImage(business_id=1, url="https://i.postimg.cc/YS58dqZg/burnt-caramelvulpixsundae.jpg", preview=False, menu_id=7)

    # Stardew Farmhouse (4 Images Total)
    sf_business_image1 = BusinessImage(business_id=2, url="https://i.postimg.cc/g2KyRJSJ/Cheese-Cauliflower.png", preview=True, menu_id=8)
    sf_business_image2 = BusinessImage(business_id=2, url="https://i.postimg.cc/gcfKb1LY/Artichoke-Dip.png", preview=False, menu_id=9)
    sf_business_image3 = BusinessImage(business_id=2, url="https://i.postimg.cc/wTLQqFDD/Fiddlehead-Risotto.png", preview=False, menu_id=10)
    sf_business_image4 = BusinessImage(business_id=2, url="https://i.postimg.cc/MGPyPL8J/Eggplant-Parmesan.png", preview=False, menu_id=11)
    sf_business_image5 = BusinessImage(business_id=2, url="https://i.postimg.cc/y8KXk9Tt/Banana-Pudding.png", preview=False, menu_id=12)
    sf_business_image6 = BusinessImage(business_id=2, url="https://i.postimg.cc/GphFjCVj/Triple-Shot-Espresso.png", preview=False, menu_id=13)

# Hunters Cafe (14 Images Total)
    hc_business_image1 = BusinessImage(business_id=3, url="https://i.postimg.cc/PfS5YgYd/tokyo-hunters-bar-preview.jpg", preview=True)
    hc_business_image2 = BusinessImage(business_id=3, url="https://i.postimg.cc/tJvRb6ps/tokyo-hunters-bar-filler.jpg", preview=False)
    hc_business_image3 = BusinessImage(business_id=3, url="https://i.postimg.cc/hvt4NsWF/tokyo-hunters-bar-gaming.jpg", preview=False)
    hc_business_image4 = BusinessImage(business_id=3, url="https://i.postimg.cc/Z5BnTw94/tokyo-hunters-bar-dragon.jpg", preview=False)
    hc_business_image5 = BusinessImage(business_id=3, url="https://i.postimg.cc/5Nkjdh2s/tokyo-hunters-bar-decor.jpg", preview=False)
    hc_business_image6 = BusinessImage(business_id=3, url="https://i.postimg.cc/CK8R4cYm/tokyo-hunters-bar-cooking.jpg", preview=False)
    hc_business_image7 = BusinessImage(business_id=3, url="https://i.postimg.cc/vTYDbMnN/tokyo-hunters-bar-butcher.jpg", preview=False)
    hc_business_image8 = BusinessImage(business_id=3, url="https://i.postimg.cc/qqPY2BGm/Yakitori-Combo.jpg", preview=False, menu_id=14)
    hc_business_image9 = BusinessImage(business_id=3, url="https://i.postimg.cc/fLg1TfSQ/Niang-Co-Sake.jpg", preview=False, menu_id=15)
    hc_business_image10 = BusinessImage(business_id=3, url="https://i.postimg.cc/RFzNpwZ9/Hunters-Tofu.jpg", preview=False, menu_id=16)
    hc_business_image11 = BusinessImage(business_id=3, url="https://i.postimg.cc/W1kpRtK4/Yuzu-Beef-Steak.jpg", preview=False, menu_id=17)
    hc_business_image12 = BusinessImage(business_id=3, url="https://i.postimg.cc/FRtLt2GM/Meowbec.webp", preview=False, menu_id=18)
    hc_business_image13 = BusinessImage(business_id=3, url="https://i.postimg.cc/tTX9Vkg1/Meow-Meow-Fantasy.jpg", preview=False, menu_id=19)
    hc_business_image14 = BusinessImage(business_id=3, url="https://i.postimg.cc/PrBhMTxn/Dragons-Breath.jpg", preview=False, menu_id=20)

    # Continental Hotel (13 Images Total)
    ch_business_image1 = BusinessImage(business_id=4, url="https://i.postimg.cc/9QJ1ytC4/Continental-Hotel-Preview.webp", preview=True)
    ch_business_image2 = BusinessImage(business_id=4, url="https://i.postimg.cc/xTVsQ16d/Continental-Hotel-Filler.jpg", preview=False)
    ch_business_image3 = BusinessImage(business_id=4, url="https://i.postimg.cc/rpZn2GH6/Continental-Hotel-Filler-Lounge.png", preview=False)
    ch_business_image4 = BusinessImage(business_id=4, url="https://i.postimg.cc/0Q6tkMgz/Continental-Hotel-Filler-Room.webp", preview=False)
    ch_business_image5 = BusinessImage(business_id=4, url="https://i.postimg.cc/CLCcxp2s/Continental-Hotel-Veal-Marsala.jpg", preview=False, menu_id=21)
    ch_business_image6 = BusinessImage(business_id=4, url="https://i.postimg.cc/x10tkFDD/Continental-Hotel-Tortellini.jpg", preview=False, menu_id=22)
    ch_business_image7 = BusinessImage(business_id=4, url="https://i.postimg.cc/1RqWbqcT/Continental-Hotel-Lobster.jpg", preview=False, menu_id=23)
    ch_business_image8 = BusinessImage(business_id=4, url="https://i.postimg.cc/13H7J1c3/Continental-Hotel-Caeser-Salad.jpg", preview=False, menu_id=24)
    ch_business_image9 = BusinessImage(business_id=4, url="https://i.postimg.cc/Pq537V2z/Continental-Hotel-Assorted-Baked-Clams.jpg", preview=False, menu_id=25)
    ch_business_image10 = BusinessImage(business_id=4, url="https://i.postimg.cc/wML0NCjH/Continental-Hotel-Pinot-Noir.jpg", preview=False, menu_id=26)
    ch_business_image11 = BusinessImage(business_id=4, url="https://i.postimg.cc/zB9xVz50/Continental-Hotel-Hibiki.png", preview=False, menu_id=27)
    ch_business_image12 = BusinessImage(business_id=4, url="https://i.postimg.cc/L6jbg1Jf/Continental-Hotel-Gelato.jpg", preview=False, menu_id=28)
    ch_business_image13 = BusinessImage(business_id=4, url="https://i.postimg.cc/rwcY1w4H/Continental-Hotel-Bandaid.jpg", preview=False, menu_id=29)


    # Baratie (6 Images Total)
    ba_business_image1 = BusinessImage(business_id=5, url="https://i.postimg.cc/xT5kt67P/Baratie-Preview.webp", preview=True)
    ba_business_image2 = BusinessImage(business_id=5, url="https://i.postimg.cc/HkLrKQ11/Baratie-Owner.webp", preview=False)
    ba_business_image3 = BusinessImage(business_id=5, url="https://i.postimg.cc/3NCyM1wY/Baratie-Absolute.png", preview=False, menu_id=31)
    ba_business_image4 = BusinessImage(business_id=5, url="https://i.postimg.cc/rySRtVN3/Baratie-Blessing-of-East-Blue.png", preview=False, menu_id=32)
    ba_business_image5 = BusinessImage(business_id=5, url="https://i.postimg.cc/T1XyHFft/Baratie-Mandarin-Orange-Jelly.png", preview=False, menu_id=33)
    ba_business_image6 = BusinessImage(business_id=5, url="https://i.postimg.cc/Qxh9Q26t/Baratie-Red-Nosed-Mousse.png", preview=False, menu_id=34)

    # Cafe Leblanc (4 Images Total)
    cl_business_image1 = BusinessImage(business_id=6, url="https://i.postimg.cc/ZnWWnN4y/Cafe-Leblanc-Preview.png", preview=True)
    cl_business_image2 = BusinessImage(business_id=6, url="https://i.postimg.cc/9f2wbztv/Cafe-Leblanc-Filler.webp", preview=False)
    cl_business_image3 = BusinessImage(business_id=6, url="https://i.postimg.cc/xCxk95D2/Cafe-Leblanc-Curry-Coffee.jpg", preview=False, menu_id=35)
    cl_business_image4 = BusinessImage(business_id=6, url="https://i.postimg.cc/hG0z5g2h/Cafe-Leblanc-Hotdog-Coffee.jpg", preview=False, menu_id=36)
    cl_business_image5 = BusinessImage(business_id=6, url="https://i.postimg.cc/xCTJr7Z5/Cafe-Leblanc-Omelette-Coffee.jpg", preview=False, menu_id=37)
    cl_business_image6 = BusinessImage(business_id=6, url="https://i.postimg.cc/2ShBnnvQ/Cafe-Leblanc-Deluxe-Curry.jpg", preview=False, menu_id=38)

    # Urahara Shoten (3 Images Total)
    us_business_image1 = BusinessImage(business_id=7, url="https://i.postimg.cc/rF4ghnt3/Urahara-Shoten-Preview.webp", preview=True)
    us_business_image2 = BusinessImage(business_id=7, url="https://i.postimg.cc/Y2hdFq2p/Urahara-Shoten-Kurosaki-Curry.jpg", preview=False, menu_id=40)
    us_business_image3 = BusinessImage(business_id=7, url="https://i.postimg.cc/MXJGdFJz/Urahara-Shoten-Kirio-Feast.webp", preview=False, menu_id=41)
    us_business_image4 = BusinessImage(business_id=7, url="https://i.postimg.cc/WpCXwLt0/Urahara-Shoten-Kon-Dog.jpg", preview=False, menu_id=42)

    # Four Horsemen Izakaya (5 Images Total)
    fhi_business_image1 = BusinessImage(business_id=8, url="https://i.postimg.cc/nr2VZYsJ/Four-Horsemen-Izakaya-Preview.jpg", preview=True)
    fhi_business_image4 = BusinessImage(business_id=8, url="https://i.postimg.cc/MZmpyx9F/Four-Horsemen-Izakaya-Denji-Morning-After.jpg", preview=False, menu_id=43)
    fhi_business_image5 = BusinessImage(business_id=8, url="https://i.postimg.cc/FsPFBp5b/Four-Horsemen-Izakaya-Pochita-Bites.jpg", preview=False, menu_id=44)
    fhi_business_image2 = BusinessImage(business_id=8, url="https://i.postimg.cc/pXVXC77X/Four-Horsemen-Izakaya-Makima-Curry-Udon.jpg", preview=False, menu_id=45)
    fhi_business_image3 = BusinessImage(business_id=8, url="https://i.postimg.cc/t4wqXggY/Four-Horsemen-Izakaya-Hayakawa-Gyoza.png", preview=False, menu_id=46)

    # Animal Crossing Deli and Cafe (5 Images Total)
    acd_business_image1 = BusinessImage(business_id=9, url="https://i.postimg.cc/KjLRtgsk/Animal-Crossing-Deli-Tomato-Bagel.png", preview=True, menu_id=47)
    acd_business_image2 = BusinessImage(business_id=9, url="https://i.postimg.cc/Gp2tqf51/Animal-Crossing-Deli-Veggie-Sandwich.png", preview=False, menu_id=48)
    acd_business_image3 = BusinessImage(business_id=9, url="https://i.postimg.cc/cLdr8C7C/Animal-Crossing-Deli-Mixed-Fruits-Sandwich.png", preview=False, menu_id=49)
    acd_business_image4 = BusinessImage(business_id=9, url="https://i.postimg.cc/W1StmVSn/Animal-Crossing-Deli-Pumpkin-Bagel.png", preview=False, menu_id=50)
    acd_business_image5 = BusinessImage(business_id=9, url="https://i.postimg.cc/ZKt94VCr/Animal-Crossing-Deli-Salmon-Bagel.png", preview=False, menu_id=51)
    acd_business_image6 = BusinessImage(business_id=9, url="https://i.postimg.cc/DfWs2S5K/Animal-Crossing-Deli-Apple-Smoothie.webp", preview=False, menu_id=52)
    acd_business_image7 = BusinessImage(business_id=9, url="https://i.postimg.cc/mkFT0fQ0/Animal-Crossing-Deli-Iced-Caffee-Latte.webp", preview=False, menu_id=55)
    acd_business_image8 = BusinessImage(business_id=9, url="https://i.postimg.cc/cHPvKcTG/Animal-Crossing-Deli-Peach-Smoothie.webp", preview=False, menu_id=53)
    acd_business_image9 = BusinessImage(business_id=9, url="https://i.postimg.cc/05LSr9HK/Animal-Crossing-Deli-Coconut-Juice.webp", preview=False, menu_id=54)

    # Ghibli's Desserts (6 Images Total)
    gd_business_image1 = BusinessImage(business_id=10, url="https://i.postimg.cc/N0wVHkTK/totoro-cupcake.png", preview=True, menu_id=56)
    gd_business_image2 = BusinessImage(business_id=10, url="https://i.postimg.cc/mrNnN1N8/Screenshot-2024-03-13-at-8-05-40-PM-removebg-preview.png", preview=False, menu_id=57)
    gd_business_image3 = BusinessImage(business_id=10, url="https://i.postimg.cc/28VPR6rS/cat-bus-eclair.png", preview=False, menu_id=58)
    gd_business_image4 = BusinessImage(business_id=10, url="https://i.postimg.cc/wjNZMGtK/ponyo-cheesecake.png", preview=False, menu_id=59)
    gd_business_image5 = BusinessImage(business_id=10, url="https://i.postimg.cc/xCf4sj6Y/soot-vanilla-tart.png", preview=False, menu_id=60)
    gd_business_image6 = BusinessImage(business_id=10, url="https://i.postimg.cc/SN3Hyhx7/no-face-swiss-roll.png", preview=False, menu_id=61)
    gd_business_image7 = BusinessImage(business_id=10, url="https://i.postimg.cc/DfCtMsVN/jiji-donut.png", preview=False, menu_id=62)
    gd_business_image8 = BusinessImage(business_id=10, url="https://i.postimg.cc/ZnD2vkFm/otori-sama-macaron.png", preview=False, menu_id=63)

    db.session.add_all([
        pc_business_image1, pc_business_image2, pc_business_image3, pc_business_image4, pc_business_image5, pc_business_image6,pc_business_image7,
        sf_business_image1, sf_business_image2, sf_business_image3, sf_business_image4, sf_business_image5, sf_business_image6,
        hc_business_image1, hc_business_image2, hc_business_image3, hc_business_image4, hc_business_image5,
        hc_business_image6, hc_business_image7, hc_business_image8, hc_business_image9, hc_business_image10, hc_business_image13, hc_business_image14,
        hc_business_image11, hc_business_image12, ch_business_image1, ch_business_image2, ch_business_image3,
        ch_business_image4, ch_business_image5, ch_business_image6, ch_business_image7, ch_business_image8, ch_business_image12, ch_business_image13,
        ch_business_image9, ch_business_image10, ch_business_image11, ba_business_image1, ba_business_image2,
        ba_business_image3, ba_business_image4, ba_business_image5, ba_business_image6, cl_business_image1, cl_business_image2, cl_business_image3, cl_business_image4, cl_business_image5, cl_business_image6,
        us_business_image1, us_business_image2, us_business_image3, us_business_image4, fhi_business_image1, fhi_business_image2,
        fhi_business_image3, fhi_business_image4, fhi_business_image5, acd_business_image1, acd_business_image2,
        acd_business_image3, acd_business_image4, acd_business_image5, acd_business_image6, acd_business_image7, acd_business_image8, acd_business_image9, gd_business_image1, gd_business_image2,
        gd_business_image3, gd_business_image4, gd_business_image5, gd_business_image6, gd_business_image7, gd_business_image8
    ])
    db.session.commit()


def undo_business_images():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.business_images RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM business_images"))

    db.session.commit()

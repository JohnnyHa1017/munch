from app.models import db, BusinessImage, environment, SCHEMA
from sqlalchemy.sql import text

def seed_business_images():
    # Pokemon Cafe (5 Images Total)
    pc_business_image1 = BusinessImage(business_id=1, url="https://i.postimg.cc/DzpmhSnJ/cheesyrowletpizza.jpg", preview=True)
    pc_business_image2 = BusinessImage(business_id=1, url="https://i.postimg.cc/qR8fLFbJ/piquantpikachucurry.jpg", preview=False)
    pc_business_image3 = BusinessImage(business_id=1, url="https://i.postimg.cc/kGK5Ww8K/happysnorlaxlocomoco.jpg", preview=False)
    pc_business_image4 = BusinessImage(business_id=1, url="https://i.postimg.cc/QCs2nqwp/teddiursaicedcoffee.jpg", preview=False)
    pc_business_image5 = BusinessImage(business_id=1, url="https://i.postimg.cc/d173VJVW/eeveelatte.jpg", preview=False)

    # Stardew Farmhouse (4 Images Total)
    sf_business_image1 = BusinessImage(business_id=2, url="https://i.postimg.cc/g2KyRJSJ/Cheese-Cauliflower.png", preview=True)
    sf_business_image2 = BusinessImage(business_id=2, url="https://i.postimg.cc/gcfKb1LY/Artichoke-Dip.png", preview=False)
    sf_business_image3 = BusinessImage(business_id=2, url="https://i.postimg.cc/wTLQqFDD/Fiddlehead-Risotto.png", preview=False)
    sf_business_image4 = BusinessImage(business_id=2, url="https://i.postimg.cc/MGPyPL8J/Eggplant-Parmesan.png", preview=False)

    # Hunters Cafe (12 Images Total)
    hc_business_image1 = BusinessImage(business_id=3, url="https://i.postimg.cc/PfS5YgYd/tokyo-hunters-bar-preview.jpg", preview=True)
    hc_business_image2 = BusinessImage(business_id=3, url="https://i.postimg.cc/tJvRb6ps/tokyo-hunters-bar-filler.jpg", preview=False)
    hc_business_image3 = BusinessImage(business_id=3, url="https://i.postimg.cc/hvt4NsWF/tokyo-hunters-bar-gaming.jpg", preview=False)
    hc_business_image4 = BusinessImage(business_id=3, url="https://i.postimg.cc/Z5BnTw94/tokyo-hunters-bar-dragon.jpg", preview=False)
    hc_business_image5 = BusinessImage(business_id=3, url="https://i.postimg.cc/5Nkjdh2s/tokyo-hunters-bar-decor.jpg", preview=False)
    hc_business_image6 = BusinessImage(business_id=3, url="https://i.postimg.cc/CK8R4cYm/tokyo-hunters-bar-cooking.jpg", preview=False)
    hc_business_image7 = BusinessImage(business_id=3, url="https://i.postimg.cc/vTYDbMnN/tokyo-hunters-bar-butcher.jpg", preview=False)
    hc_business_image8 = BusinessImage(business_id=3, url="https://i.postimg.cc/qqPY2BGm/Yakitori-Combo.jpg", preview=False)
    hc_business_image9 = BusinessImage(business_id=3, url="https://i.postimg.cc/fLg1TfSQ/Niang-Co-Sake.jpg", preview=False)
    hc_business_image10 = BusinessImage(business_id=3, url="https://i.postimg.cc/RFzNpwZ9/Hunters-Tofu.jpg", preview=False)
    hc_business_image11 = BusinessImage(business_id=3, url="https://i.postimg.cc/W1kpRtK4/Yuzu-Beef-Steak.jpg", preview=False)
    hc_business_image12 = BusinessImage(business_id=3, url="https://i.postimg.cc/FRtLt2GM/Meowbec.webp", preview=False)

    # Continental Hotel (11 Images Total)
    ch_business_image1 = BusinessImage(business_id=4, url="https://i.postimg.cc/9QJ1ytC4/Continental-Hotel-Preview.webp", preview=True)
    ch_business_image2 = BusinessImage(business_id=4, url="https://i.postimg.cc/xTVsQ16d/Continental-Hotel-Filler.jpg", preview=False)
    ch_business_image3 = BusinessImage(business_id=4, url="https://i.postimg.cc/rpZn2GH6/Continental-Hotel-Filler-Lounge.png", preview=False)
    ch_business_image4 = BusinessImage(business_id=4, url="https://i.postimg.cc/0Q6tkMgz/Continental-Hotel-Filler-Room.webp", preview=False)
    ch_business_image5 = BusinessImage(business_id=4, url="https://i.postimg.cc/CLCcxp2s/Continental-Hotel-Veal-Marsala.jpg", preview=False)
    ch_business_image6 = BusinessImage(business_id=4, url="https://i.postimg.cc/x10tkFDD/Continental-Hotel-Tortellini.jpg", preview=False)
    ch_business_image7 = BusinessImage(business_id=4, url="https://i.postimg.cc/1RqWbqcT/Continental-Hotel-Lobster.jpg", preview=False)
    ch_business_image8 = BusinessImage(business_id=4, url="https://i.postimg.cc/13H7J1c3/Continental-Hotel-Caeser-Salad.jpg", preview=False)
    ch_business_image9 = BusinessImage(business_id=4, url="https://i.postimg.cc/Pq537V2z/Continental-Hotel-Assorted-Baked-Clams.jpg", preview=False)
    ch_business_image10 = BusinessImage(business_id=4, url="https://i.postimg.cc/wML0NCjH/Continental-Hotel-Pinot-Noir.jpg", preview=False)
    ch_business_image11 = BusinessImage(business_id=4, url="https://i.postimg.cc/zB9xVz50/Continental-Hotel-Hibiki.png", preview=False)

    # Baratie (6 Images Total)
    ba_business_image1 = BusinessImage(business_id=5, url="https://i.postimg.cc/xT5kt67P/Baratie-Preview.webp", preview=True)
    ba_business_image2 = BusinessImage(business_id=5, url="https://i.postimg.cc/HkLrKQ11/Baratie-Owner.webp", preview=False)
    ba_business_image3 = BusinessImage(business_id=5, url="https://i.postimg.cc/3NCyM1wY/Baratie-Absolute.png", preview=False)
    ba_business_image4 = BusinessImage(business_id=5, url="https://i.postimg.cc/rySRtVN3/Baratie-Blessing-of-East-Blue.png", preview=False)

    # Cafe Leblanc (4 Images Total)
    cl_business_image1 = BusinessImage(business_id=6, url="https://i.postimg.cc/ZnWWnN4y/Cafe-Leblanc-Preview.png", preview=True)
    cl_business_image2 = BusinessImage(business_id=6, url="https://i.postimg.cc/9f2wbztv/Cafe-Leblanc-Filler.webp", preview=False)
    cl_business_image3 = BusinessImage(business_id=6, url="https://i.postimg.cc/xCxk95D2/Cafe-Leblanc-Curry-Coffee.jpg", preview=False)
    cl_business_image4 = BusinessImage(business_id=6, url="https://i.postimg.cc/hG0z5g2h/Cafe-Leblanc-Hotdog-Coffee.jpg", preview=False)

    # Urahara Shoten (3 Images Total)
    us_business_image1 = BusinessImage(business_id=7, url="https://i.postimg.cc/rF4ghnt3/Urahara-Shoten-Preview.webp", preview=True)
    us_business_image2 = BusinessImage(business_id=7, url="https://i.postimg.cc/dVK6g221/Urahara-Shoten-Filler.webp", preview=False)
    us_business_image3 = BusinessImage(business_id=7, url="https://i.postimg.cc/Y2hdFq2p/Urahara-Shoten-Kurosaki-Curry.jpg", preview=False)

    # Four Horsemen Izakaya (5 Images Total)
    fhi_business_image1 = BusinessImage(business_id=8, url="https://i.postimg.cc/nr2VZYsJ/Four-Horsemen-Izakaya-Preview.jpg", preview=True)
    fhi_business_image2 = BusinessImage(business_id=8, url="https://i.postimg.cc/VNtY5cS4/Four-Horsemen-Izakaya-Filler.avif", preview=False)
    fhi_business_image3 = BusinessImage(business_id=8, url="https://i.postimg.cc/Dw8fkGn9/Four-Horsemen-Izakaya-Drunk.webp", preview=False)
    fhi_business_image4 = BusinessImage(business_id=8, url="https://i.postimg.cc/MZmpyx9F/Four-Horsemen-Izakaya-Denji-Morning-After.jpg", preview=False)
    fhi_business_image5 = BusinessImage(business_id=8, url="https://i.postimg.cc/FsPFBp5b/Four-Horsemen-Izakaya-Pochita-Bites.jpg", preview=False)

    # Animal Crossing Deli and Cafe (5 Images Total)
    acd_business_image1 = BusinessImage(business_id=9, url="https://i.postimg.cc/KjLRtgsk/Animal-Crossing-Deli-Tomato-Bagel.png", preview=True)
    acd_business_image2 = BusinessImage(business_id=9, url="https://i.postimg.cc/Gp2tqf51/Animal-Crossing-Deli-Veggie-Sandwich.png", preview=False)
    acd_business_image3 = BusinessImage(business_id=9, url="https://i.postimg.cc/cLdr8C7C/Animal-Crossing-Deli-Mixed-Fruits-Sandwich.png", preview=False)
    acd_business_image4 = BusinessImage(business_id=9, url="https://i.postimg.cc/W1StmVSn/Animal-Crossing-Deli-Pumpkin-Bagel.png", preview=False)
    acd_business_image5 = BusinessImage(business_id=9, url="https://i.postimg.cc/ZKt94VCr/Animal-Crossing-Deli-Salmon-Bagel.png", preview=False)
    acd_business_image6 = BusinessImage(business_id=9, url="https://i.postimg.cc/DfWs2S5K/Animal-Crossing-Deli-Apple-Smoothie.webp", preview=False)
    acd_business_image7 = BusinessImage(business_id=9, url="https://i.postimg.cc/mkFT0fQ0/Animal-Crossing-Deli-Iced-Caffee-Latte.webp", preview=False)


    # Ghibli's Desserts (6 Images Total)
    gd_business_image1 = BusinessImage(business_id=10, url="https://i.postimg.cc/N0wVHkTK/totoro-cupcake.png", preview=True)
    gd_business_image2 = BusinessImage(business_id=10, url="https://i.postimg.cc/mrNnN1N8/Screenshot-2024-03-13-at-8-05-40-PM-removebg-preview.png", preview=False)
    gd_business_image3 = BusinessImage(business_id=10, url="https://i.postimg.cc/28VPR6rS/cat-bus-eclair.png", preview=False)
    gd_business_image4 = BusinessImage(business_id=10, url="https://i.postimg.cc/wjNZMGtK/ponyo-cheesecake.png", preview=False)
    gd_business_image5 = BusinessImage(business_id=10, url="https://i.postimg.cc/xCf4sj6Y/soot-vanilla-tart.png", preview=False)
    gd_business_image6 = BusinessImage(business_id=10, url="https://i.postimg.cc/SN3Hyhx7/no-face-swiss-roll.png", preview=False)

    db.session.add_all([
        pc_business_image1, pc_business_image2, pc_business_image3, pc_business_image4, pc_business_image5,
        sf_business_image1, sf_business_image2, sf_business_image3, sf_business_image4,
        hc_business_image1, hc_business_image2, hc_business_image3, hc_business_image4, hc_business_image5,
        hc_business_image6, hc_business_image7, hc_business_image8, hc_business_image9, hc_business_image10,
        hc_business_image11, hc_business_image12, ch_business_image1, ch_business_image2, ch_business_image3,
        ch_business_image4, ch_business_image5, ch_business_image6, ch_business_image7, ch_business_image8,
        ch_business_image9, ch_business_image10, ch_business_image11, ba_business_image1, ba_business_image2,
        ba_business_image3, ba_business_image4, cl_business_image1, cl_business_image2, cl_business_image3, cl_business_image4,
        us_business_image1, us_business_image2, us_business_image3, fhi_business_image1, fhi_business_image2,
        fhi_business_image3, fhi_business_image4, fhi_business_image5, acd_business_image1, acd_business_image2,
        acd_business_image3, acd_business_image4, acd_business_image5, acd_business_image6, acd_business_image7, gd_business_image1, gd_business_image2,
        gd_business_image3, gd_business_image4, gd_business_image5, gd_business_image6
    ])
    db.session.commit()


def undo_business_images():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.business_images RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM business_images"))

    db.session.commit()

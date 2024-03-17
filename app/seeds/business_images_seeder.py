from app.models import db, BusinessImage, environment, SCHEMA
from sqlalchemy.sql import text

def seed_business_images():
        # Pokemon Cafe (6 Images Total)
    pc_business_image1 = BusinessImage(business_id=1, url="1", preview=True)
    pc_business_image2 = BusinessImage(business_id=1, url="2", preview=False)
    pc_business_image3 = BusinessImage(business_id=1, url="3", preview=False)
    pc_business_image4 = BusinessImage(business_id=1, url="4", preview=False)
    pc_business_image5 = BusinessImage(business_id=1, url="5", preview=False)
    pc_business_image6 = BusinessImage(business_id=1, url="6", preview=False)

    # Stardew Farmhouse (4 Images Total)
    sf_business_image1 = BusinessImage(business_id=2, url="7", preview=True)
    sf_business_image2 = BusinessImage(business_id=2, url="8", preview=False)
    sf_business_image3 = BusinessImage(business_id=2, url="9", preview=False)
    sf_business_image4 = BusinessImage(business_id=2, url="10", preview=False)

    # Hunters Cafe (12 Images Total)
    hc_business_image1 = BusinessImage(business_id=3, url="11", preview=True)
    hc_business_image2 = BusinessImage(business_id=3, url="12", preview=False)
    hc_business_image3 = BusinessImage(business_id=3, url="13", preview=False)
    hc_business_image4 = BusinessImage(business_id=3, url="14", preview=False)
    hc_business_image5 = BusinessImage(business_id=3, url="15", preview=False)
    hc_business_image6 = BusinessImage(business_id=3, url="16", preview=False)
    hc_business_image7 = BusinessImage(business_id=3, url="17", preview=False)
    hc_business_image8 = BusinessImage(business_id=3, url="18", preview=False)
    hc_business_image9 = BusinessImage(business_id=3, url="19", preview=False)
    hc_business_image10 = BusinessImage(business_id=3, url="20", preview=False)
    hc_business_image11 = BusinessImage(business_id=3, url="21", preview=False)
    hc_business_image12 = BusinessImage(business_id=3, url="22", preview=False)

    # Continental Hotel (11 Images Total)
    ch_business_image1 = BusinessImage(business_id=4, url="23", preview=True)
    ch_business_image2 = BusinessImage(business_id=4, url="24", preview=False)
    ch_business_image3 = BusinessImage(business_id=4, url="25", preview=False)
    ch_business_image4 = BusinessImage(business_id=4, url="26", preview=False)
    ch_business_image5 = BusinessImage(business_id=4, url="27", preview=False)
    ch_business_image6 = BusinessImage(business_id=4, url="28", preview=False)
    ch_business_image7 = BusinessImage(business_id=4, url="29", preview=False)
    ch_business_image8 = BusinessImage(business_id=4, url="30", preview=False)
    ch_business_image9 = BusinessImage(business_id=4, url="31", preview=False)
    ch_business_image10 = BusinessImage(business_id=4, url="32", preview=False)
    ch_business_image11 = BusinessImage(business_id=4, url="33", preview=False)

    # Baratie (7 Images Total)
    ba_business_image1 = BusinessImage(business_id=5, url="34", preview=True)
    ba_business_image2 = BusinessImage(business_id=5, url="35", preview=False)
    ba_business_image3 = BusinessImage(business_id=5, url="36", preview=False)
    ba_business_image4 = BusinessImage(business_id=5, url="37", preview=False)
    ba_business_image5 = BusinessImage(business_id=5, url="38", preview=False)
    ba_business_image6 = BusinessImage(business_id=5, url="39", preview=False)
    ba_business_image7 = BusinessImage(business_id=5, url="40", preview=False)

    # Cafe Leblanc (5 Images Total)
    cl_business_image1 = BusinessImage(business_id=6, url="41", preview=True)
    cl_business_image2 = BusinessImage(business_id=6, url="42", preview=False)
    cl_business_image3 = BusinessImage(business_id=6, url="43", preview=False)
    cl_business_image4 = BusinessImage(business_id=6, url="44", preview=False)
    cl_business_image5 = BusinessImage(business_id=6, url="45", preview=False)

    # Urahara Shoten (3 Images Total)
    us_business_image1 = BusinessImage(business_id=7, url="46", preview=True)
    us_business_image2 = BusinessImage(business_id=7, url="47", preview=False)
    us_business_image3 = BusinessImage(business_id=7, url="48", preview=False)

    # Four Horsemen Izakaya (5 Images Total)
    fhi_business_image1 = BusinessImage(business_id=8, url="49", preview=True)
    fhi_business_image2 = BusinessImage(business_id=8, url="50", preview=False)
    fhi_business_image3 = BusinessImage(business_id=8, url="51", preview=False)
    fhi_business_image4 = BusinessImage(business_id=8, url="52", preview=False)
    fhi_business_image5 = BusinessImage(business_id=8, url="53", preview=False)

    # Animal Crossing Deli and Cafe (5 Images Total)
    acd_business_image1 = BusinessImage(business_id=9, url="54", preview=True)
    acd_business_image2 = BusinessImage(business_id=9, url="55", preview=False)
    acd_business_image3 = BusinessImage(business_id=9, url="56", preview=False)
    acd_business_image4 = BusinessImage(business_id=9, url="57", preview=False)
    acd_business_image5 = BusinessImage(business_id=9, url="58", preview=False)

    # Ghibli's Desserts (6 Images Total)
    gd_business_image1 = BusinessImage(business_id=10, url="59", preview=True)
    gd_business_image2 = BusinessImage(business_id=10, url="60", preview=False)
    gd_business_image3 = BusinessImage(business_id=10, url="61", preview=False)
    gd_business_image4 = BusinessImage(business_id=10, url="62", preview=False)
    gd_business_image5 = BusinessImage(business_id=10, url="63", preview=False)
    gd_business_image6 = BusinessImage(business_id=10, url="64", preview=False)

    db.session.add_all([
        pc_business_image1, pc_business_image2, pc_business_image3, pc_business_image4, pc_business_image5,
        pc_business_image6, sf_business_image1, sf_business_image2, sf_business_image3, sf_business_image4,
        hc_business_image1, hc_business_image2, hc_business_image3, hc_business_image4, hc_business_image5,
        hc_business_image6, hc_business_image7, hc_business_image8, hc_business_image9, hc_business_image10,
        hc_business_image11, hc_business_image12, ch_business_image1, ch_business_image2, ch_business_image3,
        ch_business_image4, ch_business_image5, ch_business_image6, ch_business_image7, ch_business_image8,
        ch_business_image9, ch_business_image10, ch_business_image11, ba_business_image1, ba_business_image2,
        ba_business_image3, ba_business_image4, ba_business_image5, ba_business_image6, ba_business_image7,
        cl_business_image1, cl_business_image2, cl_business_image3, cl_business_image4, cl_business_image5,
        us_business_image1, us_business_image2, us_business_image3, fhi_business_image1, fhi_business_image2,
        fhi_business_image3, fhi_business_image4, fhi_business_image5, acd_business_image1, acd_business_image2,
        acd_business_image3, acd_business_image4, acd_business_image5, gd_business_image1, gd_business_image2,
        gd_business_image3, gd_business_image4, gd_business_image5, gd_business_image6
    ])
    db.session.commit()


def undo_business_images():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.business_images RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM business_images"))

    db.session.commit()

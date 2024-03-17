from app.models import db, Menu, environment, SCHEMA
from sqlalchemy.sql import text

def seed_menus():
    Cheesy_Rowlet_Pizza = Menu(
        business_id=1,
        name="Cheese Rowlet Pizza",
        category="Appetizer",
        price=14.95,
        description="A Rowlet white sauce and basil pizza and a pokeball marinara and cheese thin crust pizza",
    )

    Piquant_Pikachu_Curry = Menu(
        business_id=1,
        name="Piquant Pikachu Curry",
        category="Entree",
        price=25.95,
        description="Red curry with carrots, potatoes, and onions cut into star shapes. Comes with a rice shaped Pikachu",
    )

    Happy_Snorlax_Loco_Moco = Menu(
        business_id=1,
        name="Happy Snorlax Loco Moco",
        category="Entree",
        price=28.95,
        description="White rice topped with a Snorlax hamburger patty with a sunny-side up fried egg. Comes with a side salad and a cup of soup",
    )

    Teddiursa_Iced_Coffee = Menu(
        business_id=1,
        name="Teddiursa Iced Coffee",
        category="Drink",
        price=7.95,
        description="An iced coffee with donuts in the shape of Teddiursa's ears",
    )

    Eevee_Latte = Menu(
        business_id=1,
        name="Eevee Latte",
        category="Drink",
        price=5.95,
        description="Hot or iced vanilla latte with Eevee art",
    )

    Fluffy_Eevee_Pancakes = Menu(
        business_id=1,
        name="Fluffy Eevee pancakes",
        category="Dessert",
        price=14.95,
        description="Three fluffy pancakes served with whipped cream and fresh fruit",
    )

    Burnt_Caramel_Vulpix_Sundae = Menu(
        business_id=1,
        name="Burnt-Caramel Vulpix Sundae",
        category="Dessert",
        price=15.95,
        description="Vanilla ice cream, chocolate chips, caramel drizzle, chocolate wafer, and bananas",
    )

    Cheese_Cauliflower = Menu(
        business_id=2,
        name="Cheese Cauliflower",
        category="Appetizer",
        price=8.95,
        description="Roasted cauliflower baked in a gratin cheese sauce",
    )

    Artichoke_Dip = Menu(
        business_id=2,
        name="Artichoke Dip",
        category="Appetizer",
        price=7.95,
        description="Cool and refreshing baked artichoke dip topped with golden breadcrumbs",
    )

    Fiddlehead_Risotto = Menu(
        business_id=2,
        name="Fiddlehead Risotto",
        category="Entree",
        price=12.95,
        description="A creamy rice dish served with sauteed fern heads",
    )

    Eggplant_Parmesan = Menu(
        business_id=2,
        name="Eggplant Parmesan",
        category="Entree",
        price=11.95,
        description="Crispy baked eggplant layered with marinara, herbs, and cheese",
    )

    Banana_Pudding = Menu(
        business_id=2,
        name="Banana Pudding",
        category="Dessert",
        price=5.95,
        description="A creamy dessert with a wonderful tropical flavor",
    )

    Triple_Shot_Espresso = Menu(
        business_id=2,
        name="Triple Shot Espresso",
        category="Drink",
        price=3.99,
        description="It's more potent than regular coffee!",
    )

    Yakitori_Combo = Menu(
        business_id=3,
        name="Yakitori Combo",
        category="Appetizer",
        price=12.99,
        description="A combination of 8 different kinds of Yakitori, including chicken, beef and pepper, shrimp, etc.",
    )

    Niang_Co_Sake = Menu(
        business_id=3,
        name="Niang Co Sake",
        category="Drink",
        price=28.99,
        description="Premium sake imported from Japan, carefully selected by our feline mixologist",
    )

    Hunters_Tofu = Menu(
        business_id=3,
        name="Hunter’s Tofu",
        category="Appetizer",
        price=8.99,
        description="Tofu steak with umeboshi sauce",
    )

    Yuzu_Beef_Steak = Menu(
        business_id=3,
        name="Yuzu Beef Steak",
        category="Entree",
        price=29.99,
        description="Kobe beef directly imported from Japan, carefully selected by chef",
    )

    Meowbec = Menu(
        business_id=3,
        name="Meowbec",
        category="Drink",
        price=19.99,
        description="Wine made by our feline friends",
    )

    Meow_Meow_Fantasy = Menu(
        business_id=3,
        name="Meow Meow Fantasy",
        category="Drink",
        price=12.99,
        description="Cocktail mixed with all kinds of fruits",
    )

    Dragons_Breath = Menu(
        business_id=3,
        name="Dragon’s Breath",
        category="Drink",
        price=6.99,
        description="Premium beer imported from Japan",
    )

    Veal_Marsala = Menu(
        business_id=4,
        name="Veal Marsala",
        category="Entree",
        price=90.00,
        description="Premium beef steaks and calamari cooked with wine",
    )

    Tortellini_al_Ragu = Menu(
        business_id=4,
        name="Tortellini al Ragu",
        category="Entree",
        price=32.00,
        description="Tender pasta filled with savory meat in rich ragu sauce",
    )

    Lobster_Ravioli = Menu(
        business_id=4,
        name="Lobster Ravioli",
        category="Entree",
        price=50.00,
        description="Luxurious pasta pillows stuffed with succulent lobster meat, served in a creamy sauce infused with herbs and seafood essence.",
    )

    Caesar_Salad = Menu(
        business_id=4,
        name="Caesar Salad",
        category="Appetizer",
        price=42.00,
        description="Crisp romaine lettuce tossed in creamy Caesar dressing, topped with crunchy croutons and grated Parmesan cheese.",
    )

    Assorted_Baked_Clams = Menu(
        business_id=4,
        name="Assorted Baked Clams",
        category="Appetizer",
        price=39.00,
        description="Fresh claims filled with a medley of breadcrumbs, garlic, herbs, and sometimes cheese, baked until golden and flavorful.",
    )

    Continental_Pinot_Noir = Menu(
        business_id=4,
        name="Continental Pinot Noir",
        category="Drink",
        price=39.00,
        description="Continental secret wine selected by Winston",
    )

    Hibiki_100_YO = Menu(
        business_id=4,
        name="Hibiki 100 YO",
        category="Drink",
        price=50000.00,
        description="Winston’s favorite drink",
    )

    Killer_Gelato = Menu(
        business_id=4,
        name="Killer Gelato",
        category="Dessert",
        price=25.00,
        description="Gelato cold as John",
    )

    Band_Aid = Menu(
        business_id=4,
        name="Band Aid",
        category="Specials",
        price=100.00,
        description="A magic band aid will cure any of your injuries!",
    )

    Raw_Ham_Melon = Menu(
        id=5,
        name="Raw Ham Melon",
        category="Appetizer",
        price=8.99,
        description="Savor the flavors of Italy with our Raw Ham Melon, inspired by the classic Italian dish Prosciutto e Melone. This appetizer features thinly sliced raw ham draped over sweet, ripe cantaloupe melon, creating a perfect harmony of savory and sweet flavors.",
    )

    Absolute_Justice = Menu(
        id=5,
        name="Absolute Justice",
        category="Entree",
        price=23.99,
        description="This exquisite dish features a rich and aromatic Japanese curry sauce, simmered to perfection with tender chunks of carrots, potatoes, and onions. Served additionally with some Samba Beef which is a specialty meat found on Samba island.",
    )

    Blessing_of_East_Blue = Menu(
        id=5,
        name="Blessing of East Blue",
        category="Entree",
        price=20.00,
        description="This savory treasure features a tantalizing blend of tender shrimp, succulent scallops, and flavorful crab meat, all expertly stir-fried with fragrant jasmine rice, fresh vegetables, and a secret blend of exotic spices that will transport your taste buds to the high seas.",
    )

    Mandarin_Orange_Jelly = Menu(
        id=5,
        name="Mandarin Orange Jelly",
        category="Dessert",
        price=9.99,
        description='Indulge in a taste of exotic luxury with our "Mandarin Orange Jelly." Made from succulent mandarin oranges imported directly from the lush groves of Cocoyasi Village on Conomi Islands, this exquisite dessert is a true delicacy. Each delicate slice of mandarin orange is suspended in a bed of light and refreshing jelly, creating a harmonious blend of sweet citrus flavors and silky smooth texture.',
    )

    Red_nosed_great_adventure_Framboise_Mousse = Menu(
        id=5,
        name="Red-nosed great adventure ‘Framboise Mousse’",
        category="Dessert",
        price=12.99,
        description="A decadent dessert that combines the bold flavors of raspberries, blackberries, blueberries, and strawberries in a harmonious blend. Each layer of this velvety mousse is infused with the essence of these luscious berries, creating a symphony of sweet and tart flavors that dance on your palate.",
    )

    Leblanc_Coffee_Set = Menu(
        id=6,
        name="Leblanc Coffee Set",
        category="Specials",
        price=13.99,
        description="Savor the rich, aromatic flavors of our authentic Japanese curry, made with a blend of spices that tantalize your taste buds. Pair it with a freshly brewed cup of coffee",
    )

    Hotdog_Coffee_Set = Menu(
        id=6,
        name="Hotdog + Coffee set",
        category="Specials",
        price=4.50,
        description="Bite into a juicy hotdog nestled in a soft bun, topped with your favorite condiments. Pair it with a steaming cup of freshly brewed coffee",
    )

    Omelette_Sandwich_Coffee_Set = Menu(
        id=6,
        name="Omelette Sandwich + Coffee set",
        category="Specials",
        price=4.00,
        description="Sink your teeth into a fluffy omelette sandwiched between two slices of toasted bread, creating a perfect blend of textures and flavors. Pair it with a steaming cup of coffee",
    )

    Deluxe_Curry = Menu(
        id=6,
        name="Deluxe Curry",
        category="Entree",
        price=8.00,
        description="This exquisite dish features a rich and flavorful curry sauce made from a blend of aromatic spices, slow-cooked to perfection to enhance its depth and complexity",
    )

    Coffee = Menu(
        id=6,
        name="Coffee",
        category="Drink",
        price=3.00,
        description="Made from meticulously selected beans, our pour-over process ensures a rich, nuanced flavor in every sip.",
    )

    Kurosaki_Curry_with_Side_Salad = Menu(
        id=7,
        name="Kurosaki Curry with Side Salad",
        category="Entree",
        price=14.99,
        description="Slow-cooked to perfection, our curry offers a delightful balance of sweetness and spice, served alongside steamed rice for a truly satisfying meal.",
    )

    Kon_Stuffed_Dog = Menu(
        id=7,
        name="Kon’s Stuffed Dog",
        category="Specials",
        price=5.99,
        description="Timeless taste of our classic hotdog, served on a soft bun and topped with tangy ketchup and zesty mustard for that perfect balance of sweet and savory. Customize your experience with optional relish.",
    )

    Kirios_Reiatsu_Imbued_Feast = Menu(
        id=7,
        name="Kirio’s Reiatsu Imbued Feast",
        category="Specials",
        price=349.99,
        description="An unforgettable dining experience, experience our succulent Peking duck, roasted to crispy perfection and served with traditional accompaniments, including delicate pancakes, tangy hoisin sauce, and fresh scallions. (Serves 12 People)",
    )

    Denjis_Morning_After = Menu(
        id=8,
        name="Denji’s Morning After",
        category="Specials",
        price=11.99,
        description="Sink your teeth and indulge in our perfectly toasted bread, slathered with butter, paired with an array of exquisite jams. A delightful treat any time and leaves you craving for more.",
    )

    Honey_Glazed_Pochita_Bites = Menu(
        id=8,
        name="Honey Glazed Pochita Bites",
        category="Appetizer",
        price=14.99,
        description="Savor honey-glazed hotdog bites, paired with tangy Dijon mustard for a sweet and savory appetizer sensation.",
    )

    Makimas_Devil_Curry_Udon = Menu(
        id=8,
        name="Makima’s Devil Curry Udon",
        category="Entree",
        price=16.99,
        description='Delve into the inferno with our "Devil Level" Spicy Curry Udon – a fiery fusion of thick udon noodles and devilishly hot curry.',
    )

    Hayakawa_Gyozas = Menu(
        id=8,
        name="Hayakawa Gyoza’s",
        category="Appetizer",
        price=8.99,
        description="Come try Aki’s savory and juicy pan-fried gyozas—a delectable harmony of succulent fillings and satisfying crunch. (8 Pieces)",
    )

    Tomato_Bagel = Menu(
        id=9,
        name="Tomato Bagel",
        category="Entree",
        price=8.99,
        description="Tomato and lettuce with plain cream cheese",
    )

    Veggie_Sandwich = Menu(
        id=9,
        name="Veggie Sandwich",
        category="Entree",
        price=8.99,
        description="Hot sandwich with tomato, carrot, lettuce, and cheese",
    )

    Mixed_Fruits_Sandwich = Menu(
        id=9,
        name="Mixed Fruits Sandwich",
        category="Entree",
        price=9.99,
        description="Orange, pear, and peaches with whipped cream",
    )

    Pumpkin_Bagel = Menu(
        id=9,
        name="Pumpkin Bagel",
        category="Entree",
        price=8.99,
        description="Cinnamon sugar bagel with house pumpkin spread",
    )

    Salmon_Bagel = Menu(
        id=9,
        name="Salmon Bagel",
        category="Entree",
        price=10.99,
        description="Bagel with plain cream cheese and smoked salmon",
    )

    Apple_Smoothie = Menu(
        id=9,
        name="Apple Smoothie",
        category="Drink",
        price=3.99,
        description="Greek yogurt, oat milk, maple syrup, apples",
    )

    Peach_Smoothie = Menu(
        id=9,
        name="Peach Smoothie",
        category="Drink",
        price=3.99,
        description="Frozen peaches, coconut milk, honey, cinnamon",
    )

    Coconut_Juice = Menu(
        id=9,
        name="Coconut Juice",
        category="Drink",
        price=3.99,
        description="Fresh young coconut",
    )

    Iced_Caffe_Latte = Menu(
        id=9,
        name="Iced Caffe Latte",
        category="Drink",
        price=3.99,
        description="Refreshing ice latte",
    )

    Totoro_Cupcake = Menu(
        id=10,
        name="Totoro Cupcake",
        category="Dessert",
        price=5.50,
        description="Vanilla cake with earl grey frosting shaped as my neighbor Totoro",
    )

    Totoro_Hot_Chocolate = Menu(
        id=10,
        name="Totoro Hot Chocolate",
        category="Dessert",
        price=6.50,
        description="Hot chocolate topped with sweetened whipped cream",
    )

    Cat_Bus_Eclair = Menu(
        id=10,
        name="Cat Bus Eclair",
        category="Dessert",
        price=5.50,
        description="Choux dough pastry filled with a vanilla custard dipped in chocolate",
    )

    Ponyo_Cheesecake = Menu(
        id=10,
        name="Ponyo Cheesecake",
        category="Dessert",
        price=39.95,
        description="No bake butterfly pea cheesecake with graham cracker crust",
    )

    Soot_Vanilla_Tart = Menu(
        id=10,
        name="Soot Vanilla Tart",
        category="Dessert",
        price=6.50,
        description="Hokkaido baked cheese tart topped with charcoal frosting",
    )

    No_Face_Swiss_Roll = Menu(
        id=10,
        name="No Face Swiss Roll",
        category="Dessert",
        price=6.50,
        description="Cookies and cream ube swiss roll",
    )

    Jiji_Donut = Menu(
        id=10,
        name="Jiji Donut",
        category="Dessert",
        price=5.50,
        description="Chocolate donut with a charcoal glaze",
    )

    Otori_sama_Macaron = Menu(
        id=10,
        name="Otori sama Macaron",
        category="Dessert",
        price=5.50,
        description="Lemon macaron layered with grape compote and lemon butter cream",
    )

    db.session.add_all([
        Cheesy_Rowlet_Pizza, Piquant_Pikachu_Curry, Happy_Snorlax_Loco_Moco, Teddiursa_Iced_Coffee,
        Eevee_Latte, Fluffy_Eevee_Pancakes, Burnt_Caramel_Vulpix_Sundae, Cheese_Cauliflower,
        Artichoke_Dip, Fiddlehead_Risotto, Eggplant_Parmesan, Banana_Pudding, Triple_Shot_Espresso,
        Yakitori_Combo, Niang_Co_Sake, Hunters_Tofu, Yuzu_Beef_Steak, Meowbec, Meow_Meow_Fantasy,
        Dragons_Breath, Veal_Marsala, Tortellini_al_Ragu, Lobster_Ravioli, Caesar_Salad,
        Assorted_Baked_Clams, Continental_Pinot_Noir, Hibiki_100_YO, Killer_Gelato, Band_Aid,
        Raw_Ham_Melon, Absolute_Justice, Blessing_of_East_Blue, Mandarin_Orange_Jelly,
        Red_nosed_great_adventure_Framboise_Mousse, Leblanc_Coffee_Set, Hotdog_Coffee_Set,
        Omelette_Sandwich_Coffee_Set, Deluxe_Curry, Coffee, Kurosaki_Curry_with_Side_Salad,
        Kon_Stuffed_Dog, Kirios_Reiatsu_Imbued_Feast, Denjis_Morning_After, Honey_Glazed_Pochita_Bites,
        Makimas_Devil_Curry_Udon, Hayakawa_Gyozas, Tomato_Bagel, Veggie_Sandwich, Mixed_Fruits_Sandwich,
        Pumpkin_Bagel, Salmon_Bagel, Apple_Smoothie, Peach_Smoothie, Coconut_Juice, Iced_Caffe_Latte,
        Totoro_Cupcake, Totoro_Hot_Chocolate, Cat_Bus_Eclair, Ponyo_Cheesecake, Soot_Vanilla_Tart,
        No_Face_Swiss_Roll, Jiji_Donut, Otori_sama_Macaron
    ])

    db.session.commit()

def undo_menus():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.menus RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM menus"))

    db.session.commit()

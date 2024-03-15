from app.models import db, User, environment, SCHEMA
from sqlalchemy.sql import text


# Adds a demo user, you can add other users here if you want
def seed_users():
    demo = User(
        username='Demo', first_name='Demo', last_name='Lition', email='demo@aa.io', password='password')
    marnie = User(
        username='marnie', first_name='Margie', last_name='Nie', email='marnie@aa.io', password='password')
    bobbie = User(
        username='bobbie', first_name='Bobby', last_name='Flay', email='bobbie@aa.io', password='password')
    Ryou = User(
        username='MoonChopperr', first_name='Ryou', last_name='Nishiyama', email='MoonChopper@aa.io', password='password')
    Tyler = User(
        username='TylerHan1226', first_name='Tyler', last_name='Han', email='TylerHan1226@aa.io', password='password')
    Jasmine = User(
        username='jtruong97', first_name='Jasmine', last_name='Truong', email='jtruong97@aa.io', password='password')
    Johnny = User(
        username='JohnnyHa1017', first_name='Johnny', last_name='Ha', email='JohnnyHa1017@aa.io', password='password')
    David = User(
        username='hisownspace', first_name='David', last_name='Nash', email='hisownspace@aa.io', password='password')
    Brad = User(
        username='bradsimpson123', first_name='Brad', last_name='Simpson', email='bradsimpson123@aa.io', password='password')
    Andrew = User(
        username='andrwtran', first_name='Andrew', last_name='Tran', email='andrwtran@aa.io', password='password')

    db.session.add_all([demo, marnie, bobbie, Ryou, Tyler, Jasmine, Johnny, David, Brad, Andrew])
    db.session.commit()


# Uses a raw SQL query to TRUNCATE or DELETE the users table. SQLAlchemy doesn't
# have a built in function to do this. With postgres in production TRUNCATE
# removes all the data from the table, and RESET IDENTITY resets the auto
# incrementing primary key, CASCADE deletes any dependent entities.  With
# sqlite3 in development you need to instead use DELETE to remove all data and
# it will reset the primary keys for you as well.
def undo_users():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.users RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM users"))

    db.session.commit()

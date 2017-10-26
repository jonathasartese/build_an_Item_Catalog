from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import User, Base, Category, CatalogItem

engine = create_engine('sqlite:///catalogitemsandusers.db')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()


# Create dummy user
User1 = User(name="Robo Barista", email="tinnyTim@udacity.com",
             picture='https://pbs.twimg.com/profile_images/2671170543/18debd694829ed78203a5a36dd364160_400x400.png')
session.add(User1)
session.commit()

# Categories and Items
category1 = Category(name="Soccer")
session.add(category1)
session.commit()

category2 = Category(name="Basketball")
session.add(category2)
session.commit()

category3 = Category(name="Baseball")
session.add(category3)
session.commit()

category4 = Category(name="Frisbee")
session.add(category4)
session.commit()

category5 = Category(name="Snowboarding")
session.add(category5)
session.commit()

category6 = Category(name="Rock Climbing")
session.add(category6)
session.commit()

category7 = Category(name="Foosball")
session.add(category7)
session.commit()

category8 = Category(name="Skating")
session.add(category8)
session.commit()

category9 = Category(name="Hockey")
session.add(category9)
session.commit()

print("added categories!")

# Category Items

catalogitem1 = CatalogItem(title="Soccer Cleats", category=category1, user=User1, 
                        description="Soccer Cleats")
session.add(catalogitem1)
session.commit()

catalogitem2 = CatalogItem(title="Jersey", category=category1, user=User1,
                        description="Jersey")
session.add(catalogitem2)
session.commit()

catalogitem3 = CatalogItem(title="Bat", category=category3, user=User1,
                        description="Bat")
session.add(catalogitem3)
session.commit()

catalogitem4 = CatalogItem(title="Frisbee", category=category4, user=User1,
                        description="Frisbee")
session.add(catalogitem4)
session.commit()

catalogitem5 = CatalogItem(title="Shinguards", category=category1, user=User1,
                        description="Shinguards")
session.add(catalogitem5)
session.commit()

catalogitem6 = CatalogItem(title="Two shinguards", category=category1, user=User1,
                        description="Two shinguards")
session.add(catalogitem6)
session.commit()

catalogitem7 = CatalogItem(title="Snowboards", category=category5, user=User1,
                        description="Snowboards")
session.add(catalogitem7)
session.commit()

catalogitem8 = CatalogItem(title="Goggles", category=category5, user=User1,
                        description="Goggles")
session.add(catalogitem8)
session.commit()

catalogitem9 = CatalogItem(title="Stick", category=category9, user=User1,
                        description="Stick")
session.add(catalogitem9)
session.commit()



print("added menu items!")

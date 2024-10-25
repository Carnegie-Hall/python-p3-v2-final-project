from boba import Boba
from tea import Tea

Boba.delete_all()
Tea.delete_all()

strawberry = Tea.create(name="Strawberry")
blueberry = Tea.create(name="Blueberry")
raspberry = Tea.create(name="Raspberry")

Boba.create(name="KiwiLimeLight", flavor="Green", tea_id=strawberry.id)
Boba.create(name="LovelyStarFruit", flavor="Sweet", tea_id=blueberry.id)
Boba.create(name="PurpleReign", flavor="Sour", tea_id=strawberry.id)
Boba.create(name="RedPeakTwin", flavor="Sweet", tea_id=raspberry.id)
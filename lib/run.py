import ipdb

from boba import Boba
from tea import Tea
from cli import Cli

# Boba.drop_table()
Boba.create_table()
# Boba(name="OrangeFantasy", flavor="Mango")
Tea.create_table()
# Tea.drop_table()
# Boba.find_by_id(100)
# ipdb.set_trace()

cli = Cli()
cli.start()


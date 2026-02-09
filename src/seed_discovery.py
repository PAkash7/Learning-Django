import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Learning_Djengo.settings")
django.setup()

from django.contrib.auth.models import User
from mars.models import Discovery

# Create a default user if one doesn't exist
if not User.objects.filter(username="MarsRover").exists():
    user = User.objects.create_superuser("MarsRover", "rover@mars.com", "password")
else:
    user = User.objects.get(username="MarsRover")

discoveries = [
    {
        "title": "Water Ice Found!",
        "content": "We have confirmed the presence of subsurface water ice in the Utopia Planitia region. This is a massive breakthrough for potential colonization efforts.",
        "author": user
    },
    {
        "title": "New Cave System",
        "content": "A network of lava tubes has been identified near Olympus Mons. These could provide excellent radiation shielding for future habitats.",
        "author": user
    },
    {
        "title": "Dust Storm Approaches",
        "content": "Sensors indicate a global dust storm is forming in the southern hemisphere. Solar power efficiency is expected to drop by 40%.",
        "author": user
    }
]

for item in discoveries:
    Discovery.objects.create(
        title=item["title"],
        content=item["content"],
        author=item["author"]
    )

print("Discovery database populated successfully!")

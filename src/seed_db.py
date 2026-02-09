import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Learning_Djengo.settings")
django.setup()

from mars.models import MarsStatus

data = [
    {
        "Human":"Not Found",
        "Water":"Searching",
        "Temperature":"Hot",
        "Moisture":"Unknown",
    },
    {
        "Human":"Dead",
        "Water":"Found",
        "Temperature":"Hot",
        "Moisture":"Available",
    }
]

for item in data:
    MarsStatus.objects.create(
        human_status=item["Human"],
        water_status=item["Water"],
        temperature=item["Temperature"],
        moisture_status=item["Moisture"]
    )

print("Database populated successfully via script!")

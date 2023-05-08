import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "dashboard.settings")
django.setup()


import json

from app.models import dataBase

with open('jsondata.json',encoding='utf-8') as f:
    data = json.load(f)
    
for item in data:
    report = dataBase(
        end_year=item['end_year'],
        intensity=item[str('intensity')],
        sector=item['sector'],
        topic=item['topic'],
        insight=item['insight'],
        url=item['url'],
        region=item['region'],
        start_year=item['start_year'],
        impact=item['impact'],
        added=item['added'],
        published=item['published'],
        country=item['country'],
        relevance=item[str('relevance')],
        pestle=item['pestle'],
        source=item['source'],
        title=item['title'],
        likelihood=item[str('likelihood')]
    )
    report.save()

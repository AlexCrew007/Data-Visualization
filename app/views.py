from django.shortcuts import render
from app.models import dataBase
from django.http import HttpResponse
from collections import defaultdict
from .forms import FilterForm
# Create your views here.

def first(request):

    form=FilterForm()
    data=dataBase.objects.all()

    end_year_filter=request.GET.get('end_year')
    topic_filter=request.GET.get('topic')
    sector_filter=request.GET.get('sector')
    region_filter=request.GET.get('region')
    source_filter=request.GET.get('source')
    country_filter=request.GET.get('country')
   
    if end_year_filter=="" or end_year_filter==None:
        pass
    else:
        data=data.filter(end_year=end_year_filter)
    if topic_filter=="" or topic_filter==None:
        pass
    else:
        data=data.filter(topic__icontains=topic_filter)
    if sector_filter=="" or sector_filter==None:
        pass
    else:
        data=data.filter(sector__icontains=sector_filter)
    if region_filter=="" or region_filter==None:
        pass
    else:
        data=data.filter(region__icontains=region_filter)
    if source_filter=="" or source_filter==None:
        pass
    else:
        data=data.filter(source__icontains=source_filter)
    if country_filter=="" or country_filter==None:
        pass
    else:
        data=data.filter(country__icontains=country_filter)

    data=data.values()
    country=defaultdict(lambda :0)
    dic=defaultdict(lambda :0)
    region=defaultdict(lambda :0)
    intensity=defaultdict(lambda :0)
    topic=defaultdict(lambda :set())

        
    for x in data:
        if x['region']=='':
            if x['topic']=='':
                pass
            else:
                topic[x['region']].add(x['topic'])
            if x['intensity']=='':
                intensity['Others']+=0
            else:
                intensity['Others']+=int(x['intensity'])
        elif x['region']!='':
            if x['topic']=='':
                pass
            else:
                topic[x['region']].add(x['topic'])
            if x['intensity']=='':
                intensity['Others']+=0
            else:
                intensity[x['region']]+=int(x['intensity'])
        if x['region']=='':
            if x['relevance']=='':
                region['Others']+=0
            else:
                region['Others']+=int(x['relevance'])
        elif x['region']!='':
            if x['relevance']=='':
                region['relevance']+=0
            else:
                region[x['region']]+=int(x['relevance'])
        if x['country']!='':
            country[x['country']]+=1
        elif x['country']=='':
            country['Others']+=1
        if x['intensity']=="":
            if x['country']=="":
                dic["Others"]+=0
            else:
                dic[x['country']]+=0
        elif x['intensity']!="":
            if x['country']=="":
                dic["Others"]+=int(x['intensity'])
            else:
                dic[x['country']]+=int(x['intensity'])
   
    topic_val=[]
    for x in topic:
        topic_val.append(len(topic[x]))
    region_=list(region.keys())
    relevance=list(region.values())
    intensity=list(intensity.values())
    context={
        'lst': list(dic.values()),
        'country':list(dic.keys()),
        'country_count':list(country.values()),
        'region':list(region.keys()),
        'relevance':list(region.values()),
        'topic_val':topic_val,
        'form':form,
    }
    return render(request,'main.html',context)

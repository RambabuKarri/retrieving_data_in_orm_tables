from django.shortcuts import render

# Create your views here.
from app.models import *
from django.db.models.functions import Length
from django.db.models import Q


def display_topic(request):
    topics=Topic.objects.all()
    d={'topics':topics}
    return render(request,'display_topic.html',d)

def display_webpage(request):
    webpages=Webpage.objects.all()

    webpages=Webpage.objects.filter(topic_name='Cricket')
    webpages=Webpage.objects.filter(topic_name='Volley Ball')
    webpages=Webpage.objects.exclude(topic_name='Volley Ball')
    webpages=Webpage.objects.all()[3::]
    webpages=Webpage.objects.all()[::-1]
    webpages=Webpage.objects.all().order_by('name')
    webpages=Webpage.objects.all().order_by('-name')
    webpages=Webpage.objects.all().order_by(Length('name'))
    webpages=Webpage.objects.all().order_by(Length('name').desc())

    webpages=Webpage.objects.all()
    webpages=Webpage.objects.filter(name__in=['rahul','Dhoni'])
    webpages=Webpage.objects.filter(name__regex='R\w+')
    webpages=Webpage.objects.all()
    webpages=Webpage.objects.filter(Q(name='Virat') | Q(url__startswith='http'))
    webpages=Webpage.objects.filter(Q(name='Rahul') & Q(url__startswith='http'))
    webpages=Webpage.objects.all()
    Webpage.objects.filter(name='Virat').update(url='http://vk.in')



    d={'webpages':webpages}
    return render(request,'display_webpage.html',d)

def display_accessrecord(request):
    access=AccessRecord.objects.all()
    access=AccessRecord.objects.filter(date='1979-07-07')
    access=AccessRecord.objects.filter(date__gt='1979-07-07')
    access=AccessRecord.objects.filter(date__lte='1979-07-07')
    access=AccessRecord.objects.filter(date__year='2023')
    access=AccessRecord.objects.filter(date__month='07')
    access=AccessRecord.objects.filter(date__day='12')
    access=AccessRecord.objects.filter(date__year__gte='2020')
    access=AccessRecord.objects.filter(date__year__lte='2020')
    access=AccessRecord.objects.filter(date__day__gt='10')
    access=AccessRecord.objects.all()

    d={'access':access}
    return render(request,'display_accessrecord.html',d)

def update_webpage(request):
    Webpage.objects.filter(name='Virat').update(url='http://vk.in')
    #Webpage.objects.filter(name='Dhoni').update(url='https://MSD.in')
    #Webpage.objects.filter(topic_name='Cricket').update(url='https://IndianTeam.in')
    #Webpage.objects.filter(name='Dhoni MSD').update(url='https://MSD.in')
    #Webpage.objects.filter(name='Dhoni').update(topic_name='BCCI Cricket')
    #Webpage.objects.filter(name='Dhoni').update(topic_name='Rugby')
    #Webpage.objects.update_or_create(name='Abc',defaults={'url':'http://ABCDE.com'})
    #Webpage.objects.update_or_create(topic_name='Rugby',defaults={'url':'http://Rugby.com'})
    #Webpage.objects.update_or_create(name='Abc',defaults={'url':'http://ABCDE.com'})
    #CTO=Topic.objects.get(topic_name='Cricket')
    #Webpage.objects.update_or_create(name='Dhoni',defaults={'topic_name':CTO})
    

    webpages=Webpage.objects.all()
    d={'webpages':webpages}
    return render(request,'display_webpage.html',d)


def delete_webpage(request):
    Webpage.objects.filter(name='Rahul').delete()
    #Webpage.objects.all().delete()
    webpages=Webpage.objects.all()
    d={'webpages':webpages}
    return render(request,'display_webpage.html',d)







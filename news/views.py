from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404
import datetime as dt
from .models import Article
# Create your views here.
def welcome(request):

  return render(request,'welcome.html')
def news_today(request):
  date = dt.date.today()
  news = Article.todays_news()
  # day = convert_dates(date)
  # # function converting a date object into the exact day
  # html = f'''
  # <html>
  #   <body>
  #     <h1>News for {day}  {date.day}-{date.month}-{date.year}</h1>
  #   </body>
  # </html>
  # '''
  return render(request,'all-news/today-news.html',{'date':date,'news':news})
def convert_dates(dates):
  # function to get weekday number from the date.
  day_number = dt.date.weekday(dates)
  days =['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
  day= days[day_number]
  return day
def past_days_news(request,past_date):
  try:
    date = dt.datetime.strptime(past_date,'%Y-%m-%d').date()
  except ValueError:
    raise Http404()
    assert False
  if date == dt.date.today():
    return redirect(news_today)
    news = Article.days_news(date)
  return render(request,'all-news/past-news.html',{'date':date})
def search_results(request):
  if 'article' in request.GET and request and request.GET['article']:
    search_term = request.GET.get('article')
    searched_articles = Article.search_by_title(search_term)
    message= f'{search_term}'
    return render(request,'all-news/search.html',{'message':message,'articles':searched_articles})
  else:
    
    message = "You haven't search for any term"
    return render(request,'all-news/search.html',{"message":message})
def article(request,article_id):
  try:
    article = Article.objects.get(id = article_id)
  except DoesNotExist:
    raise Http404()
  return render (request,'all-news/article.html',{'article':article })
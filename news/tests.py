from django.test import TestCase
import datetime as dt

# from django.test import TestCase
from .models import Editor,Article,tags
class EditorTestClass(TestCase):

  def setUp(self):
    self.terry= Editor(first_name ="Kimberly", last_name = "Kardashian", email = "kimkay@gmail.com")
  def test_instance(self):

    self.assertTrue(isinstance(self.terry,Editor))
      # Editor.objects.create(first_name = 'Kimberly',last_name = 'Kardashian',email='kimkay@gmail.com')
  def test_save_method(self):
    self.terry.save_editor()
    editors = Editor.objects.all()
    self.assertTrue(len(editors)>0)
class ArticleTestClass(TestCase):
  def setUp(self):
    self.james = Editor(first_name ="Kimberly", last_name = "Kardashian", email = "kimkay@gmail.com")
    self.james.save_editor()
    self.new_tag= tags(name='testing')
    self.new_tag.save()
    self.new_article=Article(title='Test Article',post='This is a random test Post',editor=self.james)
    self.new_article.save()
    self.new_article.tags.add(self.new_tag)
  def tearDown(self):
    Editor.objects.all().delete()
    tags.objects.all().delete()
    Article.objects.all().delete()
  def test_get_news_today(self):
    today_news = Article.todays_news()
    self.assertTrue(len(today_news)>0)

    
  def test_get_news_by_date(self):


    test_date = '2017-03-17'
    date = dt.datetime.strptime(test_date, '%Y-%m-%d').date()
    news_by_date = Article.days_news(date)
    self.assertTrue(len(news_by_date) == 0)

  
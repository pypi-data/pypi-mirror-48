import datetime
import unittest
from django.test import TestCase
from django.utils import timezone
from django.urls import reverse
from django.urls import resolve
from polls.models import Question, Choice
from django.test import Client
from model_mommy import mommy
from model_mommy.recipe import Recipe, foreign_key
from mock import Mock, patch, PropertyMock


###########################################################################
###########################################################################
###########################################################################


class QuestionMethodTests(TestCase):

    def test_was_published_recently_with_future_question(self):
        time = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(pub_date=time)
        self.assertIs(future_question.was_published_recently(), False)

    def test_was_published_recently_with_old_question(self):
        time = timezone.now() - datetime.timedelta(days=30)
        old_question = Question(pub_date=time)
        self.assertIs(old_question.was_published_recently(), False)

    def test_was_published_recently_with_recent_question(self):
        time = timezone.now() - datetime.timedelta(hours=1)
        recent_question = Question(pub_date=time)
        self.assertIs(recent_question.was_published_recently(), True)

###########################################################################
###########################################################################
###########################################################################


def create_question(question_text, days):
    time = timezone.now() + datetime.timedelta(days=days)
    return Question.objects.create(question_text=question_text, pub_date=time)


###########################################################################
###########################################################################
###########################################################################

class QuestionIndexDetailTest(TestCase):
    def test_detail_view_with_a_future_question(self):

        future_question = create_question(question_text='Future questions.', days=5)
        url = reverse('polls:detail', args=(future_question.id,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

    def test_detail_view_with_a_past_question(self):
        
        past_question = create_question(question_text='Past questions.', days=-5)
        url = reverse('polls:detail', args=(past_question.id,))
        response = self.client.get(url)
        self.assertContains(response, past_question.question_text)

###########################################################################
###########################################################################
###########################################################################


class QuestionIndexViewTests(TestCase):
    def test_no_questions(self):
        
        response = self.client.get(reverse('polls:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No polls are available.")
        self.assertQuerysetEqual(response.context['latest_question_list'], [])

    def test_past_question(self):
       
        create_question(question_text="Past question.", days=-30)
        response = self.client.get(reverse('polls:index'))
        self.assertQuerysetEqual(
            response.context['latest_question_list'],
            ['<Question: Past question.>']
        )

    def test_two_past_questions(self):
        
        create_question(question_text="Past question 1.", days=-30)
        create_question(question_text="Past question 2.", days=-5)
        response = self.client.get(reverse('polls:index'))
        self.assertQuerysetEqual(
            response.context['latest_question_list'],
            ['<Question: Past question 2.>', '<Question: Past question 1.>']
        )


###########################################################################
###########################################################################
###########################################################################

class ChoiceMethodTest(TestCase):

    def test_vadilate_choice_instance(self):        
        qObj = Choice()        
        self.assertIsInstance(qObj,Choice)
        self.assertEqual(qObj.__str__(),"choice_object_instance")


###########################################################################
###########################################################################
###########################################################################


class VoteTest(TestCase):

    def test_voting_404(self):
        vote_question_404 = create_question(question_text='Vote for this.', days=-2)

        #vote_question_404.choice_set.create(choice_text = 'Testing', votes=0)
        client = Client()
        # Perform a vote on the poll by mocking a POST request.
        response = client.post('/polls/11000/vote/', {'choice':1,}, follow = False)
        self.assertEqual(response.status_code, 404)

    def test_choice_not_exists(self):
        create_question(question_text='Vote for this choice.', days=-2)
        
        client = Client()
        # Perform a vote on the poll by mocking a POST request.
        response = client.post('/polls/1/vote/', {'choice':11000,})
        # import pdb; pdb.set_trace()
        self.assertEqual(response.status_code, 200)
        
    def test_voting_302(self):
        vote_question_302 = create_question(question_text='Vote for this.', days=-2)

        vote_question_302.choice_set.create(choice_text='Testing', votes=0)

        client = Client()
        response = client.post('/polls/1/vote/', {'choice': '1',})
        #import pdb; pdb.set_trace()
        self.assertEqual(response.status_code, 302)
        choice = Choice.objects.get(pk=1)
        self.assertEqual(choice.votes, 1)

###########################################################################
###########################################################################
###########################################################################


# class Test_Questions_Date(TestCase):
#     def mock_question(self):
       
#         return Mock(
#             question_text='Test',
#             pub_date=(timezone.now() + datetime.timedelta(days=days)),
#         )

#     def test_was_published_recently_with_future_question(self):
#         time = timezone.now() + datetime.timedelta(days=30)
#         future_question = Question(pub_date=time)
#         self.assertIs(future_question.was_published_recently(), False)

#     def test_was_published_recently_with_old_question(self):
#         time = timezone.now() - datetime.timedelta(days=30)
#         old_question = Question(pub_date=time)
#         self.assertIs(old_question.was_published_recently(), False)

#     def test_was_published_recently_with_recent_question(self):
#         time = timezone.now() - datetime.timedelta(hours=1)
#         recent_question = Question(pub_date=time)
#         self.assertIs(recent_question.was_published_recently(), True)



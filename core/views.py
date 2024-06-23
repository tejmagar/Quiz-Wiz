import json

from django.shortcuts import render

from .models import Question

# Create your views here.


def prepare_questions(questions):
    items = []
    for question in questions:
        data = {
            'question': question.question,
            'options': [],
            'correctAnswer': str(question.correct_option)
        }

        answers = []
        for (index, answer) in enumerate(question.answers.split(",")):
            item = {
                'id': str(index + 1),
                'text': answer.strip()
            }

            answers.append(item)

            data['options'] = answers

        items.append(data)

    return items


def home(request):
    easy_questions = prepare_questions(
        Question.objects.filter(category='easy').all())
    medium_questions = prepare_questions(
        Question.objects.filter(category='medium').all()
    )
    hard_questions = prepare_questions(
        Question.objects.filter(category='hard').all()
    )

    quiz_ctx = {
        'easy': easy_questions,
        'medium': medium_questions,
        'hard': hard_questions
    }

    context = {
        'quiz_ctx': json.dumps(quiz_ctx)
    }

    return render(request, 'index.html', context)

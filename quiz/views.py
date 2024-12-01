from django.shortcuts import render, redirect
from .models import Question
import random

def dashboard(request):

    #uaing session to save the result
    session_results = request.session.get('quiz_results', {
        'total_attempts': 0,
        'correct_answers': 0
    })
    
    total_attempts = session_results['total_attempts']
    correct_answers = session_results['correct_answers']

    #error handeling as attempts initially is 0
    try:
        percentage = (correct_answers / total_attempts * 100)
    except ZeroDivisionError:
        percentage = 0
    
    context = {
        'total_attempts': total_attempts,
        'correct_answers': correct_answers,
        'percentage': round(percentage, 2)
    }
    return render(request, 'quiz/dashboard.html', context)

def quiz(request):
    total_questions = Question.objects.count()
    
    if request.method == 'POST':
        question_id = request.POST.get('question_id')
        selected_answer = request.POST.get('answer')
        
        question = Question.objects.get(id=question_id)
        is_correct = selected_answer == question.correct_answer
        
        session_results = request.session.get('quiz_results', {
            'total_attempts': 0,
            'correct_answers': 0
        })
        session_results['total_attempts'] += 1
        if is_correct:
            session_results['correct_answers'] += 1
        request.session['quiz_results'] = session_results
        
        attempted_ids = request.session.get('attempted_questions', [])
        remaining_questions = total_questions - len(attempted_ids)
        
        context = {
            'question': question,
            'selected_answer': selected_answer,
            'is_correct': is_correct,
            'correct_answer': question.correct_answer,
            'is_last_question': remaining_questions <= 0
        }
        return render(request, 'quiz/result.html', context)
    
    attempted_ids = request.session.get('attempted_questions', [])
    if not attempted_ids or len(attempted_ids) >= total_questions:
        request.session['attempted_questions'] = []
        request.session['quiz_results'] = {
            'total_attempts': 0,
            'correct_answers': 0
        }
        attempted_ids = []
    
    available_questions = list(Question.objects.exclude(id__in=attempted_ids))
    
    if not available_questions:
        return redirect('dashboard')
    
    question = random.choice(available_questions)
    
    attempted_ids = request.session['attempted_questions']
    attempted_ids.append(question.id)
    request.session['attempted_questions'] = attempted_ids
    request.session.modified = True
    
    remaining_questions = total_questions - len(attempted_ids)
    
    context = {
        'question': question,
        'is_last_question': remaining_questions <= 0,
        'questions_remaining': remaining_questions
    }
    
    return render(request, 'quiz/quiz.html', context)

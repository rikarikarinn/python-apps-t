from django.shortcuts import render, get_object_or_404, redirect
from .models import Question, Choice
from .forms import SignUpForm
from django.contrib.auth import login

# 投票一覧ページ
def index(request):
    # 公開済みかつ非表示でない質問のみ表示
    latest_question_list = Question.objects.filter(is_active=True).order_by('-pub_date')[:5]
    return render(request, 'polls/index.html', {'latest_question_list': latest_question_list})

# 投票詳細ページ
def detail(request, question_id):
    # 非表示の質問は404
    question = get_object_or_404(Question, pk=question_id, is_active=True)
    return render(request, 'polls/detail.html', {'question': question})

# 投票処理
def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id, is_active=True)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "選択肢を選んでください。",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return redirect('polls:results', question_id=question.id)

# 投票結果ページ
def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id, is_active=True)
    total_votes = sum(c.votes for c in question.choice_set.all())

    choices = []
    for choice in question.choice_set.all():
        ratio = (choice.votes / total_votes * 100) if total_votes > 0 else 0
        choices.append({
            "text": choice.choice_text,
            "votes": choice.votes,
            "ratio": round(ratio, 1),
        })

    context = {
        "question": question,
        "choices": choices,
        "total_votes": total_votes,
    }
    return render(request, 'polls/results.html', context)

# サインアップページ
def signup(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('polls:index')
    else:
        form = SignUpForm()
    return render(request, 'polls/signup.html', {'form': form})

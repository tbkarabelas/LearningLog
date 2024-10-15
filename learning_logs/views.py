"""End of project ideas, add streak for when you have a streak for your logs
    showing your progress through out the course, log what you learned and imporveed that day

"""

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Topic, Entry
from .forms import TopicForm, EntryForm

def index(request):
    return render(request, 'learning_logs/index.html')
@login_required
def topics(request):
    topics = Topic.objects.order_by('date_added')
    context = {'topics': topics}
    return render(request, 'learning_logs/topics.html', context)

@login_required
def topic(request,topic_id):
    topic = Topic.objects.get(id=topic_id)
    entries = topic.entry_set.order_by
    context = {'topic': topic, 'entries': entries}
    return render(request, 'learning_logs/topic.html', context)
@login_required
def new_topic(request):
    """Add new tpoic"""
    if request.method != 'POST':
        # no data create blank field
        form = TopicForm()

    else:
        form  = TopicForm(data=request.POST)
        if form.isvalid():
            form.save()
            return redirect('learning_logs:topics')
        
    context = {'form': form}
    return render(request, 'learning_logs/new_topic.html', context)

@login_required
def new_entry(request, topic_id):
    """Add a new entry for a topic"""
    topic = Topic.objects.get(id=topic_id)

    if request.method != 'POST':
        # no data submitted; create a blank form
        form = EntryForm()
    else:
        # POST data submiteed; create a blank form
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            new_entry.save()
            return redirect('learning_logs:topic', topic_id=topic_id)
    
    context = {'topic': topic, 'form': form}
    return render(request, 'learning_logs/new_entry.html', context)
@login_required
def edit_entry(request, entry_id):
    """edit an existing entry"""
    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic

    if request.method != 'POST':
        # pre-fill with exisitng entry
        form = EntryForm(instance=entry)
    else:
        # POST data submitted; process data
        form = EntryForm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('learning_logs:topic', topic_id=topic.id)
    
    context = {'entry': entry, 'topic': topic, 'form': form}
    return render(request, 'learning_logs/edit_entry.html', context)
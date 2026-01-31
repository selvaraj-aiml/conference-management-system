from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import ConferenceSession, PaperPresentation, Paper

def is_admin(user):
    return user.is_authenticated and user.role == 'admin'

@login_required
@user_passes_test(is_admin)
def admin_session_list(request):
    sessions = ConferenceSession.objects.order_by('date', 'start_time')
    return render(request, 'admin/sessions/list.html', {'sessions': sessions})

@login_required
@user_passes_test(is_admin)
def admin_session_create(request):
    if request.method == 'POST':
        ConferenceSession.objects.create(
            title=request.POST['title'],
            session_type=request.POST['session_type'],
            date=request.POST['date'],
            start_time=request.POST['start_time'],
            end_time=request.POST['end_time'],
            hall=request.POST.get('hall', ''),
            speaker=request.POST.get('speaker', '')
        )
        messages.success(request, "Session created successfully!")
        return redirect('admin_session_list')

    return render(request, 'admin/sessions/create.html')

@login_required
@user_passes_test(is_admin)
def admin_session_edit(request, session_id):
    session = get_object_or_404(ConferenceSession, id=session_id)

    if request.method == 'POST':
        session.title = request.POST['title']
        session.session_type = request.POST['session_type']
        session.date = request.POST['date']
        session.start_time = request.POST['start_time']
        session.end_time = request.POST['end_time']
        session.hall = request.POST.get('hall', '')
        session.speaker = request.POST.get('speaker', '')
        session.save()
        messages.success(request, "Session updated successfully!")
        return redirect('admin_session_list')

    return render(request, 'admin/sessions/edit.html', {'session': session})
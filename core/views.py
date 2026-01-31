from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from core.models import Paper, Profile, ReviewAssignment, ConferenceSession, PaperPresentation
from users.models import User

@login_required
def admin_dashboard(request):
    if request.user.role != 'admin':
        return redirect(request.user.get_dashboard_url())

    stats = {
        'total_authors': Profile.objects.filter(role='author').count(),
        'total_reviewers': Profile.objects.filter(role='reviewer').count(),
        'total_participants': Profile.objects.filter(role='participant').count(),
        'total_papers': Paper.objects.count(),
        'pending_reviews': Paper.objects.filter(status='under_review').count(),
    }

    papers = Paper.objects.all().order_by('-created_at')

    if request.method == 'POST' and 'assign_reviewer' in request.POST:
        paper_id = request.POST.get('paper_id')
        reviewer_id = request.POST.get('reviewer_id')

        try:
            paper = Paper.objects.get(id=paper_id)
            reviewer = User.objects.get(id=reviewer_id, role='reviewer')
            paper.reviewer = reviewer
            paper.status = 'assigned'
            paper.save()
            messages.success(request, f"Paper '{paper.title}' assigned to {reviewer.username}")
        except Exception as e:
            messages.error(request, f"Assignment failed: {str(e)}")

        return redirect('admin_dashboard')

    reviewers = User.objects.filter(role='reviewer')

    return render(request, "dashboards/admin_dashboard.html", {
        'stats': stats,
        'papers': papers,
        'reviewers': reviewers,
    })

@login_required
def author_dashboard(request):
    if request.user.role != 'author':
        return redirect(request.user.get_dashboard_url())

    papers = Paper.objects.filter(author=request.user).order_by('-created_at')

    return render(request, "dashboards/author_dashboard.html", {
        'papers': papers,
    })

@login_required
def reviewer_dashboard(request):
    if request.user.role != 'reviewer':
        messages.error(request, "Only reviewers can access this dashboard.")
        return redirect(request.user.get_dashboard_url())

    assigned_papers = Paper.objects.filter(reviewer=request.user).order_by('-created_at')

    return render(request, "dashboards/reviewer_dashboard.html", {
        'assigned_papers': assigned_papers,
    })

@login_required
def participant_dashboard(request):
    if request.user.role != 'participant':
        return redirect(request.user.get_dashboard_url())

    sessions = ConferenceSession.objects.order_by('date', 'start_time')

    return render(request, "dashboards/participant_dashboard.html", {
        'sessions': sessions,
    })

def is_admin(user):
    return user.is_authenticated and user.role == 'admin'

@user_passes_test(is_admin)
def manage_users(request):
    users = User.objects.all().order_by('-date_joined')

    context = {
        'users': users,
        'total_admins': users.filter(role='admin').count(),
        'total_authors': users.filter(role='author').count(),
        'total_reviewers': users.filter(role='reviewer').count(),
        'total_participants': users.filter(role='participant').count(),
    }

    return render(request, 'admin/manage_users.html', context)

@user_passes_test(is_admin)
def update_user(request, user_id):
    user = User.objects.get(id=user_id)

    if request.method == "POST":
        new_role = request.POST.get("role")
        new_status = request.POST.get("status")

        if new_role and new_role in dict(User.ROLE_CHOICES):
            user.role = new_role

        if new_status == "active":
            user.is_active = True
        elif new_status == "inactive":
            user.is_active = False

        user.save()
        messages.success(request, f"User {user.username} updated successfully!")

    return redirect("manage_users")

@login_required
def review_paper(request, paper_id):
    paper = get_object_or_404(Paper, id=paper_id, reviewer=request.user)

    if request.method == "POST":
        decision = request.POST.get("decision")
        comments = request.POST.get("review_comments")

        if decision in ['accepted', 'rejected']:
            paper.status = decision
        paper.review_comment = comments
        paper.save()

        messages.success(request, "Review submitted successfully!")
        return redirect("reviewer_dashboard")

    return render(request, "dashboards/review_form.html", {
        "paper": paper,
    })

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

@login_required
@user_passes_test(is_admin)
def admin_assign_paper_to_session(request, paper_id):
    paper = get_object_or_404(Paper, id=paper_id)

    if paper.status != 'accepted':
        messages.error(request, "Only accepted papers can be assigned to a session.")
        return redirect('admin_dashboard')

    if request.method == 'POST':
        session_id = request.POST.get('session_id')
        order = request.POST.get('presentation_order', 1)

        try:
            session = ConferenceSession.objects.get(id=session_id)
            
            if PaperPresentation.objects.filter(paper=paper).exists():
                messages.error(request, "This paper is already assigned to a session.")
            else:
                PaperPresentation.objects.create(
                    paper=paper,
                    session=session,
                    presentation_order=order
                )
                paper.status = 'scheduled'
                paper.save()
                messages.success(request, f"Paper '{paper.title}' assigned to {session.title} at position {order}")
        except Exception as e:
            messages.error(request, f"Assignment failed: {str(e)}")

        return redirect('admin_dashboard')

    sessions = ConferenceSession.objects.order_by('date', 'start_time')

    return render(request, 'admin/assign_paper_to_session.html', {
        'paper': paper,
        'sessions': sessions,
    })
from . import views
from django.urls import path
from django.contrib import admin


urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout_view"),
    path("register", views.register, name="register"),
    path("profile", views.profile, name="profile"),
    path("search_jobs", views.search_jobs, name="search_jobs"),
    path("post_job", views.post_job, name="post_job"),
    path("edit_profile", views.edit_profile, name="edit_profile"),
    path("job_detail/<int:job_id>", views.job_detail, name="job_detail"),
    path("step1/<int:job_id>", views.step1, name="step1"),
    path("step2/<int:job_id>", views.step2, name="step2"),
    path("confirm_application/<int:job_id>", views.confirm_application, name="confirm_application"),
    path("remove_application/<int:application_id>", views.remove_application, name="remove_application"),
    path("send_message/<int:receiver_id>", views.send_message, name="send_message"),
    path("saved_jobs", views.saved_jobs, name="saved_jobs"),
    path("save_job", views.save_job, name="save_job"),
    path("delete_job/<int:job_id>", views.delete_job, name="delete_job"),
    path("candidates/<int:job_id>", views.candidates, name="candidates"),
    path("inbox", views.inbox, name="inbox"),
    path("delete_message/<int:message_id>", views.delete_message, name="delete_message"),
]

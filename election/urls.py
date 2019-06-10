from django.urls import path, reverse

from election.views import *

app_name = 'election'

urlpatterns = [
    path(r'', ElectionCreateAPIView.as_view(), name="create"),
    path(r'get/<str:pk>/', ElectionDetailsAPIView.as_view(), name="details"),
    path(r'vote/', VoteAPIView.as_view(), name="vote"),
]

def new_election():
    return reverse("election:create")

def election_details(election_pk):
    return reverse("election:details", args=(election_pk,))

def vote():
    return reverse("election:vote")

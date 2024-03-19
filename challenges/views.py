from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string
# Create your views here.

monthly_releases = {
    "january": ["Attack on Titan Final Season Part 2", "Komi Can't Communicate"],
    "february": ["Demon Slayer: Kimetsu no Yaiba Entertainment District Arc", "The Case Study of Vanitas Part 2"],
    "march": ["JoJo's Bizarre Adventure Part 6: Stone Ocean", "The Rising of the Shield Hero Season 2"],
    "april": ["My Hero Academia Season 6", "Tokyo Revengers Part 2"],
    "may": ["One Piece: Romance Dawn", "Edens Zero"],
    "june": ["Jujutsu Kaisen 0 (Movie)", "To Your Eternity Season 2"],
    "july": ["The World's Finest Assassin Gets Reincarnated in Another World as an Aristocrat", "The Duke of Death and His Maid"],
    "august": ["Re:Zero - Starting Life in Another World Season 3", "That Time I Got Reincarnated as a Slime Season 3"],
    "september": ["Bleach: Thousand-Year Blood War Arc", "Banished from the Heroes' Party"],
    "october": ["Black Clover: Quartet Knights", "Platinum End"],
    "november": ["Dragon Ball Super: Super Hero (Movie)", "Mushoku Tensei: Jobless Reincarnation Season 2"],
    "december": ["Sword Art Online Progressive: Aria of a Starless Night", "The Faraway Paladin"]
}


def month_challenges_by_numbers(request, month):
    months = list(monthly_releases.keys())
    if month > len(months):
        return HttpResponseNotFound("Not Supported")

    forward_month = months[month-1]
    redirect_url = reverse('release-month', args=[forward_month])
    return HttpResponseRedirect(redirect_url)


def month_challenges(request, month):
    try:
        content = monthly_releases[month]
        html_string = render_to_string('challenges/challenge.html')
        return HttpResponse(html_string)
    except KeyError:
        return HttpResponseNotFound("Mentioned release is not available")


def index(request):
    months = list(monthly_releases.keys())
    html = '<h4><ul>'
    for month in months:
        month_path = reverse("release-month", args=[month])
        html += f"<li><a href=\"{month_path}\">{month.capitalize()}</a></li>"
        
    html += '</ul></h4>'
    return HttpResponse(html)

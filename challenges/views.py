from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect

# STATIC ROUTES


# def jan_index(request):
#     return HttpResponse('January - Eat no meat for the rest of the month')


# def feb_index(request):
#     return HttpResponse('February - Wlak at least 20 min every day of this week')


# def march_index(request):
#     return HttpResponse('March - Learn Django every day till the end of the course')

# DYNAMIC ROUTES


monthly_challenges = {
    "january": "january -Eat no meat for the rest of the month",
    "february": "february - Wlak at least 20 min every day of this week",
    "march": "march - Learn Django every day till the end of the course",
    "april": "april - Eat no meat for the rest of the month",
    "may": "may - Learn Django every day till the end of the course",
    "june": "june - Wlak at least 20 min every day of this week",
    "july": "july - Eat no meat for the rest of the month",
    "august": "august - Learn Django every day till the end of the course",
    "september": "september - Eat no meat for the rest of the month",
    "october": "october - Learn Django every day till the end of the course",
    "november": "november - Wlak at least 20 min every day of this week",
    "december": "december - Learn Django every day till the end of the course",
}


def index(request):
    list_items = ""
    months = list(monthly_challenges.keys())

    for month in months:
        list_items = list_items + \
            f'<li><a href="{month}">{month.capitalize()}<a/></li>'

    response = f"<ul>{list_items}</ul>"
    return HttpResponse(response)


def monthly_challenge(request, cur_month):
    try:
        month_challenge = monthly_challenges[cur_month]
        month = cur_month.capitalize()
        return render(request, 'challenges/single_challenge.html', {"text": month_challenge, "title": month})
    except:
        return HttpResponseNotFound('<h1>Month is not supported</h1>')


def index_monthly_challenge(request, cur_month):
    # This is a way to create a real "List" from dict_keys that create after the key() method
    try:
        months = list(monthly_challenges.keys())
        month = months[cur_month - 1]
        return HttpResponseRedirect(month)
    except:
        return HttpResponseNotFound('<h1>Month is not supported</h1>')

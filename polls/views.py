# from django.shortcuts import render
# from django.http import HttpResponse, JsonResponse

from django.http import JsonResponse

# def index(request):
#     latest_question_list = Type.objects.all()[:1]
#     # for q in latest_question_list
#     #     output[] = q; 
#     # output = ', '.join([q.title for q in latest_question_list])
#     output = latest_question_list
#     return HttpResponse(output)

# -------------- Pass data set to provided view without shortcut

def listing(request):
    # latest_question_list = Listing.objects.all()[:5]
    # template = loader.get_template('polls/index.html')
    host_url = "localhost:3000"
    propertyObj = {
        "0" : {
            'id' : 1,
            'purposeDetail' : {
                'id' : 1,
                'title' : "for sale",
                'url' : "for-sale",
            },
            'typeDetail' : {
                'id' : 4,
                'title' : "apartment",
                'url' : "apartment",
            },
            'bed' : 3,
            'bath' : 2,
            'price' : 1200000,
            'areaCovered' : 1200,
            'areaLand' : 1500,
            'title' : "Awesome apartment in dubai marina",
            'description' : "Awesome apartment in dubai marina that you can count on",
            'url' : {
                '0' : "/for-sale/apartment/dubai/dubai-marina/Awesome_apartment_in_dubai_marina-1" 
            },
            'userdetail' : {
                'name' : "Omer waleed",
                'email' : "omer24waleed@gmail.com",
                'phone' : "+923228473603"
            },
            'locationdetail' : {
                'locId' : 4,
                'locationTitle' : "Dubai Marina",
                'locIds' : "1;4",
            }
        },
        "1" : {
            'id' : 1,
            'purposeDetail' : {
                'id' : 1,
                'title' : "for sale",
                'url' : "for-sale",
            },
            'typeDetail' : {
                'id' : 4,
                'title' : "apartment",
                'url' : "apartment",
            },
            'bed' : 3,
            'bath' : 2,
            'price' : 1200000,
            'areaCovered' : 1200,
            'areaLand' : 1500,
            'title' : "Awesome apartment in dubai marina",
            'description' : "Awesome apartment in dubai marina that you can count on",
            'url' : {
                '0' : "/for-sale/apartment/dubai/dubai-marina/Awesome_apartment_in_dubai_marina-1" 
            },
            'userdetail' : {
                'name' : "Omer waleed",
                'email' : "omer24waleed@gmail.com",
                'phone' : "+923228473603"
            },
            'locationdetail' : {
                'locId' : 4,
                'locationTitle' : "Dubai Marina",
                'locIds' : "1;4",
            }
        },
    }
    context = {
        'listing' : propertyObj,
        'lising_count' : 2,
    }
    return JsonResponse(context)


# -------------- PAss data set to provided view with shortcut

# def index(request):
#     latest_question_list = Question.objects.order_by('-pub_date')[:5]
#     context = {
#         'latest_question_list': latest_question_list,
#     }
#     return render(request, 'polls/index.html', context)

def breadcrumb(request):
    host_url = "localhost:3000"
    locationObj = {
        'breadcrumb' : {
            'locId' : 4,
            'locationTitle' : "dubai marina",
            'locIds' : "1;4",
            'level' : 2,
            'breadcrumbTitle' : "apartment for sale in dubai marina",
            'locBreadcrumb' : {
                0 : {
                    "id" : 1,
                    "title" : "dubai",
                    "key" : "dubai",
                    'breadcrumbTitle' : "apartment for sale in dubai",
                    "url" : "/for-sale/apartment/dubai/"
                },
                1 : {
                    "id" : 4,
                    "title" : "dubai marina",
                    "key" : "dubai/dubai-marina",
                    'breadcrumbTitle' : "apartment for sale in dubai marina",
                    "url" : "/for-sale/house/dubai/dubai-marina/"
                }
            },
        },
    }
    context = {
        'breadcrumb' : locationObj,
    }
    return JsonResponse(context)

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)

# Create your views here.
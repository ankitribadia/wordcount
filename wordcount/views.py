from django.http import HttpResponse
from django.shortcuts import render
import operator


def homepage(request):
    return render(request, 'home.html')

def eggs(request):
    return HttpResponse("Eggs are great")

def count(request):
    fulltext = request.GET['fulltext']
    word_list = fulltext.split()
    word_dict = {}
    for word in word_list:
        if word in word_dict:
            word_dict[word] +=1
        else:
            word_dict[word] = 1
    
    sorted_words = sorted(word_dict.items(), key=operator.itemgetter(1),reverse=True)
    # sorted_dict = sorted(word_dict, key=word_dict.get, reverse=True)
    return render(request, 'count.html',{'input_text': fulltext,'counter':len(word_list), 'word_dict': sorted_words})
    # "{% url 'count' %} "
    
def about(request):
    return render(request, 'about.html')
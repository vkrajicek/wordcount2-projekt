from django.http import HttpResponse
#    return HttpResponse(' Nazdar vole toto je Oneeeeee')

from django.shortcuts import render
import operator

def homepage(request):
    return render(request, 'homepage.html')

def one(request):
    return render(request, 'one.html')

def count(request):
    fulltext = request.GET['fulltextarea']
    #print(fulltext) toto by islo do konzoli
    word_list = fulltext.split()
    word_count_dict = {}
    for word in word_list:
        if word in word_count_dict:
            word_count_dict[word]+=1
        else:
            word_count_dict[word]=1
    words_sorted = sorted(word_count_dict.items(), key=operator.itemgetter(1), reverse=True)

    return render(request, 'count.html', {'fulltext':fulltext, 'count':len(word_list), 'sorted_words': words_sorted})

def about(request):
    return render(request, 'about.html')

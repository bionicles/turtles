from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'ninjas/index.html')

def ninjas(request):
    return render(request, 'ninjas/ninjas.html')

def color(request, color):
    color = color.lower()
    accepted_colors = ['blue', 'orange', 'red', 'purple']
    if color not in accepted_colors:
        return render(request, 'ninjas/meagan.html')
    img_link = "ninjas/images/{}.jpg".format(color)
    # source_string = "ninjas/images/" + color + ".jpg"
    # print source_string
    # img_html_code = "<img src '{% static " + source_string + "%}' alt=" +
    context = {'color': color, "img_link": img_link}
    return render(request, 'ninjas/color.html', context)

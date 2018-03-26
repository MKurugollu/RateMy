from django.http import HttpResponse
from ratemy.models import Category, Post, UserProfile


from django.contrib.auth.decorators import login_required

@login_required
def follow_category(request):
    cat_id = None
    if request.method == 'GET':
        cat_id = request.GET['category_id']
    followers = 0
    if cat_id:
        cat = Category.objects.get(id=int(cat_id))
        if cat:
            followers = cat.followers + 1
            cat.followers = followers
            cat.save()
    return HttpResponse(followers)





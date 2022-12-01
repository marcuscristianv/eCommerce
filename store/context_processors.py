from .models import Category

# return all the categories
def categories(request):
    return {
        'categories': Category.objects.all()
    }
from .models import Category, category

def get_all_categories(request):
    categories = Category.objects.all()
    context = {
        "categories": categories,
    }
    return context
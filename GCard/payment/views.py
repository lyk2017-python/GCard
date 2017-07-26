from django
class card(generic.ListView):
    model = Card
class pDetail(generic.DetailView):
    def get_queryset(self):
        return Product.objects.all()
class hView(generic.ListView):
    def get_queryset(self):
        return Product.objects.all()
class balance(generic.DetailView):
    model = Card
class HowItWorks(generic.TemplateView):
    template_name = "payment/how_it_works.html"

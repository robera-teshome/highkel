from django.shortcuts import render

# Create your views here.

def home(request):
	return render(request,'home.html')
	
def about(request):
	return render(request,'about.html')

def appointment(request):
	return render(request,'appointment.html')

def blog_details(request):
	return render(request,'blog-details.html')
def blog_sidebar(request):
	return render(request,'blog_sidebar.html')
def contact(request):
	return render(request,'contact.html')
def error_404(request):
	return render(request,'error_404.html')
def login(request):
	return render(request,'login.html')
def portfolio_category(request):
	return render(request,'portfolio_category.html')
def portfolio_details(request):
	return render(request,'portfolio_details.html')
def portfolio(request):
	return render(request,'portfolio.html')	
def posts_by_author(request):
	return render(request,'posts_by_author.html')	
def posts_by_date(request):
	return render(request,'posts_by_date.html')	
def posts_by_tag(request):
	return render(request,'posts_by_tag.html')	
def pricing_plan(request):
	return render(request,'pricing_plan.html')
def privacy_policy(request):
	return render(request,'privacy_policy.html')
def recover_password(request):
	return render(request,'recover_password.html')	
def register(request):
	return render(request,'register.html')	
def service_details(request):
	return render(request,'service_details.html')	
def service_one(request):
	return render(request,'service_one.html')	
def service_two(request):
	return render(request,'service_two.html')	
def team(request):
	return render(request,'team.html')	
def terms_of_service(request):
	return render(request,'terms_of_service.html')			
def testimonials(request):
	return render(request,'testimonials.html')					
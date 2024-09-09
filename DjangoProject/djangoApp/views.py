from django.shortcuts import render, get_object_or_404, redirect
from .models import FrameWork_Varity, Framework_Reviews, Framework_courses, FrameWork_certificate, EnrolledCourse
from .forms import ReviewForm
from django.contrib.auth.decorators import login_required

def items(request):
    frameworks = FrameWork_Varity.objects.all()
    return render(request, 'djangoApp/items.html', {'frameworks': frameworks})

def framework_details(request, framework_id):
    framework = get_object_or_404(FrameWork_Varity, pk=framework_id)
    reviews = Framework_Reviews.objects.filter(framework=framework)
    courses = Framework_courses.objects.filter(framework=framework)
    certificates = FrameWork_certificate.objects.filter(framework=framework)

    enrolled_courses = []
    if request.user.is_authenticated:
        enrolled_courses = EnrolledCourse.objects.filter(user=request.user).values_list('course', flat=True)

    return render(request, 'djangoApp/framework_details.html', {
        'framework': framework,
        'reviews': reviews,
        'courses': courses,
        'certificates': certificates,
        'enrolled_courses': enrolled_courses,
    })

@login_required
def enroll_course(request, course_id):
    course = get_object_or_404(Framework_courses, id=course_id)
    user = request.user

    # Check if the user is already enrolled in this course
    if EnrolledCourse.objects.filter(user=user, course=course).exists():
        # Redirect to the course detail page with a message
        return redirect('course_detail', course_id=course_id)

    # Enroll the user
    EnrolledCourse.objects.create(user=user, course=course)

    # Redirect to the course detail page
    return redirect('course_detail', course_id=course_id)

@login_required
def enroll_confirmation(request, course_id):
    course = get_object_or_404(Framework_courses, id=course_id)
    review_form = ReviewForm()
    return render(request, 'djangoApp/enroll_in_course.html', {
        'course': course,
        'review_form': review_form,
    })

@login_required
def submit_review(request, course_id):
    course = get_object_or_404(Framework_courses, id=course_id)
    framework = course.framework

    if EnrolledCourse.objects.filter(user=request.user, course=course).exists():
        if request.method == 'POST':
            form = ReviewForm(request.POST)
            if form.is_valid():
                review = form.cleaned_data['review']
                rating = form.cleaned_data['rating']
                
                Framework_Reviews.objects.create(
                    framework=framework, 
                    user=request.user, 
                    review=review, 
                    rating=rating
                )
                return redirect('framework_details', framework_id=framework.id)
    return redirect('framework_details', framework_id=framework.id)

@login_required
def course_detail(request, course_id):
    course = get_object_or_404(Framework_courses, id=course_id)
    return render(request, 'djangoApp/course_detail.html', {'course': course})

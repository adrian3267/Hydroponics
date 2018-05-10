from django.contrib.auth.models import User
from main.models import PageContent
from django.contrib.auth.decorators import login_required

def get_header_data(request):
    header_data = {
        'header_line1_label': 'Invalid User',
        'header_line1_value': '',
        'header_line2_label': '',
        'header_line2_value': '',
        'header_line3_label': '',
        'header_line3_value': '',
        'header_line4_label': '',
        'header_line4_value': '',
    }
    if request.session.get('user_type', None) is not None:
        user_type = request.session['user_type']

        # language = 'portuguese'
        # page_content = PageContent.objects.values(language)
        if user_type == 'Embraco':
            header_data = {
                      'header_line1_label': 'User:',
                      'header_line1_value': request.user.get_full_name,
                      'header_line2_label': 'Area:',
                      'header_line2_value': request.user.embracoprofile.department,
                      'header_line3_label': '',
                      'header_line3_value': '',
                      'header_line4_label': '',
                      'header_line4_value': '',
            }
        elif user_type == 'Supplier':
            header_data = {
                      'header_line1_label': 'Supplier:',
                      'header_line1_value': request.user.get_full_name,
                      'header_line2_label': 'Product:',
                      'header_line2_value': request.user.supplierprofile.contactPerson,
                      'header_line3_label': '',
                      'header_line3_value': '',
                      'header_line4_label': '',
                      'header_line4_value': '',
            }
    return header_data
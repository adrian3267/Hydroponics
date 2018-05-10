def verify_certification_session(request):
    certification = request.session.get('certification', None)
    if certification is not None:
        return certification
    else:
        return False
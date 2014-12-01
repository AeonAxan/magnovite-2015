from app.main.models import Profile


def profile(request):
    if request.user.is_authenticated():
        try:
            profile = request.user.profile
            return {'profile' : profile}
        except Profile.DoesNotExist:
            pass

    return {'profile': ''}


def upload_photo_user(instance, filename):
    return 'user_{0}/photo/{1}'.format(instance.user.id, filename)

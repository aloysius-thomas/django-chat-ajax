def user_image_upload_location(instance, filename):
    extension = filename.split(".")[1].lower()
    filename = str(instance)
    filename = filename.replace(" ", "-")
    filename = filename + "." + extension
    return '%s/%s' % ("user/profile/", filename)

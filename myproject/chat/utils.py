def attachment_upload_location(instance, filename):
    try:
        extension = filename.split(".")[1].lower()
        extension = "." + extension
    except Exception as e:
        print(e, "Handled")
        extension = ""
    filename = str(instance.id)
    filename = filename.replace(" ", "-")
    filename = filename + extension
    location = "chat_attachments" + "/" + instance.chat_id + "/" + instance.attachment_type
    return '%s/%s' % (location, filename)

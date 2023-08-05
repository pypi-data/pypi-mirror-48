# Django messaging application

This messaging app has to be integrated into an existing django website.

## Quick start

1. Add "messaging" to your INSTALLED_APPS setting like this:
```
INSTALLED_APPS = [  
    ...  
    'django_markdown_messaging',  
]
```

2. Include the messaging URLconf in your project urls.py like this:
```
path('msg/', include(('django_markdown_messaging.urls', 'messaging'))),
```

3. Run `python manage.py migrate` to create the messaging models.

4. Start the development server and visit http://127.0.0.1:8000/msg to check if everything is ok.

## How to use

1. Go to http://127.0.0.1:8000/msg and click on "new message"
2. Write your message using plain text or markdown syntax
3. You can choose to allow editing or deleting of this message
4. Then, click on "Save" button
5. Link of the message appears on screen, just copy and paste it to your friends! :-)
6. If you go on the message page, you'll see your message and eventually a link to edit or delete this message.

## Override those ugly templates

You can add a *templates/messaging* folder in your base application to override default templates.

There are four pages that you can override safely:
- **[base.html](https://gitlab.com/aloha68/django-markdown-messaging/blob/master/django_markdown_messaging/templates/messaging/base.html)**: the base page for all the messaging templates
- **[index.html](https://gitlab.com/aloha68/django-markdown-messaging/blob/master/django_markdown_messaging/templates/messaging/index.html)**: index page with a form to search a message
- **[message.html](https://gitlab.com/aloha68/django-markdown-messaging/blob/master/django_markdown_messaging/templates/messaging/message.html)**: page to display an existing message
- **[edit-message.html](https://gitlab.com/aloha68/django-markdown-messaging/blob/master/django_markdown_messaging/templates/messaging/edit-message.html)**: page to add a new message or to edit an existing one

If you have any questions, I can help you! :-)

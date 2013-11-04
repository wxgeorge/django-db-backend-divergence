django-db-backend-divergence
============================

Minimal Django app exhibiting difference between the sqlite3 and mysql database backends when aggregating datetime fields
with extra SQL.

# Details of this Example
Two models: Users and Subscriptions. Subscriptions apply to users and have an expiry time. We are interested in computing the latest expiry time for any User.

This is computed here by qualifying every queryset concerning User models with extra sql that takes a MAX over all expiry times for that user.

When settings.DATABASES['ENGINE']='django.db.backends.mysql',

```
>./manage.py aggregated_datetime_type
database engine: mysql
aggregated datatime type: <type 'datetime.datetime'>
```

When settings.DATABASES['ENGINE']='django.db.backends.sqlite3'

```
>./manage.py aggregated_datetime_type
database engine: sqlite3
aggregated datatime type: <type 'unicode'>
```

# Run it yourself
Clone this project, syncdb, and run './manage.py aggregated_datetime_type' to see the data type associated with current
database backend.

# One Solution:
Make better use of the Django ORM to auto-populate aggregate computed fields, using [annotate](https://docs.djangoproject.com/en/1.5/topics/db/aggregation/#generating-aggregates-for-each-item-in-a-queryset). Thanks to [ramiromorales](http://twitter.com/ramiromorales) for pointing this out on the [Django users group](https://groups.google.com/d/msg/django-users/I7sUcqCacxE/Crcbwp2uScsJ).

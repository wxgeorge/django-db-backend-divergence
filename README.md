django-db-backend-divergence
============================

Small Django app exhibiting a divergence between the sqlite3 and mysql database backends when aggregating datetime fields.

# Details
Two models: Users and Subscriptions. Subscriptions apply to users and have an expiry time. We are interested in computing the latest expiry time for any User.

This is computed here by qualifies every queryset concerning User models with extra sql that takes a MAX over all expiry times for that user.

When the database engine 

- is mysql, the extra field is a datetime object
- is sqlite, the extra field is a unicode object


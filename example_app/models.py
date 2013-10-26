from django.db import models

class UserManager(models.Manager):
  def get_query_set(self):
    qset = super(UserManager, self).get_query_set()
    qset = qset.extra(select={'expiry_dt':'SELECT MAX(sub.end_dt) '\
                                          '  FROM example_app_subscription AS sub '\
                                          '  WHERE sub.user_id=id'})
    return qset


class User(models.Model):
  objects=UserManager()

class Subscription(models.Model):
  user = models.ForeignKey(User)
  end_dt = models.DateTimeField()


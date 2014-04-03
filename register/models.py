from django.db import models

class info(models.Model):
    name = models.CharField(max_length=100, default='NONE')
    password = models.CharField(max_length=50, default='NONE')
    year = models.IntegerField(default=0)
    roll = models.CharField(max_length=8, default='NONE')
    branch = models.CharField(max_length=45, default='NONE')
    mob_num = models.CharField(max_length=13, default='NONE')
    email_id = models.CharField(max_length=100, primary_key=True)
    gender = models.CharField(max_length=2, default='M')
    dob = models.CharField(max_length=11, default='NONE')
    verify = models.BooleanField(default=False)
    rand = models.CharField(max_length=21, default='NONE')
    def __unicode__(self):
        return self.email_id

class resume(models.Model):
    email_id = models.CharField(max_length=100, primary_key=True)
    q1 = models.CharField(max_length=2000, default='NONE')
    q2 = models.CharField(max_length=2000, default='NONE')
    q3 = models.CharField(max_length=2000, default='NONE')
    q4 = models.CharField(max_length=2000, default='NONE')
    def __unicode__(self):
        return self.email_id


class info_user(models.Model):
    email_id = models.CharField(max_length=100, primary_key=True)
    info_user_1 = models.CharField(max_length=1000, default='NONE')
    info_user_2 = models.CharField(max_length=1000, default='NONE')
    def __unicode__(self):
        return self.email_id


class review_exec(models.Model):
    email_id = models.CharField(max_length=100, primary_key=True)
    review_executive_1 = models.CharField(max_length=1000, default='NONE')
    review_executive_2 = models.CharField(max_length=1000, default='NONE')
    def __unicode__(self):
        return self.email_id


from django.db import models

# Create your models here.
class User(models.Model):
    username_text = models.CharField(db_column='Username', max_length=50)
    first_name_text = models.CharField(db_column='FirstName', max_length=50)
    last_name_text = models.CharField(db_column='LastName', max_length=50)
    join_date = models.DateTimeField(db_column='date joined')
    def __str__(self):
        return self.username_text + ' (' + self.first_name_text + ' ' + self.last_name_text + ')'

class AccountType(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    account_type_text = models.CharField(db_column='AccountType', max_length=50)
    def __str__(self):
        return self.account_type_text

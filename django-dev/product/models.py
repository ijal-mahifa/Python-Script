# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class NikeCrawl(models.Model):
    id = models.CharField(primary_key=True, max_length=500)
    title = models.CharField(max_length=500, blank=True, null=True)
    subtitle = models.CharField(max_length=500, blank=True, null=True)
    status = models.CharField(max_length=500, blank=True, null=True)
    stylecode = models.CharField(db_column='styleCode', max_length=500, blank=True, null=True)  # Field name made lowercase.
    colorcode = models.CharField(db_column='colorCode', max_length=500, blank=True, null=True)  # Field name made lowercase.
    stylecolor = models.CharField(db_column='styleColor', max_length=500, blank=True, null=True)  # Field name made lowercase.
    colordescription = models.CharField(db_column='colorDescription', max_length=500, blank=True, null=True)  # Field name made lowercase.
    genders = models.TextField(blank=True, null=True)  # This field type is a guess.
    sporttags = models.TextField(db_column='sportTags', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    quantitylimit = models.IntegerField(db_column='quantityLimit', blank=True, null=True)  # Field name made lowercase.
    styletype = models.CharField(db_column='styleType', max_length=500, blank=True, null=True)  # Field name made lowercase.
    producttype = models.CharField(db_column='productType', max_length=500, blank=True, null=True)  # Field name made lowercase.
    country = models.CharField(max_length=500, blank=True, null=True)
    currency = models.CharField(max_length=500, blank=True, null=True)
    currentprice = models.FloatField(db_column='currentPrice', blank=True, null=True)  # Field name made lowercase.
    available = models.BooleanField(blank=True, null=True)
    imageurls = models.CharField(db_column='imageUrls', max_length=500, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'nike_crawl'

# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-09-23 17:16
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models, transaction,connection
import django.db.models.deletion
import django.utils.timezone
import jsonfield.fields
import model_utils.fields
import json
from manati_ui.models import Weblog,AnalysisSession,AnalysisSessionUsers,User

def dictfetchall(cursor):
    "Return all rows from a cursor as a dict"
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]


def get_all_weblogs(self, id=None):
    with connection.cursor() as cursor:
        if id:
            cursor.execute("SELECT * FROM manati_weblogs WHERE id = %s", [id])
        else:
            cursor.execute("SELECT * FROM manati_weblogs")
        row = dictfetchall(cursor)
    return row

def update_attributes_raw_weblog(id, attributes_json, new_id):
    with connection.cursor() as cursor:
        cursor.execute("UPDATE manati_weblogs SET attributes = %s, id = %s WHERE id = %s", [attributes_json, new_id, id])


def update_weblogs(apps, schema_editor):
    # Weblog.objects.all().update(id="".join([F('id'), str(":"), F('analysis_session_id')]))
    for weblog in Weblog.objects.all():
        old_attributes = get_all_weblogs(weblog.id)[0]
        old_attributes.pop("id", None)
        old_attributes.pop("created_at", None)
        old_attributes.pop('verdict', None)
        old_attributes.pop('updated_at', None)
        old_attributes.pop('register_status', None)
        old_attributes.pop('analysis_session_id', None)
        old_attributes.pop('attributes', None)
        old_attributes.pop('mod_attributes', None)
        new_id = str(weblog.analysis_session_id) + ":" + str(weblog.id)
        attributes = json.dumps(old_attributes)
        update_attributes_raw_weblog(str(weblog.id), attributes,new_id)

    for weblog in Weblog.objects.all():
        if len(weblog.id.split(':')) <= 1:
            weblog.delete()

    current_user = User.objects.get(id=1)
    for analysis_session in AnalysisSession.objects.all():
        AnalysisSessionUsers.objects.create(analysis_session_id=analysis_session.id,
                                            user_id=current_user.id,
                                            columns_order=json.dumps({}))

class Migration(migrations.Migration):
    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('manati_ui', '0005_auto_20160923_1716'),
    ]

    operations = [
        ## updating Weblogs IDs and updating copying old attributes to new parameter IDs
        migrations.RunPython(update_weblogs),
        migrations.RunSQL('SET CONSTRAINTS ALL IMMEDIATE',
                          reverse_sql=migrations.RunSQL.noop),

    ]
# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-11-04 09:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manati_ui', '0014_moduleauxweblog'),
    ]

    operations = [
        migrations.AlterField(
            model_name='weblog',
            name='verdict',
            field=models.CharField(choices=[('malicious', 'Malicious'), ('legitimate', 'Legitimate'), ('suspicious', 'Suspicious'), ('undefined', 'Undefined'), ('falsepositive', 'False Positive'), ('malicious_legitimate', 'Malicious/Legitimate'), ('suspicious_legitimate', 'Suspicious/Legitimate'), ('undefined_legitimate', 'Undefined/Legitimate'), ('falsepositive_legitimate', 'False Positive/Legitimate'), ('undefined_malicious', 'Undefined/Malicious'), ('suspicious_malicious', 'Suspicious/Malicious'), ('falsepositive_malicious', 'False Positive/Malicious'), ('falsepositive_suspicious', 'False Positive/Suspicious'), ('undefined_suspicious', 'Undefined/Suspicious'), ('undefined_falsepositive', 'Undefined/False Positive')], default='undefined', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='webloghistory',
            name='old_verdict',
            field=models.CharField(choices=[('malicious', 'Malicious'), ('legitimate', 'Legitimate'), ('suspicious', 'Suspicious'), ('undefined', 'Undefined'), ('falsepositive', 'False Positive'), ('malicious_legitimate', 'Malicious/Legitimate'), ('suspicious_legitimate', 'Suspicious/Legitimate'), ('undefined_legitimate', 'Undefined/Legitimate'), ('falsepositive_legitimate', 'False Positive/Legitimate'), ('undefined_malicious', 'Undefined/Malicious'), ('suspicious_malicious', 'Suspicious/Malicious'), ('falsepositive_malicious', 'False Positive/Malicious'), ('falsepositive_suspicious', 'False Positive/Suspicious'), ('undefined_suspicious', 'Undefined/Suspicious'), ('undefined_falsepositive', 'Undefined/False Positive')], default='undefined', max_length=50),
        ),
        migrations.AlterField(
            model_name='webloghistory',
            name='verdict',
            field=models.CharField(choices=[('malicious', 'Malicious'), ('legitimate', 'Legitimate'), ('suspicious', 'Suspicious'), ('undefined', 'Undefined'), ('falsepositive', 'False Positive'), ('malicious_legitimate', 'Malicious/Legitimate'), ('suspicious_legitimate', 'Suspicious/Legitimate'), ('undefined_legitimate', 'Undefined/Legitimate'), ('falsepositive_legitimate', 'False Positive/Legitimate'), ('undefined_malicious', 'Undefined/Malicious'), ('suspicious_malicious', 'Suspicious/Malicious'), ('falsepositive_malicious', 'False Positive/Malicious'), ('falsepositive_suspicious', 'False Positive/Suspicious'), ('undefined_suspicious', 'Undefined/Suspicious'), ('undefined_falsepositive', 'Undefined/False Positive')], default='undefined', max_length=50),
        ),
    ]
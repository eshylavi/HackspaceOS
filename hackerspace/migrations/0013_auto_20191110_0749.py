# Generated by Django 2.2.6 on 2019-11-10 07:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hackerspace', '0012_space_one_guilde'),
    ]

    operations = [
        migrations.AlterField(
            model_name='consensusitem',
            name='boolean_meeting_1_passed',
            field=models.BooleanField(default=False, verbose_name='Passed Meeting 1?'),
        ),
        migrations.AlterField(
            model_name='consensusitem',
            name='boolean_meeting_2_passed',
            field=models.BooleanField(default=False, verbose_name='Passed Meeting 1?'),
        ),
        migrations.AlterField(
            model_name='consensusitem',
            name='one_created_by',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='o_created_by', to='hackerspace.Person', verbose_name='Created by'),
        ),
        migrations.AlterField(
            model_name='consensusitem',
            name='str_name',
            field=models.CharField(blank=True, max_length=250, null=True, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='consensusitem',
            name='text_description',
            field=models.TextField(blank=True, null=True, verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='event',
            name='int_UNIXtime_event_end',
            field=models.IntegerField(blank=True, null=True, verbose_name='Event end (UNIX time)'),
        ),
        migrations.AlterField(
            model_name='event',
            name='int_UNIXtime_event_start',
            field=models.IntegerField(blank=True, null=True, verbose_name='Event start (UNIX time)'),
        ),
        migrations.AlterField(
            model_name='event',
            name='int_minutes_duration',
            field=models.IntegerField(default=60, verbose_name='Duration in minutes'),
        ),
        migrations.AlterField(
            model_name='event',
            name='int_series_endUNIX',
            field=models.IntegerField(blank=True, null=True, verbose_name='Series End (UNIX time)'),
        ),
        migrations.AlterField(
            model_name='event',
            name='int_series_startUNIX',
            field=models.IntegerField(blank=True, null=True, verbose_name='Series Start (UNIX time)'),
        ),
        migrations.AlterField(
            model_name='event',
            name='many_hosts',
            field=models.ManyToManyField(blank=True, related_name='m_persons', to='hackerspace.Person', verbose_name='Hosts'),
        ),
        migrations.AlterField(
            model_name='event',
            name='one_guilde',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='o_guilde', to='hackerspace.Guilde', verbose_name='Guilde'),
        ),
        migrations.AlterField(
            model_name='event',
            name='one_space',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='o_space', to='hackerspace.Space', verbose_name='Space'),
        ),
        migrations.AlterField(
            model_name='event',
            name='str_location_city',
            field=models.CharField(default='San Francisco', max_length=50, verbose_name='Location City'),
        ),
        migrations.AlterField(
            model_name='event',
            name='str_location_countrycode',
            field=models.CharField(default='US', max_length=50, verbose_name='Location Country Code'),
        ),
        migrations.AlterField(
            model_name='event',
            name='str_location_name',
            field=models.CharField(default='Noisebridge', max_length=250, verbose_name='Location Name'),
        ),
        migrations.AlterField(
            model_name='event',
            name='str_location_street',
            field=models.CharField(default='2169 Mission St', max_length=250, verbose_name='Location Street'),
        ),
        migrations.AlterField(
            model_name='event',
            name='str_location_zip',
            field=models.CharField(default='94110', max_length=10, verbose_name='Location ZIP'),
        ),
        migrations.AlterField(
            model_name='event',
            name='str_name',
            field=models.CharField(blank=True, max_length=250, null=True, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='event',
            name='str_series_id',
            field=models.CharField(blank=True, max_length=250, null=True, verbose_name='Series ID'),
        ),
        migrations.AlterField(
            model_name='event',
            name='str_timezone',
            field=models.CharField(blank=True, default='America/Los_Angeles', max_length=100, null=True, verbose_name='Timezone'),
        ),
        migrations.AlterField(
            model_name='event',
            name='text_description',
            field=models.TextField(blank=True, null=True, verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='event',
            name='url_discuss_event',
            field=models.URLField(blank=True, max_length=250, null=True, verbose_name='Discuss URL'),
        ),
        migrations.AlterField(
            model_name='event',
            name='url_featured_photo',
            field=models.URLField(blank=True, null=True, verbose_name='Photo URL'),
        ),
        migrations.AlterField(
            model_name='event',
            name='url_meetup_event',
            field=models.URLField(blank=True, max_length=250, null=True, verbose_name='Meetup URL'),
        ),
        migrations.AlterField(
            model_name='event',
            name='url_slack_event',
            field=models.URLField(blank=True, max_length=250, null=True, verbose_name='Slack URL'),
        ),
        migrations.AlterField(
            model_name='guilde',
            name='many_members',
            field=models.ManyToManyField(blank=True, related_name='m_members', to='hackerspace.Person', verbose_name='Members'),
        ),
        migrations.AlterField(
            model_name='guilde',
            name='str_name',
            field=models.CharField(blank=True, max_length=250, null=True, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='guilde',
            name='text_description',
            field=models.TextField(blank=True, null=True, verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='guilde',
            name='url_featured_photo',
            field=models.URLField(blank=True, null=True, verbose_name='Photo URL'),
        ),
        migrations.AlterField(
            model_name='guilde',
            name='url_wiki',
            field=models.URLField(blank=True, null=True, verbose_name='Wiki URL'),
        ),
        migrations.AlterField(
            model_name='machine',
            name='one_guilde',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='o_machine_guilde', to='hackerspace.Guilde', verbose_name='Guilde'),
        ),
        migrations.AlterField(
            model_name='machine',
            name='one_space',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='o_machine_space', to='hackerspace.Space', verbose_name='Space'),
        ),
        migrations.AlterField(
            model_name='machine',
            name='str_name',
            field=models.CharField(blank=True, max_length=250, null=True, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='machine',
            name='text_description',
            field=models.TextField(blank=True, null=True, verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='machine',
            name='url_featured_photo',
            field=models.URLField(blank=True, null=True, verbose_name='Photo URL'),
        ),
        migrations.AlterField(
            model_name='machine',
            name='url_wiki',
            field=models.URLField(blank=True, null=True, verbose_name='Wiki URL'),
        ),
        migrations.AlterField(
            model_name='person',
            name='str_name',
            field=models.CharField(blank=True, max_length=250, null=True, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='person',
            name='text_description',
            field=models.TextField(blank=True, null=True, verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='person',
            name='url_featured_photo',
            field=models.URLField(blank=True, null=True, verbose_name='Photo URL'),
        ),
        migrations.AlterField(
            model_name='person',
            name='url_wiki',
            field=models.URLField(blank=True, null=True, verbose_name='Wiki URL'),
        ),
        migrations.AlterField(
            model_name='space',
            name='one_guilde',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='o_spaces_guilde', to='hackerspace.Guilde', verbose_name='Guilde'),
        ),
        migrations.AlterField(
            model_name='space',
            name='str_name',
            field=models.CharField(blank=True, max_length=250, null=True, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='space',
            name='text_description',
            field=models.TextField(blank=True, null=True, verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='space',
            name='url_featured_photo',
            field=models.URLField(blank=True, null=True, verbose_name='Photo URL'),
        ),
        migrations.AlterField(
            model_name='space',
            name='url_wiki',
            field=models.URLField(blank=True, null=True, verbose_name='Wiki URL'),
        ),
    ]
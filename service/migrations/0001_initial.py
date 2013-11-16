# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Service'
        db.create_table(u'service_service', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('process_id', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('cost', self.gf('django.db.models.fields.DecimalField')(max_digits=20, decimal_places=2)),
            ('service_input', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('service_output', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('pre_requirements', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('max_bandwidth', self.gf('django.db.models.fields.DecimalField')(max_digits=50, decimal_places=9)),
            ('min_bandwidth', self.gf('django.db.models.fields.DecimalField')(max_digits=50, decimal_places=9)),
            ('delay', self.gf('django.db.models.fields.TimeField')()),
            ('date_created', self.gf('django.db.models.fields.DateTimeField')()),
            ('date_modified', self.gf('django.db.models.fields.DateTimeField')()),
            ('date_used', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal(u'service', ['Service'])

        # Adding M2M table for field service_type on 'Service'
        m2m_table_name = db.shorten_name(u'service_service_service_type')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('service', models.ForeignKey(orm[u'service.service'], null=False)),
            ('servicetype', models.ForeignKey(orm[u'service.servicetype'], null=False))
        ))
        db.create_unique(m2m_table_name, ['service_id', 'servicetype_id'])

        # Adding model 'ServiceType'
        db.create_table(u'service_servicetype', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('category', self.gf('django.db.models.fields.CharField')(max_length=20, null=True, blank=True)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
        ))
        db.send_create_signal(u'service', ['ServiceType'])


    def backwards(self, orm):
        # Deleting model 'Service'
        db.delete_table(u'service_service')

        # Removing M2M table for field service_type on 'Service'
        db.delete_table(db.shorten_name(u'service_service_service_type'))

        # Deleting model 'ServiceType'
        db.delete_table(u'service_servicetype')


    models = {
        u'service.service': {
            'Meta': {'ordering': "['name', 'process_id']", 'object_name': 'Service'},
            'cost': ('django.db.models.fields.DecimalField', [], {'max_digits': '20', 'decimal_places': '2'}),
            'date_created': ('django.db.models.fields.DateTimeField', [], {}),
            'date_modified': ('django.db.models.fields.DateTimeField', [], {}),
            'date_used': ('django.db.models.fields.DateTimeField', [], {}),
            'delay': ('django.db.models.fields.TimeField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'max_bandwidth': ('django.db.models.fields.DecimalField', [], {'max_digits': '50', 'decimal_places': '9'}),
            'min_bandwidth': ('django.db.models.fields.DecimalField', [], {'max_digits': '50', 'decimal_places': '9'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'pre_requirements': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'process_id': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'service_input': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'service_output': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'service_type': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'symmetrical': 'False', 'to': u"orm['service.ServiceType']"})
        },
        u'service.servicetype': {
            'Meta': {'ordering': "['name']", 'object_name': 'ServiceType'},
            'category': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        }
    }

    complete_apps = ['service']
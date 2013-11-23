# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Service.date_modified'
        db.alter_column(u'service_service', 'date_modified', self.gf('django.db.models.fields.DateTimeField')(null=True))

        # Changing field 'Service.max_bandwidth'
        db.alter_column(u'service_service', 'max_bandwidth', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=50, decimal_places=9))

        # Changing field 'Service.delay'
        db.alter_column(u'service_service', 'delay', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=50, decimal_places=3))

        # Changing field 'Service.date_used'
        db.alter_column(u'service_service', 'date_used', self.gf('django.db.models.fields.DateTimeField')(null=True))

        # Changing field 'Service.min_bandwidth'
        db.alter_column(u'service_service', 'min_bandwidth', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=50, decimal_places=9))

    def backwards(self, orm):

        # User chose to not deal with backwards NULL issues for 'Service.date_modified'
        raise RuntimeError("Cannot reverse this migration. 'Service.date_modified' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration
        # Changing field 'Service.date_modified'
        db.alter_column(u'service_service', 'date_modified', self.gf('django.db.models.fields.DateTimeField')())

        # User chose to not deal with backwards NULL issues for 'Service.max_bandwidth'
        raise RuntimeError("Cannot reverse this migration. 'Service.max_bandwidth' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration
        # Changing field 'Service.max_bandwidth'
        db.alter_column(u'service_service', 'max_bandwidth', self.gf('django.db.models.fields.DecimalField')(max_digits=50, decimal_places=9))

        # User chose to not deal with backwards NULL issues for 'Service.delay'
        raise RuntimeError("Cannot reverse this migration. 'Service.delay' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration
        # Changing field 'Service.delay'
        db.alter_column(u'service_service', 'delay', self.gf('django.db.models.fields.DecimalField')(max_digits=50, decimal_places=3))

        # User chose to not deal with backwards NULL issues for 'Service.date_used'
        raise RuntimeError("Cannot reverse this migration. 'Service.date_used' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration
        # Changing field 'Service.date_used'
        db.alter_column(u'service_service', 'date_used', self.gf('django.db.models.fields.DateTimeField')())

        # User chose to not deal with backwards NULL issues for 'Service.min_bandwidth'
        raise RuntimeError("Cannot reverse this migration. 'Service.min_bandwidth' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration
        # Changing field 'Service.min_bandwidth'
        db.alter_column(u'service_service', 'min_bandwidth', self.gf('django.db.models.fields.DecimalField')(max_digits=50, decimal_places=9))

    models = {
        u'service.service': {
            'Meta': {'ordering': "['name', 'process_id']", 'object_name': 'Service'},
            'cost': ('django.db.models.fields.DecimalField', [], {'max_digits': '20', 'decimal_places': '2'}),
            'date_created': ('django.db.models.fields.DateTimeField', [], {}),
            'date_modified': ('django.db.models.fields.DateTimeField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'date_used': ('django.db.models.fields.DateTimeField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'delay': ('django.db.models.fields.DecimalField', [], {'default': 'None', 'null': 'True', 'max_digits': '50', 'decimal_places': '3', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'max_bandwidth': ('django.db.models.fields.DecimalField', [], {'default': 'None', 'null': 'True', 'max_digits': '50', 'decimal_places': '9', 'blank': 'True'}),
            'min_bandwidth': ('django.db.models.fields.DecimalField', [], {'default': 'None', 'null': 'True', 'max_digits': '50', 'decimal_places': '9', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
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
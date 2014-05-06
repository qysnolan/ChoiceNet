# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Service.process_id'
        db.delete_column(u'service_service', 'process_id')

        # Deleting field 'Service.cost'
        db.delete_column(u'service_service', 'cost')

        # Deleting field 'Service.pre_requirements'
        db.delete_column(u'service_service', 'pre_requirements')

        # Deleting field 'Service.service_input'
        db.delete_column(u'service_service', 'service_input')

        # Deleting field 'Service.max_bandwidth'
        db.delete_column(u'service_service', 'max_bandwidth')

        # Deleting field 'Service.delay'
        db.delete_column(u'service_service', 'delay')

        # Deleting field 'Service.service_output'
        db.delete_column(u'service_service', 'service_output')

        # Deleting field 'Service.min_bandwidth'
        db.delete_column(u'service_service', 'min_bandwidth')

        # Adding field 'Service.service_id'
        db.add_column(u'service_service', 'service_id',
                      self.gf('django.db.models.fields.CharField')(default='0', max_length=255),
                      keep_default=False)

        # Adding field 'Service.service_type'
        db.add_column(u'service_service', 'service_type',
                      self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Service.hosted_node_id'
        db.add_column(u'service_service', 'hosted_node_id',
                      self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Service.end_point1_id'
        db.add_column(u'service_service', 'end_point1_id',
                      self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Service.end_point1_ip'
        db.add_column(u'service_service', 'end_point1_ip',
                      self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Service.end_point2_id'
        db.add_column(u'service_service', 'end_point2_id',
                      self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Service.end_point2_ip'
        db.add_column(u'service_service', 'end_point2_ip',
                      self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Service.service_bandwidth'
        db.add_column(u'service_service', 'service_bandwidth',
                      self.gf('django.db.models.fields.DecimalField')(default=0.0, max_digits=64, decimal_places=12),
                      keep_default=False)

        # Adding field 'Service.service_latency'
        db.add_column(u'service_service', 'service_latency',
                      self.gf('django.db.models.fields.DecimalField')(default=0.0, max_digits=64, decimal_places=12),
                      keep_default=False)

        # Adding field 'Service.service_cost'
        db.add_column(u'service_service', 'service_cost',
                      self.gf('django.db.models.fields.DecimalField')(default=0.0, max_digits=64, decimal_places=12),
                      keep_default=False)

        # Adding field 'Service.controller_id'
        db.add_column(u'service_service', 'controller_id',
                      self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Service.controller_ip'
        db.add_column(u'service_service', 'controller_ip',
                      self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Service.service_listings'
        db.add_column(u'service_service', 'service_listings',
                      self.gf('django.db.models.fields.CharField')(max_length=1024, null=True, blank=True),
                      keep_default=False)

        # Removing M2M table for field service_type on 'Service'
        db.delete_table(db.shorten_name(u'service_service_service_type'))


    def backwards(self, orm):
        # Adding field 'Service.process_id'
        db.add_column(u'service_service', 'process_id',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)


        # User chose to not deal with backwards NULL issues for 'Service.cost'
        raise RuntimeError("Cannot reverse this migration. 'Service.cost' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration        # Adding field 'Service.cost'
        db.add_column(u'service_service', 'cost',
                      self.gf('django.db.models.fields.DecimalField')(max_digits=20, decimal_places=2),
                      keep_default=False)

        # Adding field 'Service.pre_requirements'
        db.add_column(u'service_service', 'pre_requirements',
                      self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Service.service_input'
        db.add_column(u'service_service', 'service_input',
                      self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Service.max_bandwidth'
        db.add_column(u'service_service', 'max_bandwidth',
                      self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=50, decimal_places=9, blank=True),
                      keep_default=False)

        # Adding field 'Service.delay'
        db.add_column(u'service_service', 'delay',
                      self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=50, decimal_places=3, blank=True),
                      keep_default=False)

        # Adding field 'Service.service_output'
        db.add_column(u'service_service', 'service_output',
                      self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Service.min_bandwidth'
        db.add_column(u'service_service', 'min_bandwidth',
                      self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=50, decimal_places=9, blank=True),
                      keep_default=False)

        # Deleting field 'Service.service_id'
        db.delete_column(u'service_service', 'service_id')

        # Deleting field 'Service.service_type'
        db.delete_column(u'service_service', 'service_type')

        # Deleting field 'Service.hosted_node_id'
        db.delete_column(u'service_service', 'hosted_node_id')

        # Deleting field 'Service.end_point1_id'
        db.delete_column(u'service_service', 'end_point1_id')

        # Deleting field 'Service.end_point1_ip'
        db.delete_column(u'service_service', 'end_point1_ip')

        # Deleting field 'Service.end_point2_id'
        db.delete_column(u'service_service', 'end_point2_id')

        # Deleting field 'Service.end_point2_ip'
        db.delete_column(u'service_service', 'end_point2_ip')

        # Deleting field 'Service.service_bandwidth'
        db.delete_column(u'service_service', 'service_bandwidth')

        # Deleting field 'Service.service_latency'
        db.delete_column(u'service_service', 'service_latency')

        # Deleting field 'Service.service_cost'
        db.delete_column(u'service_service', 'service_cost')

        # Deleting field 'Service.controller_id'
        db.delete_column(u'service_service', 'controller_id')

        # Deleting field 'Service.controller_ip'
        db.delete_column(u'service_service', 'controller_ip')

        # Deleting field 'Service.service_listings'
        db.delete_column(u'service_service', 'service_listings')

        # Adding M2M table for field service_type on 'Service'
        m2m_table_name = db.shorten_name(u'service_service_service_type')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('service', models.ForeignKey(orm[u'service.service'], null=False)),
            ('servicetype', models.ForeignKey(orm[u'service.servicetype'], null=False))
        ))
        db.create_unique(m2m_table_name, ['service_id', 'servicetype_id'])


    models = {
        u'accounts.user': {
            'Meta': {'ordering': "['last_name', 'first_name']", 'object_name': 'User'},
            'accountType': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'date_joined': ('django.db.models.fields.DateTimeField', [], {}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'isSuper': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"}),
            'username': ('django.db.models.fields.EmailField', [], {'unique': 'True', 'max_length': '70'})
        },
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'service.service': {
            'Meta': {'ordering': "['name', 'service_id']", 'object_name': 'Service'},
            'controller_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'controller_ip': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'date_created': ('django.db.models.fields.DateTimeField', [], {}),
            'date_modified': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'date_used': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '3000', 'null': 'True', 'blank': 'True'}),
            'end_point1_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'end_point1_ip': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'end_point2_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'end_point2_ip': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'hosted_node_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'owner': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'service_owner'", 'null': 'True', 'to': u"orm['accounts.User']"}),
            'picture': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'service_bandwidth': ('django.db.models.fields.DecimalField', [], {'default': '0.0', 'max_digits': '64', 'decimal_places': '12'}),
            'service_cost': ('django.db.models.fields.DecimalField', [], {'default': '0.0', 'max_digits': '64', 'decimal_places': '12'}),
            'service_id': ('django.db.models.fields.CharField', [], {'default': "'0'", 'max_length': '255'}),
            'service_latency': ('django.db.models.fields.DecimalField', [], {'default': '0.0', 'max_digits': '64', 'decimal_places': '12'}),
            'service_listings': ('django.db.models.fields.CharField', [], {'max_length': '1024', 'null': 'True', 'blank': 'True'}),
            'service_type': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'})
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
# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Changing field 'Error.checksum'
        db.alter_column('djangodblog_error', 'checksum', self.gf('django.db.models.fields.CharField')(default='', max_length=32))

        # Changing field 'Error.datetime'
        db.alter_column('djangodblog_error', 'datetime', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True))

        # Removing index on 'Error', fields ['datetime']
        db.delete_index('djangodblog_error', ['datetime'])

        # Adding field 'ErrorBatch.datetime'
        db.add_column('djangodblog_errorbatch', 'datetime', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, default=None, db_index=True, blank=True), keep_default=False)

        # Changing field 'ErrorBatch.first_seen'
        db.alter_column('djangodblog_errorbatch', 'first_seen', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True))

        # Changing field 'ErrorBatch.last_seen'
        db.alter_column('djangodblog_errorbatch', 'last_seen', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True))


    def backwards(self, orm):
        
        # Adding index on 'Error', fields ['datetime']
        db.create_index('djangodblog_error', ['datetime'])

        # Changing field 'Error.checksum'
        db.alter_column('djangodblog_error', 'checksum', self.gf('django.db.models.fields.CharField')(max_length=32, null=True))

        # Changing field 'Error.datetime'
        db.alter_column('djangodblog_error', 'datetime', self.gf('django.db.models.fields.DateTimeField')())

        # Deleting field 'ErrorBatch.datetime'
        db.delete_column('djangodblog_errorbatch', 'datetime')

        # Changing field 'ErrorBatch.first_seen'
        db.alter_column('djangodblog_errorbatch', 'first_seen', self.gf('django.db.models.fields.DateTimeField')())

        # Changing field 'ErrorBatch.last_seen'
        db.alter_column('djangodblog_errorbatch', 'last_seen', self.gf('django.db.models.fields.DateTimeField')())


    models = {
        'djangodblog.error': {
            'Meta': {'object_name': 'Error'},
            'checksum': ('django.db.models.fields.CharField', [], {'max_length': '32', 'db_index': 'True'}),
            'class_name': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '128', 'null': 'True', 'blank': 'True'}),
            'data': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'datetime': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'level': ('django.db.models.fields.PositiveIntegerField', [], {'default': '40', 'db_index': 'True', 'blank': 'True'}),
            'logger': ('django.db.models.fields.CharField', [], {'default': "'root'", 'max_length': '64', 'db_index': 'True', 'blank': 'True'}),
            'message': ('django.db.models.fields.TextField', [], {}),
            'server_name': ('django.db.models.fields.CharField', [], {'max_length': '128', 'db_index': 'True'}),
            'traceback': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'})
        },
        'djangodblog.errorbatch': {
            'Meta': {'unique_together': "(('logger', 'server_name', 'checksum'),)", 'object_name': 'ErrorBatch'},
            'checksum': ('django.db.models.fields.CharField', [], {'max_length': '32', 'db_index': 'True'}),
            'class_name': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '128', 'null': 'True', 'blank': 'True'}),
            'datetime': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'db_index': 'True', 'blank': 'True'}),
            'first_seen': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_seen': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'db_index': 'True', 'blank': 'True'}),
            'level': ('django.db.models.fields.PositiveIntegerField', [], {'default': '40', 'db_index': 'True', 'blank': 'True'}),
            'logger': ('django.db.models.fields.CharField', [], {'default': "'root'", 'max_length': '64', 'db_index': 'True', 'blank': 'True'}),
            'message': ('django.db.models.fields.TextField', [], {}),
            'server_name': ('django.db.models.fields.CharField', [], {'max_length': '128', 'db_index': 'True'}),
            'status': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0', 'db_column': "'is_resolved'"}),
            'times_seen': ('django.db.models.fields.PositiveIntegerField', [], {'default': '1'}),
            'traceback': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['djangodblog']

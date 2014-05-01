# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Validation'
        db.create_table(u'loaderio_validation', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('token', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal(u'loaderio', ['Validation'])


    def backwards(self, orm):
        # Deleting model 'Validation'
        db.delete_table(u'loaderio_validation')


    models = {
        u'loaderio.validation': {
            'Meta': {'object_name': 'Validation'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'token': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['loaderio']
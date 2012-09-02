# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Sport.group'
        db.delete_column('sports_tracking_sport', 'group_id')

        # Deleting field 'Group.fraternities'
        db.delete_column('sports_tracking_group', 'fraternities_id')

        # Adding field 'Group.sport'
        db.add_column('sports_tracking_group', 'sport',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=0, to=orm['sports_tracking.Sport']),
                      keep_default=False)

        # Adding field 'Fraternity.group'
        db.add_column('sports_tracking_fraternity', 'group',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=0, to=orm['sports_tracking.Group']),
                      keep_default=False)


    def backwards(self, orm):
        # Adding field 'Sport.group'
        db.add_column('sports_tracking_sport', 'group',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=0, to=orm['sports_tracking.Group']),
                      keep_default=False)

        # Adding field 'Group.fraternities'
        db.add_column('sports_tracking_group', 'fraternities',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=0, to=orm['sports_tracking.Fraternity']),
                      keep_default=False)

        # Deleting field 'Group.sport'
        db.delete_column('sports_tracking_group', 'sport_id')

        # Deleting field 'Fraternity.group'
        db.delete_column('sports_tracking_fraternity', 'group_id')


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'sports_tracking.fraternity': {
            'Meta': {'object_name': 'Fraternity'},
            'group': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['sports_tracking.Group']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': "'200'"})
        },
        'sports_tracking.game': {
            'Meta': {'object_name': 'Game'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'teams': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['sports_tracking.Team']", 'symmetrical': 'False'}),
            'winner': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'games_won'", 'to': "orm['sports_tracking.Team']"})
        },
        'sports_tracking.group': {
            'Meta': {'object_name': 'Group'},
            'group': ('django.db.models.fields.CharField', [], {'default': "'A'", 'max_length': "'300'"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'sport': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['sports_tracking.Sport']"})
        },
        'sports_tracking.player': {
            'Meta': {'object_name': 'Player'},
            'fraternity': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['sports_tracking.Fraternity']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"})
        },
        'sports_tracking.sport': {
            'Meta': {'object_name': 'Sport'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'season': ('django.db.models.fields.CharField', [], {'default': "'FL'", 'max_length': "'300'"}),
            'type': ('django.db.models.fields.CharField', [], {'default': "'BB'", 'max_length': "'300'"})
        },
        'sports_tracking.team': {
            'Meta': {'object_name': 'Team'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'players': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['sports_tracking.Player']", 'symmetrical': 'False'})
        }
    }

    complete_apps = ['sports_tracking']
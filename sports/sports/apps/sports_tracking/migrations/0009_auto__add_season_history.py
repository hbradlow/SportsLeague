# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Season_history'
        db.create_table('sports_tracking_season_history', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('fraternity', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['sports_tracking.Fraternity'])),
            ('sport', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['sports_tracking.Sport'])),
            ('group', self.gf('django.db.models.fields.CharField')(default='A', max_length='300')),
        ))
        db.send_create_signal('sports_tracking', ['Season_history'])


    def backwards(self, orm):
        # Deleting model 'Season_history'
        db.delete_table('sports_tracking_season_history')


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
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': "'200'"}),
            'sport_history': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['sports_tracking.Sport']", 'through': "orm['sports_tracking.Season_history']", 'symmetrical': 'False'})
        },
        'sports_tracking.game': {
            'Meta': {'object_name': 'Game'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'league': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['sports_tracking.League']"}),
            'teams': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['sports_tracking.Team']", 'symmetrical': 'False'}),
            'winner': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'games_won'", 'to': "orm['sports_tracking.Team']"})
        },
        'sports_tracking.league': {
            'Meta': {'object_name': 'League'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'season': ('django.db.models.fields.CharField', [], {'max_length': "'300'"}),
            'sport': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['sports_tracking.Sport']"}),
            'teams': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['sports_tracking.Team']", 'symmetrical': 'False'})
        },
        'sports_tracking.player': {
            'Meta': {'object_name': 'Player'},
            'fraternity': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['sports_tracking.Fraternity']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"})
        },
        'sports_tracking.season_history': {
            'Meta': {'object_name': 'Season_history'},
            'fraternity': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['sports_tracking.Fraternity']"}),
            'group': ('django.db.models.fields.CharField', [], {'default': "'A'", 'max_length': "'300'"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'sport': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['sports_tracking.Sport']"})
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
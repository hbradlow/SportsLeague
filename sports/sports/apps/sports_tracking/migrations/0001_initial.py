# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Sport'
        db.create_table('sports_tracking_sport', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('type', self.gf('django.db.models.fields.CharField')(default='BB', max_length='300')),
            ('slug', self.gf('django_extensions.db.fields.AutoSlugField')(allow_duplicates=False, max_length=50, separator=u'-', blank=True, unique=True, populate_from='type', overwrite=False)),
            ('season', self.gf('django.db.models.fields.CharField')(default='FL', max_length='300')),
            ('is_major', self.gf('django.db.models.fields.BooleanField')(default=True)),
        ))
        db.send_create_signal('sports_tracking', ['Sport'])

        # Adding model 'Player'
        db.create_table('sports_tracking_player', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
        ))
        db.send_create_signal('sports_tracking', ['Player'])

        # Adding model 'Team'
        db.create_table('sports_tracking_team', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
        ))
        db.send_create_signal('sports_tracking', ['Team'])

        # Adding M2M table for field players on 'Team'
        db.create_table('sports_tracking_team_players', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('team', models.ForeignKey(orm['sports_tracking.team'], null=False)),
            ('player', models.ForeignKey(orm['sports_tracking.player'], null=False))
        ))
        db.create_unique('sports_tracking_team_players', ['team_id', 'player_id'])

        # Adding model 'Game'
        db.create_table('sports_tracking_game', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('visitor_team', self.gf('django.db.models.fields.related.ForeignKey')(related_name='visitor_team', to=orm['sports_tracking.Team'])),
            ('home_team', self.gf('django.db.models.fields.related.ForeignKey')(related_name='home_team', to=orm['sports_tracking.Team'])),
            ('winner', self.gf('django.db.models.fields.related.ForeignKey')(related_name='games_won', null=True, to=orm['sports_tracking.Team'])),
            ('is_tie', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('sport', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['sports_tracking.Sport'])),
            ('parent', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['sports_tracking.Game'], null=True, blank=True)),
            ('location', self.gf('django.db.models.fields.CharField')(max_length='200')),
            ('date', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal('sports_tracking', ['Game'])

        # Adding model 'Fraternity'
        db.create_table('sports_tracking_fraternity', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length='200')),
        ))
        db.send_create_signal('sports_tracking', ['Fraternity'])

        # Adding M2M table for field teams on 'Fraternity'
        db.create_table('sports_tracking_fraternity_teams', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('fraternity', models.ForeignKey(orm['sports_tracking.fraternity'], null=False)),
            ('team', models.ForeignKey(orm['sports_tracking.team'], null=False))
        ))
        db.create_unique('sports_tracking_fraternity_teams', ['fraternity_id', 'team_id'])

        # Adding model 'Meeting'
        db.create_table('sports_tracking_meeting', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('description', self.gf('django.db.models.fields.TextField')(null=True)),
            ('date', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal('sports_tracking', ['Meeting'])

        # Adding M2M table for field fraternities_attended on 'Meeting'
        db.create_table('sports_tracking_meeting_fraternities_attended', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('meeting', models.ForeignKey(orm['sports_tracking.meeting'], null=False)),
            ('fraternity', models.ForeignKey(orm['sports_tracking.fraternity'], null=False))
        ))
        db.create_unique('sports_tracking_meeting_fraternities_attended', ['meeting_id', 'fraternity_id'])

        # Adding model 'Group'
        db.create_table('sports_tracking_group', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('group', self.gf('django.db.models.fields.CharField')(default='A', max_length='300')),
            ('sport', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['sports_tracking.Sport'])),
        ))
        db.send_create_signal('sports_tracking', ['Group'])

        # Adding M2M table for field fraternities on 'Group'
        db.create_table('sports_tracking_group_fraternities', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('group', models.ForeignKey(orm['sports_tracking.group'], null=False)),
            ('fraternity', models.ForeignKey(orm['sports_tracking.fraternity'], null=False))
        ))
        db.create_unique('sports_tracking_group_fraternities', ['group_id', 'fraternity_id'])

        # Adding model 'Contact'
        db.create_table('sports_tracking_contact', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('fraternity', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['sports_tracking.Fraternity'])),
            ('contact_name', self.gf('django.db.models.fields.CharField')(max_length='200')),
            ('contact_number', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
        ))
        db.send_create_signal('sports_tracking', ['Contact'])


    def backwards(self, orm):
        # Deleting model 'Sport'
        db.delete_table('sports_tracking_sport')

        # Deleting model 'Player'
        db.delete_table('sports_tracking_player')

        # Deleting model 'Team'
        db.delete_table('sports_tracking_team')

        # Removing M2M table for field players on 'Team'
        db.delete_table('sports_tracking_team_players')

        # Deleting model 'Game'
        db.delete_table('sports_tracking_game')

        # Deleting model 'Fraternity'
        db.delete_table('sports_tracking_fraternity')

        # Removing M2M table for field teams on 'Fraternity'
        db.delete_table('sports_tracking_fraternity_teams')

        # Deleting model 'Meeting'
        db.delete_table('sports_tracking_meeting')

        # Removing M2M table for field fraternities_attended on 'Meeting'
        db.delete_table('sports_tracking_meeting_fraternities_attended')

        # Deleting model 'Group'
        db.delete_table('sports_tracking_group')

        # Removing M2M table for field fraternities on 'Group'
        db.delete_table('sports_tracking_group_fraternities')

        # Deleting model 'Contact'
        db.delete_table('sports_tracking_contact')


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
        'sports_tracking.contact': {
            'Meta': {'object_name': 'Contact'},
            'contact_name': ('django.db.models.fields.CharField', [], {'max_length': "'200'"}),
            'contact_number': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'fraternity': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['sports_tracking.Fraternity']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'sports_tracking.fraternity': {
            'Meta': {'object_name': 'Fraternity'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': "'200'"}),
            'teams': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['sports_tracking.Team']", 'symmetrical': 'False'})
        },
        'sports_tracking.game': {
            'Meta': {'object_name': 'Game'},
            'date': ('django.db.models.fields.DateTimeField', [], {}),
            'home_team': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'home_team'", 'to': "orm['sports_tracking.Team']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_tie': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'location': ('django.db.models.fields.CharField', [], {'max_length': "'200'"}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['sports_tracking.Game']", 'null': 'True', 'blank': 'True'}),
            'sport': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['sports_tracking.Sport']"}),
            'visitor_team': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'visitor_team'", 'to': "orm['sports_tracking.Team']"}),
            'winner': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'games_won'", 'null': 'True', 'to': "orm['sports_tracking.Team']"})
        },
        'sports_tracking.group': {
            'Meta': {'object_name': 'Group'},
            'fraternities': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['sports_tracking.Fraternity']", 'symmetrical': 'False'}),
            'group': ('django.db.models.fields.CharField', [], {'default': "'A'", 'max_length': "'300'"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'sport': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['sports_tracking.Sport']"})
        },
        'sports_tracking.meeting': {
            'Meta': {'object_name': 'Meeting'},
            'date': ('django.db.models.fields.DateTimeField', [], {}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True'}),
            'fraternities_attended': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['sports_tracking.Fraternity']", 'symmetrical': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'sports_tracking.player': {
            'Meta': {'object_name': 'Player'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"})
        },
        'sports_tracking.sport': {
            'Meta': {'object_name': 'Sport'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_major': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'season': ('django.db.models.fields.CharField', [], {'default': "'FL'", 'max_length': "'300'"}),
            'slug': ('django_extensions.db.fields.AutoSlugField', [], {'allow_duplicates': 'False', 'max_length': '50', 'separator': "u'-'", 'blank': 'True', 'unique': 'True', 'populate_from': "'type'", 'overwrite': 'False'}),
            'type': ('django.db.models.fields.CharField', [], {'default': "'BB'", 'max_length': "'300'"})
        },
        'sports_tracking.team': {
            'Meta': {'object_name': 'Team'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'players': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['sports_tracking.Player']", 'symmetrical': 'False'})
        }
    }

    complete_apps = ['sports_tracking']
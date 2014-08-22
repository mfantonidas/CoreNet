# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'corenet_ne'
        db.create_table(u'CoreNE_corenet_ne', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=50)),
            ('ipaddr', self.gf('django.db.models.fields.IPAddressField')(unique=True, max_length=15)),
            ('netype', self.gf('django.db.models.fields.CharField')(unique=True, max_length=20)),
            ('snmpaddr', self.gf('django.db.models.fields.IPAddressField')(max_length=15, blank=True)),
            ('uplink', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True)),
        ))
        db.send_create_signal(u'CoreNE', ['corenet_ne'])

        # Adding model 'softxinfo'
        db.create_table(u'CoreNE_softxinfo', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('locate', self.gf('django.db.models.fields.CharField')(max_length=5)),
            ('area', self.gf('django.db.models.fields.CharField')(unique=True, max_length=20)),
            ('localaddr', self.gf('django.db.models.fields.IPAddressField')(max_length=15)),
            ('residue_fccus', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('lp', self.gf('django.db.models.fields.IntegerField')()),
            ('rchs', self.gf('django.db.models.fields.IntegerField')()),
            ('csc', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'CoreNE', ['softxinfo'])

        # Adding model 'IMSinfo'
        db.create_table(u'CoreNE_imsinfo', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('area', self.gf('django.db.models.fields.CharField')(unique=True, max_length=20)),
            ('imssub_action', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('imssub_ac', self.gf('django.db.models.fields.IntegerField')()),
            ('imssub_nc', self.gf('django.db.models.fields.CharField')(max_length=5)),
            ('imssub_domain', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('imssub_usertype', self.gf('django.db.models.fields.IntegerField')()),
            ('imssub_imputplid', self.gf('django.db.models.fields.IntegerField')()),
            ('imssub_sptplid', self.gf('django.db.models.fields.IntegerField')()),
            ('imssub_chargtplid', self.gf('django.db.models.fields.IntegerField')()),
            ('imssub_captplid', self.gf('django.db.models.fields.IntegerField')()),
            ('NAPTRRecord_zonename', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('NAPTRRecord_order', self.gf('django.db.models.fields.IntegerField')()),
            ('NAPTRRecord_preference', self.gf('django.db.models.fields.IntegerField')()),
            ('NAPTRRecord_flags', self.gf('django.db.models.fields.CharField')(max_length=5)),
            ('NAPTRRecord_service', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('NAPTRRecord_replacement', self.gf('django.db.models.fields.CharField')(max_length=5)),
            ('NAPTRRecord_ttl', self.gf('django.db.models.fields.IntegerField')()),
            ('MGWAGCF_gwtp', self.gf('django.db.models.fields.IntegerField')()),
            ('MGWAGCF_ptype', self.gf('django.db.models.fields.IntegerField')()),
            ('MGWAGCF_la', self.gf('django.db.models.fields.IPAddressField')(max_length=15)),
            ('MGWAGCF_pa', self.gf('django.db.models.fields.IPAddressField')(max_length=15)),
            ('MGWAGCF_masteragcf', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('MGWAGCF_slaveragcf', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('ASBRAGCF_regtp', self.gf('django.db.models.fields.IntegerField')()),
            ('ASBRAGCF_netid', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('ASBRAGCF_netinfo', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('ASBRAGCF_phncon', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('ASBRAGCF_digmap', self.gf('django.db.models.fields.IntegerField')(max_length=5)),
            ('ASBRAGCF_emgcn', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('SBR_nc', self.gf('django.db.models.fields.CharField')(max_length=5)),
            ('SBR_domain', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('SBR_lp', self.gf('django.db.models.fields.IntegerField')()),
            ('SBR_csc', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'CoreNE', ['IMSinfo'])


    def backwards(self, orm):
        # Deleting model 'corenet_ne'
        db.delete_table(u'CoreNE_corenet_ne')

        # Deleting model 'softxinfo'
        db.delete_table(u'CoreNE_softxinfo')

        # Deleting model 'IMSinfo'
        db.delete_table(u'CoreNE_imsinfo')


    models = {
        u'CoreNE.corenet_ne': {
            'Meta': {'object_name': 'corenet_ne'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ipaddr': ('django.db.models.fields.IPAddressField', [], {'unique': 'True', 'max_length': '15'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50'}),
            'netype': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '20'}),
            'snmpaddr': ('django.db.models.fields.IPAddressField', [], {'max_length': '15', 'blank': 'True'}),
            'uplink': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'})
        },
        u'CoreNE.imsinfo': {
            'ASBRAGCF_digmap': ('django.db.models.fields.IntegerField', [], {'max_length': '5'}),
            'ASBRAGCF_emgcn': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'ASBRAGCF_netid': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'ASBRAGCF_netinfo': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'ASBRAGCF_phncon': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'ASBRAGCF_regtp': ('django.db.models.fields.IntegerField', [], {}),
            'MGWAGCF_gwtp': ('django.db.models.fields.IntegerField', [], {}),
            'MGWAGCF_la': ('django.db.models.fields.IPAddressField', [], {'max_length': '15'}),
            'MGWAGCF_masteragcf': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'MGWAGCF_pa': ('django.db.models.fields.IPAddressField', [], {'max_length': '15'}),
            'MGWAGCF_ptype': ('django.db.models.fields.IntegerField', [], {}),
            'MGWAGCF_slaveragcf': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'Meta': {'object_name': 'IMSinfo'},
            'NAPTRRecord_flags': ('django.db.models.fields.CharField', [], {'max_length': '5'}),
            'NAPTRRecord_order': ('django.db.models.fields.IntegerField', [], {}),
            'NAPTRRecord_preference': ('django.db.models.fields.IntegerField', [], {}),
            'NAPTRRecord_replacement': ('django.db.models.fields.CharField', [], {'max_length': '5'}),
            'NAPTRRecord_service': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'NAPTRRecord_ttl': ('django.db.models.fields.IntegerField', [], {}),
            'NAPTRRecord_zonename': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'SBR_csc': ('django.db.models.fields.IntegerField', [], {}),
            'SBR_domain': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'SBR_lp': ('django.db.models.fields.IntegerField', [], {}),
            'SBR_nc': ('django.db.models.fields.CharField', [], {'max_length': '5'}),
            'area': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '20'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imssub_ac': ('django.db.models.fields.IntegerField', [], {}),
            'imssub_action': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'imssub_captplid': ('django.db.models.fields.IntegerField', [], {}),
            'imssub_chargtplid': ('django.db.models.fields.IntegerField', [], {}),
            'imssub_domain': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'imssub_imputplid': ('django.db.models.fields.IntegerField', [], {}),
            'imssub_nc': ('django.db.models.fields.CharField', [], {'max_length': '5'}),
            'imssub_sptplid': ('django.db.models.fields.IntegerField', [], {}),
            'imssub_usertype': ('django.db.models.fields.IntegerField', [], {})
        },
        u'CoreNE.softxinfo': {
            'Meta': {'object_name': 'softxinfo'},
            'area': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '20'}),
            'csc': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'localaddr': ('django.db.models.fields.IPAddressField', [], {'max_length': '15'}),
            'locate': ('django.db.models.fields.CharField', [], {'max_length': '5'}),
            'lp': ('django.db.models.fields.IntegerField', [], {}),
            'rchs': ('django.db.models.fields.IntegerField', [], {}),
            'residue_fccus': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['CoreNE']
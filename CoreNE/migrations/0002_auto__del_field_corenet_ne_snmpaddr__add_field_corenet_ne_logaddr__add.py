# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Removing unique constraint on 'corenet_ne', fields ['netype']
        db.delete_unique(u'CoreNE_corenet_ne', ['netype'])

        # Deleting field 'corenet_ne.snmpaddr'
        db.delete_column(u'CoreNE_corenet_ne', 'snmpaddr')

        # Adding field 'corenet_ne.logaddr'
        db.add_column(u'CoreNE_corenet_ne', 'logaddr',
                      self.gf('django.db.models.fields.IPAddressField')(default=111, max_length=15, blank=True),
                      keep_default=False)

        # Adding field 'corenet_ne.logname'
        db.add_column(u'CoreNE_corenet_ne', 'logname',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=50, blank=True),
                      keep_default=False)

        # Adding field 'corenet_ne.logpass'
        db.add_column(u'CoreNE_corenet_ne', 'logpass',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=50, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Adding field 'corenet_ne.snmpaddr'
        db.add_column(u'CoreNE_corenet_ne', 'snmpaddr',
                      self.gf('django.db.models.fields.IPAddressField')(default=111, max_length=15, blank=True),
                      keep_default=False)

        # Deleting field 'corenet_ne.logaddr'
        db.delete_column(u'CoreNE_corenet_ne', 'logaddr')

        # Deleting field 'corenet_ne.logname'
        db.delete_column(u'CoreNE_corenet_ne', 'logname')

        # Deleting field 'corenet_ne.logpass'
        db.delete_column(u'CoreNE_corenet_ne', 'logpass')

        # Adding unique constraint on 'corenet_ne', fields ['netype']
        db.create_unique(u'CoreNE_corenet_ne', ['netype'])


    models = {
        u'CoreNE.corenet_ne': {
            'Meta': {'object_name': 'corenet_ne'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ipaddr': ('django.db.models.fields.IPAddressField', [], {'unique': 'True', 'max_length': '15'}),
            'logaddr': ('django.db.models.fields.IPAddressField', [], {'max_length': '15', 'blank': 'True'}),
            'logname': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'logpass': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50'}),
            'netype': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
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
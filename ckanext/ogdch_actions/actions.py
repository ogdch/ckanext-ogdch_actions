from ckan import plugins as p

import ckan.lib.dictization
from ckan import logic

import pylons
import sqlalchemy

from ckanext.multilingual.plugin import translate_data_dict

_table_dictize = ckan.lib.dictization.table_dictize
_group_list_dictize = ckan.lib.dictization.model_dictize.group_list_dictize
_select = sqlalchemy.sql.select

class OGDActions(p.SingletonPlugin):
    p.implements(p.IActions)

    def get_actions(self):
        return {
            'term_translation_list': self.term_translation_list,
            'group_list_translated': self.group_list_translated,
            'dataset_count': self.dataset_count,
        }

    def term_translation_list(self, context, data_dict):
        '''Returns a list of all term translations

        :param lang_code: Filter for one language. If lang_code is empty,
            all term translations are returned

        '''

        model = context['model']

        lang_code = data_dict.get('lang_code', '')

        trans_table = model.term_translation_table

        q = _select([trans_table])

        if lang_code:
            q = q.where(trans_table.c.lang_code == lang_code)

        conn = model.Session.connection()
        cursor = conn.execute(q)

        results = []

        for row in cursor:
            results.append(_table_dictize(row, context))

        return results

    def group_list_translated(self, context, data_dict):
        ''' Returns all groups in the specified language

            :param lang: [de|en|fr|it] Language for translation
            :param type: [group|organization] Type of group to filter.
                         Default is group
        '''

        model = context['model']

        lang = data_dict.get('lang', 'de')
        group_type = data_dict.get('type', 'group')

        if group_type not in ('group', 'organization'):
            raise logic.ParameterError("Invalid type")
        is_org = group_type == 'organization'

        query = model.Session.query(model.Group).join(model.GroupRevision)
        query = query.filter(model.GroupRevision.state=='active')
        query = query.filter(model.GroupRevision.is_organization==is_org)

        orgs = query.all()

        data = _group_list_dictize(orgs, context)

        keys = ('id', 'name', 'title', 'description', 'image_url', 'packages')
        filtered = [dict((key, org[key]) for key in keys) for org in data]

        pylons.request.environ['CKAN_LANG'] = lang
        result = [translate_data_dict(org) for org in filtered]

        return result

    def dataset_count(self, context, data_dict):
        ''' Returns the total number of datasets '''

        model = context['model']

        query = model.Session.query(model.Package)
        query = query.filter(model.Package.state=='active')
        query = query.filter(model.Package.type=='dataset')

        return {'count': query.count()}

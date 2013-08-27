from ckan import plugins as p

import ckan.lib.dictization

import sqlalchemy

_table_dictize = ckan.lib.dictization.table_dictize

_select = sqlalchemy.sql.select

class TermTranslationActions(p.SingletonPlugin):
    p.implements(p.IActions)

    def get_actions(self):
        return {
            'term_translation_list': self.term_translation_list
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

import datetime

import pandas as pd
from pymongo import MongoClient

from config.logger import get_logger
from converter import constant
from util.util import Util


class NoSqlConverter:
    def __init__(self):
        self.logger = get_logger(self.__class__.__name__)

        self.config = Util().get_config()
        self.db = Util().get_db_connection()
        self.mongo_client = MongoClient(host=self.config['mongoDb']['host'],
                                        port=self.config['mongoDb']['port'])['gambling_simulation']['sports_data']

    def start(self):
        self.logger.info('start converter')

        for index, row in self.get_joined_table(start_id=self.last_converted_id()).iterrows():
            self.logger.debug('wipe game id: {}'.format(index))
            json_document = {}
            self.add_common_info(row, json_document, index)
            self.add_score(row, json_document)
            self.add_gamble_info(row, json_document)
            self.add_judgement_info(row, json_document)
            for group in self.get_prediction_groups():
                self.add_prediction_info(row, json_document, group)
                self.add_prediction_judgement_info(row, json_document, group)
            self.remove_nan_key(json_document)
            self.logger.debug('wiped document: {}'.format(json_document))
            self.mongo_client.insert_one(json_document)

    def get_prediction_groups(self):
        self.logger.debug('getting prediction group')
        cursor = self.db.cursor()
        cursor.execute("""show tables like 'prediction_data%'""")
        return [group[0][16:] for group in cursor.fetchall()]

    def add_common_info(self, row, json_document, index):
        self.logger.debug('add common info')

        json_document['_id'] = index
        json_document['game_id'] = index
        json_document['game_time'] = datetime.datetime.strptime('{} {}'.format(row['game_date'],
                                                                               row['play_time']),
                                                                '{} {}'.format(self.config['crawler']['dateFormat'],
                                                                               '%I:%M')).isoformat('T', 'minutes')
        json_document['gamble_id'] = row['gamble_id']
        json_document['game_type'] = row['game_type']
        return json_document

    def add_score(self, row, json_document):
        self.logger.debug('add score')
        json_document['guest'] = {'name': row['guest'],
                                  'score': row['guest_score']}

        json_document['host'] = {'name': row['host'],
                                 'score': row['host_score']}
        return json_document

    def add_gamble_info(self, row, json_document):
        self.logger.debug('add gamble info')
        json_document['gamble_info'] = {}
        json_document['gamble_info']['national'] = {
            'total_point': {'threshold': row['national_total_point_threshold']},
            'spread_point': {'host': row['national_host_point_spread'],
                             'response': {'on_hit': row[
                                 'response_ratio_if_hit_spread_point']}}}
        json_document['gamble_info']['local'] = {
            'total_point': {'threshold': row['local_total_point_threshold'],
                            'response': row[
                                'local_total_point_threshold_response_ratio']},
            'spread_point': {'host': row['local_host_point_spread'],
                             'response': {'host': row[
                                 'local_host_point_spread_response_ratio']}},
            'original': {'response': {
                'guest': row['local_origin_guest_response_ratio'],
                'host': row['local_origin_host_response_ratio']}}}
        return json_document

    def add_judgement_info(self, row, json_document):
        self.logger.debug('add judgement info')
        json_document['judgement'] = json_document.get('judgement', {})
        json_document['judgement']['game'] = json_document['judgement'].get('game', {})
        json_document['judgement']['game']['national'] = {
            'over_threshold': bool(row['over_total_point_national']),
            'spread_point': 'host' if row[
                'host_win_point_spread_national'] else 'guest'}
        json_document['judgement']['game']['local'] = {'over_threshold': bool(row['over_total_point_local']),
                                                       'spread_point': 'host' if row[
                                                           'host_win_point_spread_local'] else 'guest',
                                                       'original': 'host' if row[
                                                           'host_win_original'] else 'guest'}

    def add_prediction_info(self, row, json_document, group):
        self.logger.debug('add prediction info')
        json_document['prediction'] = json_document.get('prediction', [])
        json_document['prediction'].append({
            'group': group,
            'national': {
                'total_point': {
                    'over': {
                        'percentage': row['{}__{}'.format('percentage_national_total_point_over', group)],
                        'population': row['{}__{}'.format('population_national_total_point_over', group)]},
                    'under': {
                        'percentage': row['{}__{}'.format('percentage_national_total_point_under', group)],
                        'population': row['{}__{}'.format('population_national_total_point_under', group)]}},
                'spread_point': {
                    'guest': {
                        'percentage': row['{}__{}'.format('percentage_national_point_spread_guest', group)],
                        'population': row['{}__{}'.format('population_national_point_spread_guest', group)]},
                    'host': {
                        'percentage': row['{}__{}'.format('percentage_national_point_spread_host', group)],
                        'population': row['{}__{}'.format('population_national_point_spread_host', group)]}}},
            'local': {
                'total_point': {
                    'over': {
                        'percentage': row['{}__{}'.format('percentage_local_total_point_over', group)],
                        'population': row['{}__{}'.format('population_local_total_point_over', group)]},
                    'under': {
                        'percentage': row['{}__{}'.format('percentage_local_total_point_under', group)],
                        'population': row['{}__{}'.format('population_local_total_point_under', group)]}},
                'spread_point': {
                    'guest': {
                        'percentage': row['{}__{}'.format('percentage_local_point_spread_guest', group)],
                        'population': row['{}__{}'.format('population_local_point_spread_guest', group)]},
                    'host': {
                        'percentage': row['{}__{}'.format('percentage_local_point_spread_host', group)],
                        'population': row['{}__{}'.format('population_local_point_spread_host', group)]}},
                'original': {
                    'guest': {
                        'percentage': row['{}__{}'.format('percentage_local_original_guest', group)],
                        'population': row['{}__{}'.format('population_local_original_guest', group)]},
                    'host': {
                        'percentage': row['{}__{}'.format('percentage_local_original_host', group)],
                        'population': row['{}__{}'.format('population_local_original_host', group)]}}}})

    def add_prediction_judgement_info(self, row, json_document, group):
        self.logger.debug('add prediction judgement info')
        json_document['judgement'] = json_document.get('judgement', {})
        json_document['judgement']['prediction'] = json_document['judgement'].get('prediction', [])
        json_document['judgement']['prediction'].append({
            'group': group,
            'national': {
                'total_point': {
                    'matched_info': {
                        'is_major': bool(row['{}__{}'.format('national_total_point_result', group)]),
                        'percentage': row['{}__{}'.format('national_total_point_percentage', group)],
                        'population': row['{}__{}'.format('national_total_point_population', group)]}},
                'spread_point': {
                    'matched_info': {
                        'is_major': bool(row['{}__{}'.format('national_point_spread_result', group)]),
                        'percentage': row['{}__{}'.format('national_point_spread_percentage', group)],
                        'population': row['{}__{}'.format('national_point_spread_population', group)]}}},
            'local': {
                'total_point': {
                    'matched_info': {
                        'is_major': bool(row['{}__{}'.format('local_total_point_result', group)]),
                        'percentage': row['{}__{}'.format('local_total_point_percentage', group)],
                        'population': row['{}__{}'.format('local_total_point_population', group)]}},
                'spread_point': {
                    'matched_info': {
                        'is_major': bool(row['{}__{}'.format('local_point_spread_result', group)]),
                        'percentage': row['{}__{}'.format('local_point_spread_percentage', group)],
                        'population': row['{}__{}'.format('local_point_spread_population', group)]}},
                'original': {
                    'matched_info': {
                        'is_major': bool(row['{}__{}'.format('local_original_result', group)]),
                        'percentage': row['{}__{}'.format('local_original_percentage', group)],
                        'population': row['{}__{}'.format('local_original_population', group)]}}}})

    def remove_nan_key(self, json_document):
        for k, v in list(json_document.items()):
            self.logger.debug('check: {}-{}'.format(k, v))
            if isinstance(v, dict):
                self.remove_nan_key(v)
            elif isinstance(v, list):
                for e in v:
                    self.remove_nan_key(e)
            elif not pd.notnull(v):
                self.logger.debug('delete key-value: {}, {}'.format(k, v))
                json_document.pop(k, None)

    def iter_table_as_df(self):
        self.logger.info('start iterate db')
        # cursor = self.db.cursor()
        # cursor.execute('SHOW TABLES')
        for table_name in constant.joined_tables:
            self.logger.debug('get table: {}'.format(table_name))
            yield table_name, pd.read_sql('SELECT * FROM %s LIMIT 10' % (table_name), con=self.db, index_col='id')

    def get_joined_table(self, start_id=0):
        self.logger.info('start get joined table')
        sql_select = 'SELECT %s FROM game_data ' % ', '.join(constant.joined_columns)
        sql_join = ' '.join(['LEFT JOIN %s ON %s.id=game_data.id ' % (table_name, table_name)
                             for table_name in constant.joined_tables if table_name != 'game_data'])
        sql_where = 'WHERE game_data.id > %s' % start_id
        sql = sql_select + sql_join + sql_where
        return pd.read_sql(sql, con=self.db, index_col='id')

    def last_converted_id(self):
        return self.mongo_client.find().sort('_id', -1).limit(1).next()['_id']

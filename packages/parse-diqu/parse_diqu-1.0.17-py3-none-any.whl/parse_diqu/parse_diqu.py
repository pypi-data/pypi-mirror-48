# encoding=utf-8
import json
import os
import re
from lmf.dbv2 import db_query
from bs4 import BeautifulSoup
import jieba
import collections
import time
import pandas as  pd
from sqlalchemy import create_engine


# 连接数据库
def getpage_herf_ggstart_time(quyu):
    arr = quyu.split('*')
    db, schema = arr[0], arr[1]
    engine = create_engine('postgresql+psycopg2://postgres:zhulong.com.cn@192.168.169.47/%s' % (db))
    data_gg_html = pd.read_sql_table(table_name='gg_html', con=engine, schema=schema, index_col=None, coerce_float=True, parse_dates=None, columns=None, chunksize=None)
    df = data_gg_html[['href', 'page']]
    return df


# 读入数据库
def write_to_table(df, table_name, quyu, if_exists='replace'):
    import io
    import pandas as pd
    from sqlalchemy import create_engine
    arr = quyu.split('*')
    db, schema = arr[0], arr[1]
    db_engine = create_engine('postgresql+psycopg2:postgres:zhulong.com.cn@192.168.169.47/%s' % db)
    string_data_io = io.StringIO()
    df.to_csv(string_data_io, sep='|', index=False)
    pd_sql_engine = pd.io.sql.pandasSQL_builder(db_engine)
    table = pd.io.sql.SQLTable(table_name, pd_sql_engine, frame=df, index=False, if_exists=if_exists, schema=schema)
    table.create()
    string_data_io.seek(0)
    string_data_io.readline()  # remove header
    with db_engine.connect() as connection:
        with connection.connection.cursor() as cursor:
            copy_cmd = "COPY %s.%s FROM STDIN HEADER DELIMITER '|' CSV" % (schema, table_name)
            cursor.copy_expert(copy_cmd, string_data_io)
        connection.connection.commit()


class parseDiqu(object):
    def __init__(self):
        self.__jieba_init__()

    def __jieba_init__(self):
        json_path = os.path.join(os.path.dirname(__file__), 'xzqh_key_word.json')
        with open(json_path, 'r', encoding='utf-8') as f:
            self.xzqh_key_word = f.read()
        self.xzqh_key_word_dict_list = json.loads(self.xzqh_key_word)
        self.data = pd.DataFrame(self.xzqh_key_word_dict_list)
        self.new_diqu_list = []
        diqu = self.data['word'].tolist()
        self.new_diqu_list = []
        for d in diqu:
            self.new_diqu_list.extend(d.split(','))
        jieba.load_userdict(self.new_diqu_list)

    def t_page(self, page):
        if page is None:
            return []
        soup = BeautifulSoup(page, 'lxml')
        tmp = soup.find('style')
        if tmp is not None:
            tmp.clear()
        tmp = soup.find('script')
        if tmp is not None:
            tmp.clear()
        txt = re.sub('[^\u4E00-\u9Fa5a-zA-Z0-9:：\-\\/]', '', soup.text.strip())
        return txt

    def count_diqu(self, txt_list):
        object_list = []
        for word in jieba.cut(txt_list, cut_all=False):
            if word in self.new_diqu_list:
                object_list.append(json.dumps({word: self.data['code'][self.data['word'].str.contains(word)].tolist()[0]}, ensure_ascii=False))
        word_counts = collections.Counter(object_list)
        word_counts_top = word_counts.most_common(10)
        if word_counts_top != []:
            diqu_code1 = list(json.loads(word_counts_top[0][0]).values())[0]
            return diqu_code1
        else:
            return None

    def parse_diqu(self, page):
        """

        :param page: html 文本
        :return: diqu_code
        """
        txt_list = self.t_page(page)
        diqu_code = self.count_diqu(txt_list)
        return diqu_code




if __name__ == '__main__':
    bt = time.time()
    import os
    new_path = os.path.join(os.path.dirname(__file__),'公共区域')
    with open(new_path,'r') as f:areas = f.read()
    area_list = re.findall('\'([^\']+)\'',areas)
    list_all = area_list
    for quyu in list_all:
    # 链接数据库,读取数据
        df=getpage_herf_ggstart_time(quyu)
        p_diqu = parseDiqu()
        # conp = ['postgres', 'since2015', '192.168.3.171', 'anbang', 'anhui_anqing']
        # engine = create_engine('postgresql+psycopg2://%s:%s@%s/%s' % (conp[0], conp[1], conp[2], conp[3]))
        # df = pd.read_sql_table(table_name='gg_html', con=engine, schema=conp[4], index_col=None, coerce_float=True, parse_dates=None, columns=None, chunksize=None)
        df['diqu_code'] = df['page'].map(lambda x: p_diqu.parse_diqu(x))
        write_to_table(df, 'gg_qucode',quyu, if_exists='replace')
        print(df['diqu_code'].isnull().sum())
        print(df.info())
        # print(df['diqu_code'].value_counts())
    print(time.time() - bt)








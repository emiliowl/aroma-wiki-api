class Aroma(object):
    def build_from_csv(self, row):
        self.note = row['\ufeffNota']
        self.name = row['Nome Comum']
        self.bothanical_name = row['Nome Botânico']
        self.bothanical_family = row['Família Botânica']
        self.therapeutic_properties = row['Principais Propriedades Terapêuticas']
        self.recommendations = row['Principais Indicações']
        self.contraindication = row['Contraindicação']
        self.alchohols = row['Álcoois']
        self.aldehydes = row['Aldeídos']
        self.ketones = row['Cetonas']
        self.esters = row['Ésteres']
        self.phenols = row['Fenóis']
        self.oxides = row['Óxidos']
        self.terpenes = row['Terpenos']
        self.lactones = row['Lactonas']
        self.coumarins = row['Cumarinas']
        self.sesquiterpenes = row['Sesquiterpenos']
        self.picture = row['Picture']

        return self


    def to_dict(self):
        dic = dict()
        dic['note'] = self.note
        dic['name'] = self.name
        dic['bothanical_name'] = self.bothanical_name
        dic['bothanical_family'] = self.bothanical_family
        dic['therapeutic_properties'] = self.therapeutic_properties
        dic['recommendations'] = self.recommendations
        dic['contraindication'] = self.contraindication
        dic['alchohols'] = self.alchohols
        dic['aldehydes'] = self.aldehydes
        dic['ketones'] = self.ketones
        dic['esters'] = self.esters
        dic['phenols'] = self.phenols
        dic['oxides'] = self.oxides
        dic['terpenes'] = self.terpenes
        dic['lactones'] = self.lactones
        dic['coumarins'] = self.coumarins
        dic['sesquiterpenes'] = self.sesquiterpenes
        dic['picture'] = self.picture

        # you will thank me in your future endeavors ;)
        # import requests as r
        # res = r.get("https://api.qwant.com/api/search/images",
        #     params={
        #         'count': 1,
        #         'q': self.name,
        #         't': 'images',
        #         'safesearch': 1,
        #         'locale': 'en_US',
        #         'uiv': 4
        #     },
        #     headers={
        #         'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'
        #     }
        # )

        # if res.status_code == 200:
        #     ret = res.json()
        #     if len(ret.get('data').get('result').get('items')) > 0:
        #         dic['pic'] = ret.get('data').get('result').get('items')[0].get('media')

        return dic

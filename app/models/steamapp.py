from mongoengine import StringField
from mongoengine.fields import IntField, LongField, ListField, DictField

from app import db


class SteamApp(db.Document):
    appid = LongField(required=True, primary_key=True)
    image_icon_url = StringField()
    image_logo_url = StringField()
    name = StringField(required=True)
    playtime_2weeks = IntField()
    playtime_forever = IntField()
    type = StringField()
    controller_support = StringField()
    supported_languages = ListField()
    plataforms = DictField()
    metacritic = DictField()
    categories = ListField()
    genres = ListField()
    background = StringField()

    @staticmethod
    def create_from_app_info(app_info):
        app = SteamApp(appid=app_info['appid'])
        app.image_icon_url = app_info.get('img_icon_url')
        app.image_logo_url = app_info.get('img_logo_url')
        app.name = app_info['name']
        app.playtime_2weeks = app_info.get('playtime_2weeks')
        app.playtime_forever = app_info.get('playtime_forever')

        return app

    def set_cdata(self, cdata):
        info = cdata[str(self.appid)].get('data')
        if not info:
            return

        self.type = info['type']
        self.controller_support = info.get('controller_support')
        self.supported_languages = self._parse_supported_language(info.get('supported_languages'))
        self.plataforms = info.get('plataforms')

        self.categories = []
        for category in info.get('categories') or []:
            self.categories.append(category['description'])

        self.genres = []
        for genre in info.get('genres') or []:
            self.genres.append(genre['description'])

        self.background = info.get('background')

    @staticmethod
    def _parse_supported_language(langs):
        comment_pos = langs.rfind('<br>')
        if comment_pos > -1:
            langs = langs[:comment_pos]

        langs = langs.replace('<strong>*</strong>', '')
        langs = langs.replace('[b]*[/b]', '')
        langs = langs.replace('languages with full audio support', '')
        langs = langs.replace('(text only)', '')

        lang_list = langs.split(', ')
        formatted_list = []

        for lang in lang_list:
            formatted_list.append(lang.strip())

        return formatted_list

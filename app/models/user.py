from mongoengine import StringField, IntField
from mongoengine.fields import ListField

from app import db
from app.models.steamapp import SteamApp


class User(db.Document):
    steamid = StringField(required=True, primary_key=True)
    nickname = StringField(required=True)
    avatar = StringField()
    avatar_full = StringField()
    profile_url = StringField(required=True)
    realname = StringField()
    app_count = IntField()
    app_ids_list = ListField()
    task_id = StringField()

    token = str()

    @staticmethod
    def create_from_steamdata(steamdata):
        user = User(steamid=steamdata['steamid'])
        user.avatar = User._get_value(steamdata, 'avatar')
        user.avatar_full = User._get_value(steamdata, 'avatarfull')
        user.nickname = User._get_value(steamdata, 'personaname')
        user.profile_url = User._get_value(steamdata, 'profileurl')
        user.realname = User._get_value(steamdata, 'realname')
        return user

    @staticmethod
    def _get_value(steamdata, key):
        if key in steamdata.keys():
            return steamdata[key]
        else:
            return None

    def get_game_library(self):
        return SteamApp.objects.filter(appid__in=self.app_ids_list)

    def get_categories(self):
        return self.get_game_library().distinct(field="categories")

    def get_genres(self):
        return self.get_game_library().distinct(field="genres")

    def get_languages(self):
        return self.get_game_library().distinct(field="supported_languages")

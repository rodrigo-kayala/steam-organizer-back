from urllib.parse import urlencode
from urllib.request import urlopen

from flask import json

from app import app

__author__ = 'kayala'


def get_steam_userinfo(steam_id):
    options = {
        'key': app.config['STEAM_API_KEY'],
        'steamids': steam_id
    }
    url = 'http://api.steampowered.com/ISteamUser/GetPlayerSummaries/v0001/?{}'.format(urlencode(options))
    response = json.load(urlopen(url))
    return response['response']['players']['player'][0] or {}


def get_app_list(steam_id):
    options = {
        'key': app.config['STEAM_API_KEY'],
        'steamid': steam_id,
        'include_appinfo': 1,
        'format': 'json'
    }
    url = 'http://api.steampowered.com/IPlayerService/GetOwnedGames/v0001/?{}'.format(urlencode(options))
    response = json.load(urlopen(url))
    return response or {}


def get_app_cdata(app_id):
    options = {
        'appids': app_id
    }
    url = 'http://store.steampowered.com/api/appdetails?{}'.format(urlencode(options))

    response = json.load(urlopen(url))
    return response


def get_game_achievements(steam_id, app_id):
    options = {
        'key': app.config['STEAM_API_KEY'],
        'appid': app_id,
        'steamid': steam_id
    }
    url = 'http://api.steampowered.com/ISteamUserStats/GetPlayerAchievements/v0001/?{}'.format(urlencode(options))

    response = json.load(urlopen(url))
    return response

import re
from urllib.parse import urlencode

from flask.blueprints import Blueprint

from flask import redirect

from mongoengine import MultipleObjectsReturned, DoesNotExist
from app import oid, app

from app.models.user import User
from app.security import tokenutils
from app.security.decorators import logged_in
from app.steam import steamapiwapper

loginrest = Blueprint('login', __name__)

_steam_id_re = re.compile('steamcommunity.com/openid/id/(.*?)$')


@loginrest.route('/login')
@oid.loginhandler
def do_login():
    return oid.try_login('http://steamcommunity.com/openid')


@oid.after_login
def create_or_login(resp):
    match = _steam_id_re.search(resp.identity_url)
    steamdata = steamapiwapper.get_steam_userinfo(match.group(1))

    try:
        user = User.objects.get(steamid=steamdata['steamid'])
    except (MultipleObjectsReturned, DoesNotExist):
        user = User.create_from_steamdata(steamdata)
        user.save()

    params = {
        'id': tokenutils.create_auth_token(user)
    }

    return redirect(app.config['FRONTEND_URL'] + '?' + urlencode(params))


@loginrest.route('/users')
@logged_in
def get_user_info(**kwargs):
    return kwargs['user'].to_json()

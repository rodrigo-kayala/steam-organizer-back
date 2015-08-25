from time import sleep

from flask import Blueprint, jsonify
from flask.ext.mongoengine import json

from app import celery
from app.models.steamapp import SteamApp
from app.security import tokenutils
from app.security.decorators import logged_in
from app.security.tokenutils import get_user_from_auth_token
from app.steam import steamapiwapper

steamapprest = Blueprint('games', __name__)


@steamapprest.route('/apps', methods=['GET'])
@logged_in
def load_game_list(**kwargs):
    user = kwargs['user']
    return user.get_game_library().to_json()


@steamapprest.route('/apps/refresh', methods=['POST'])
@logged_in
def refresh_game_info(**kwargs):
    user = kwargs['user']
    task = update_game_library.apply_async(kwargs={'token': user.token})
    user.task_id = task.id
    user.save()
    tokenutils.update_user(user.token, user)
    return jsonify({}), 202


@steamapprest.route('/apps/refresh/status', methods=['GET'])
@logged_in
def refresh_game_info_status(**kwargs):
    user = kwargs['user']
    if not user.task_id or len(user.task_id) == 0:
        return jsonify({}), 404

    task = update_game_library.AsyncResult(user.task_id)

    if not task.info:
        response = {
            'state': str(task.state),
            'current': 0,
            'currentName': '',
            'total': 0
        }
    else:
        response = {
            'state': str(task.state),
            'current': task.info.get('current', 0),
            'currentName': task.info.get('currentName', ''),
            'total': task.info.get('total', 0)
        }

    return jsonify(response)


@steamapprest.route('/apps/categories', methods=['GET'])
@logged_in
def get_categories(**kwargs):
    user = kwargs['user']
    return json.json_util.dumps(user.get_categories())

@steamapprest.route('/apps/genres', methods=['GET'])
@logged_in
def get_genres(**kwargs):
    user = kwargs['user']
    return json.json_util.dumps(user.get_genres())

@steamapprest.route('/apps/languages', methods=['GET'])
@logged_in
def get_languages(**kwargs):
    user = kwargs['user']
    return json.json_util.dumps(user.get_languages())



@celery.task(bind=True)
def update_game_library(self, **kwargs):
    user = get_user_from_auth_token(kwargs['token'])
    user.app_count = steamapiwapper.get_app_list(user.steamid)['response']['game_count'] or 0
    apps = steamapiwapper.get_app_list(user.steamid)['response']['games'] or None
    user.app_ids_list = []
    current = 0

    for app in apps:
        current += 1
        app_entity = SteamApp.objects(appid=app['appid']).first()
        self.update_state(state='PROGRESS',
                          meta={'current': current,
                                'currentName': app['name'],
                                'total': user.app_count})

        if not app_entity or not app_entity.type:
            sleep(2)
            app_entity = SteamApp.create_from_app_info(app)
            app_entity.set_cdata(steamapiwapper.get_app_cdata(app_entity.appid))
            app_entity.save()

        user.app_ids_list.append(app_entity.appid)

    user.task_id = ''
    user.save()
    tokenutils.update_user(kwargs['token'], user)

    return {'current': current, 'total': user.app_count}

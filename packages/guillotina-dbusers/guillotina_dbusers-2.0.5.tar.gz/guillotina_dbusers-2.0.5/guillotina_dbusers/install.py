# -*- coding: utf-8 -*-
from guillotina import configure
from guillotina.addons import Addon
from guillotina.content import create_content_in_container
from guillotina.interfaces import ILayers
from guillotina.utils import get_authenticated_user_id

USERS_LAYER = 'guillotina_dbusers.interfaces.IDBUsersLayer'


@configure.addon(
    name="dbusers",
    title="Guillotina DB Users")
class DBUsersAddon(Addon):

    @classmethod
    async def install(self, site, request):
        registry = request.container_settings
        registry.for_interface(ILayers)['active_layers'] |= {
            USERS_LAYER
        }
        user = get_authenticated_user_id(request)
        await create_content_in_container(
            site, 'UserManager', 'users',
            creators=(user,), title='Users')
        await create_content_in_container(
            site, 'GroupManager', 'groups',
            creators=(user,), title='Groups')

    @classmethod
    async def uninstall(self, site, request):
        registry = request.container_settings
        registry.for_interface(ILayers)['active_layers'] -= {
            USERS_LAYER
        }
        if await site.async_contains('users'):
            await site.async_del('users')
        if await site.async_contains('groups'):
            await site.async_del('groups')

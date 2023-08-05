from . import users  # noqa
from . import groups # noqa
from guillotina import configure
from guillotina.api.content import DefaultPOST
from guillotina_dbusers.content.groups import IGroupManager
from guillotina_dbusers.content.users import IUserManager

# override some views...
configure.service(
    context=IGroupManager, method='POST', permission='guillotina.AddGroup'
)(DefaultPOST)


@configure.service(
    context=IUserManager, method='POST', permission='guillotina.AddUser')
class UserPOST(DefaultPOST):

    async def get_data(self):
        data = await super().get_data()
        if 'username' in data:
            data['id'] = data['username']
        elif 'id' in data:
            data['username'] = data['id']
        return data

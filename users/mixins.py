from braces.views._access import AccessMixin

class DispatcherMixin(AccessMixin):
    """
    Mixin allows you to require a user with `type_user` set to dispatcher.
    """
    def dispatch(self, request, *args, **kwargs):
        if request.user.type_user!='DP':
            return self.handle_no_permission(request)

        return super(DispatcherMixin, self).dispatch(
            request, *args, **kwargs)

        
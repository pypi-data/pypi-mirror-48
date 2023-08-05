from assemblyline import odm
from assemblyline.common import forge
Classification = forge.get_classification()

ACL = {"R", "W", "E"}


@odm.model(index=False, store=False)
class ApiKey(odm.Model):
    acl = odm.List(odm.Enum(values=ACL))  # Access control list for the apikey
    password = odm.Keyword()              # BCrypt hash of the password for the apikey


@odm.model(index=True, store=True)
class User(odm.Model):
    agrees_with_tos = odm.Date(index=False, store=False, default_set=True)  # Date the user agree with terms of service
    api_quota = odm.Integer(default=10, store=False)                        # Max number of concurrent API requests
    apikeys = odm.Mapping(odm.Compound(ApiKey), default={})                 # List of apikeys
    can_impersonate = odm.Boolean(default=False, index=False,
                                  store=False)                              # Allowed to query on behalf of others
    classification = odm.Classification(
        is_user_classification=True, copyto="__text__",
        default=Classification.UNRESTRICTED)                                # Max classification for the user
    dn = odm.Keyword(store=False, copyto="__text__", default_set=True)      # User certificate DN
    email = odm.Keyword(copyto="__text__", default_set=True)                # User's email address
    groups = odm.List(odm.Keyword(), copyto="__text__",
                      default=["USERS"])                                    # List of groups the user submits to
    is_active = odm.Boolean(default=True)                                   # is the user active
    is_admin = odm.Boolean(default=False)                                   # is the user an admin
    name = odm.Keyword(copyto="__text__")                                   # Full name of the user
    otp_sk = odm.Keyword(index=False, store=False, default_set=True)        # Secret key to generate one time passwords
    password = odm.Keyword(index=False, store=False)                        # BCrypt hash of the user's password
    submission_quota = odm.Integer(default=5, store=False)                  # Maximum number of concurrent submissions
    u2f_devices = odm.Mapping(odm.Keyword(), index=False,
                              store=False, default={})                      # Map of u2f security tokens
    uname = odm.Keyword(copyto="__text__")                                  # Username

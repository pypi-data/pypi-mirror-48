from assemblyline.common import forge

from assemblyline import odm

BODY_TYPES = {"TEXT", "MEMORY_DUMP", "GRAPH_DATA", "URL", "JSON"}
constants = forge.get_constants()
TAG_TYPES = sorted([x[0] for x in constants.STANDARD_TAG_TYPES])


@odm.model(index=True, store=False)
class Section(odm.Model):
    section_id = odm.Integer(index=False)                   # ID of the section to generate the tree
    body = odm.Optional(odm.Text(copyto="__text__"))        # Text body of the result section
    classification = odm.Classification()                   # Classification of the section
    truncated = odm.Boolean(index=False)                    # is the result section truncated of not
    finalized = odm.Boolean(index=False)                    # is the result section finalized or not
    title_text = odm.Text(copyto="__text__")                # Title of the section
    depth = odm.Integer(index=False)                        # Depth of the section
    parent_section_id = odm.Integer(index=False)            # ID of the parent section
    score = odm.Integer(index=False)                        # Score of the section
    body_format = odm.Enum(values=BODY_TYPES, index=False)  # Type of body in this section


@odm.model(index=True, store=False)
class Tag(odm.Model):
    classification = odm.Classification()   # Classification of the tag
    value = odm.Keyword(copyto="__text__")  # Value of the tag
    context = odm.Optional(odm.Keyword())   # Context of the tag
    type = odm.Enum(values=TAG_TYPES)       # Type of tag


@odm.model(index=True, store=True)
class ResultBody(odm.Model):
    truncated = odm.Boolean(index=False, store=False,
                            default=False)                  # is the result body truncated or not
    tags = odm.List(odm.Compound(Tag), default=[])          # List of tag objects
    score = odm.Integer(default=0)                          # Aggregate of the score for all sections
    sections = odm.List(odm.Compound(Section), default=[])  # List of sections


@odm.model(index=False, store=False)
class Milestone(odm.Model):
    service_started = odm.Date(default="NOW")    # Date the service started scanning
    service_completed = odm.Date(default="NOW")  # Date the service finished scanning


@odm.model(index=True, store=False)
class File(odm.Model):
    name = odm.Keyword(copyto="__text__")      # Name of the file
    sha256 = odm.Keyword(copyto="__text__")    # SHA256 hash of the file
    description = odm.Text(copyto="__text__")  # Description of the file
    classification = odm.Classification()      # Classification of the file


@odm.model(index=True, store=True)
class ResponseBody(odm.Model):
    milestones = odm.Compound(Milestone, default={})                    # Milestone block
    service_version = odm.Keyword(store=False)                          # Version of the service that ran on the file
    service_name = odm.Keyword(copyto="__text__")                       # Name of the service that scan the file
    service_tool_version = odm.Optional(odm.Keyword(copyto="__text__")) # Tool version of the service
    supplementary = odm.List(odm.Compound(File), default=[])            # List of supplementary files
    extracted = odm.List(odm.Compound(File), default=[])                # List of extracted files
    service_context = odm.Keyword(index=False, store=False,
                                  default_set=True)             # Context about the service that was running
    service_debug_info = odm.Keyword(index=False, store=False,
                                     default_set=True)          # Debug information where the service was processed


@odm.model(index=True, store=True)
class Result(odm.Model):
    classification = odm.Classification()                 # Aggregate classification for the result
    created = odm.Date(default="NOW")                     # Date at which the result object got created
    expiry_ts = odm.Date(store=False)                     # Expiry time stamp
    oversized = odm.Boolean(default=False)                # Is an oversized record
    response: ResponseBody = odm.Compound(ResponseBody)   # The body of the response from the service
    result: ResultBody = odm.Compound(ResultBody,
                                      default={})         # The result body
    sha256 = odm.Keyword(store=False)                     # SHA256 of the file the result object relates to
    drop_file = odm.Boolean(default=False)                # After this service is done, further stages don't need to run

    def build_key(self, conf_key=None):
        return self.help_build_key(
            self.sha256,
            self.response.service_name,
            self.response.service_version,
            conf_key
        )

    @staticmethod
    def help_build_key(sha256, service_name, service_version, conf_key=None):
        key_list = [
            sha256,
            service_name.replace('.', '_'),
            f"v{service_version.replace('.', '_')}"
        ]

        if conf_key:
            key_list.append('c' + conf_key.replace('.', '_'))
        else:
            key_list.append("c0")

        return '.'.join(key_list)

    def is_empty(self):
        if len(self.response.extracted) == 0 and \
                len(self.response.supplementary) == 0 and \
                len(self.result.tags) == 0 and \
                len(self.result.sections) == 0 and \
                self.result.score == 0:
            return True
        return False

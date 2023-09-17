from collections import OrderedDict

from rest_framework.renderers import JSONRenderer
from rest_framework.utils.serializer_helpers import ReturnList


class CustomJSONRenderer(JSONRenderer):
    data = {
        "info": {
            "message": "",
        },
        "data": {}
    }

    def render(self, data, accepted_media_type=None, renderer_context=None):
        if data:
            if "message" in data:
                self.data["info"]["message"] = data.pop("message")
            else:
                self.data["info"]["message"] = renderer_context["response"]\
                    .status_text

        self.data["info"]["status"] = renderer_context["response"].status_code

        if renderer_context["response"].status_code not in [200, 201, 204]:
            self.data["data"] = OrderedDict()
            self.data["info"]["response_type"] = "error"
            self._render_fail(data)
        else:
            self.data["info"]["attrs"] = []
            self._render_success(data)

        return super(
            CustomJSONRenderer, self
        ).render(self.data, accepted_media_type, renderer_context)

    def _render_success(self, data):
        if data is None:
            data = OrderedDict()

        if type(data) in (ReturnList, OrderedDict):
            self.data["info"]["response_type"] = "list"
            self.data["info"]["count"] = data["count"]\
                if "count" in data else 0
            self.data["info"]["next"] = data["next"]\
                if "next" in data else ""
            self.data["info"]["previous"] = data["previous"]\
                if "previous" in data else ""
            self.data["data"] = data\
                if "results" not in data else data["results"]

        else:
            self.data["info"]["response_type"] = "single"
            self.data["data"] = data

    def _render_fail(self, data):
        if "detail" in data:
            self.data["info"]["message"] = data["detail"]
            self.data["data"] = OrderedDict()
        else:
            messages = [i.__str__() for i in data]
            self.data["info"]["message"] = ",".join(messages)

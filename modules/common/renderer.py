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
        info = self.data["info"]
        data_info = info.setdefault("data", {})

        if data is None:
            data = OrderedDict()

        if isinstance(data, (ReturnList, OrderedDict)):
            info["response_type"] = "list"
            data_info.clear()
            data_info.update(data.get("results", data))
            info.update({
                "count": data.get("count", 0),
                "next": data.get("next", ""),
                "previous": data.get("previous", ""),
            })
        else:
            info["response_type"] = "single"
            data_info.clear()
            data_info.update(data)

    def _render_fail(self, data):
        info = self.data["info"]
        data_info = info.setdefault("data", {})

        if "detail" in data:
            info["message"] = data["detail"]
            data_info.clear()
        else:
            info["message"] = ",".join(map(str, data))
            data_info.clear()
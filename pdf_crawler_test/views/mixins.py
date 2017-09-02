from django.http import JsonResponse
from django.db.models import Model


class JSONResponseMixin(object):
    """
    A mixin that can be used to render a JSON response.
    """
    context_object_name = 'object_list'

    def render_to_response(self, context, **response_kwargs):
        """
        Returns a JSON response, transforming 'context' to make the payload.
        """
        # This parameter needed for rendering of JSON list instead of dictionary
        response_kwargs['safe'] = False

        return JsonResponse(
            self.get_data(context),
            **response_kwargs
        )

    def get_data(self, context):
        """
        Returns an object that will be serialized as JSON by json.dumps().
        Transforms model instances to dicts.
        """
        return [doc.to_dict() if isinstance(doc, Model) else doc \
                for doc in context[self.context_object_name]]
